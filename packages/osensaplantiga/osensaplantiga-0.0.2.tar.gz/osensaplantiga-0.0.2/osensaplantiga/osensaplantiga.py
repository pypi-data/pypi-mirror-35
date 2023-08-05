import sys
import glob
import serial
import json
from struct import *
from .minimalmodbusosensa import Instrument, SecurityError
import time

def serial_get_portlist():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    portlist = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            portlist.append(port)
            print(port)
        except (OSError, serial.SerialException):
            pass
    return portlist

class Pod():
    def __init__(self, port, modbus_id=247, baudrate=115200, parity=serial.PARITY_NONE, timeout=1.0, close_after_each_call=False):
        self.modbus = Instrument(port, modbus_id, close_after_each_call=close_after_each_call)
        self.modbus.serial.parity = parity
        self.modbus.serial.baudrate = baudrate
        self.modbus.serial.timeout = timeout
        self.main_dictionary = None
        self.crc_table = None

    def disconnect(self):
        self.modbus.serial.close()
    
    #read any value by naming it, can read calibrated and uncalibrated values
    def read(self, key, calibrated=True, JSON=False):
        serialization = self.main_dictionary[key]['serialization']
        if calibrated:
            address = self.main_dictionary[key]['address']
        else:
            key = "$" + key
            address = self.main_dictionary[key]['address']
        try:
            return unpack(serialization, self.modbus_read(address, calcsize(serialization)))
        except IOError as e:
            print(e)
            return None

    def dictionary(self, printStream=False):
        self.modbus.custom_command(0x01, 0x00)
        rxbytes = bytearray()
        try:
            lastReadTime = time.time()
            while True:
                bytes_to_read = self.modbus.serial.inWaiting() #shows number of bytes to receive
                # print('[BTR: {}]'.format(bytes_to_read))
                if (bytes_to_read == 0):
                    # Check if timeout exceeded
                    self.__timeout_checker(lastReadTime, time.time())
                if (bytes_to_read > 0):
                    # Update read time to current time
                    lastReadTime = time.time()
                    # Read response in serial port
                    response = self.modbus.serial.read(bytes_to_read) #reads the bytes
                    if (0 in response):
                        # Remove null character from string
                        temp = list(response)
                        temp.remove(0)
                        response = bytes(temp)
                        # Append response to string and exit loop
                        rxbytes.extend(response)
                        break
                    else:
                        rxbytes.extend(response)
        except KeyboardInterrupt:
            return 0
        # Remove extraneous elements that are non-ascii and not part of the JSON string
        text = ''
        braceCounter = 0
        for elem in rxbytes:
            if elem < 128:
                # If string is currently empty
                if (not text.strip()):
                    # If next element is not a starting brace, ignore
                    if (chr(elem) != '{'):
                        pass
                    # Otherwise, add to text and increment brace counter
                    else:
                        braceCounter += 1
                        text += chr(elem)
                # If string is not currently empty
                else:
                    # If next element is an opening curly brace, increment brace counter
                    if (chr(elem) == '{'):
                        braceCounter += 1
                    # Else if next element is a closing curly brace, decrement brace counter
                    elif (chr(elem) == '}'):
                        braceCounter -= 1
                    # Add element to string
                    text += chr(elem)
                    # If brace counter is zero, we have finished our json string and can exit
                    if (braceCounter == 0):
                        break
        if (printStream):
            print('{}\nRaw:\n{}'.format(text, rxbytes))
        self.main_dictionary = json.loads(text)
        return self.main_dictionary


    def led(self, color):
        subfunc = 0
        if color.lower() == 'green':
            value = 1
        elif color.lower() == 'red':
            value = 0
        else:
            print('Invalid LED color selection: {}'.format(color))
            return
        self.modbus.custom_command(subfunc, value)
    
    #modbus for reading the number of bytes you want
    def modbus_read(self, address, n_bytes): #2 addresses are 4 bytes which is 2 registers
        # Get # of registers (each register is 16-bits which is 2-bytes)
        n_registers = n_bytes/2
        bytearr = bytearray()
        # Read register values
        values = self.modbus.read_registers(address, int(n_registers))
        # Reconstruct byte array
        for elem in values: 
            bytearr.append(0x00FF & elem)
            bytearr.append((0xFF00 & elem) >> 8)
        # Return read bytes
        return bytearr
    
    #writes a value (proper number) to the given address based on serialization format
    def modbus_write_val(self, address, value, serialization): #takes a value to write
        success = False
        n_registers = int(calcsize(serialization)/2) #number of registers to writee to
        compartments = [None]*n_registers #a containter for the value
        modValue = pack(serialization,value) #convert the value to the correct serialization in bytes
        #now modify the bytes so the input format is right 
        i = 0
        j = 0
        #this feels like it shouldn't work but it does.
        while i <= n_registers:
            (compartments[j],) = unpack('H',modValue[i:i+2]) #separate the bytes into registers and put them into the 0-65536 range
            i += 2
            j += 1
        try:
            print('Writing {} to {:2X}'.format(compartments, address))
            self.modbus.write_registers(address,compartments)
            success = True
        except IOError as e:
            print('IOError occurred while writing...\n{}'.format(e))
        except ValueError as e:
            print('ValueError occurred while writing...\n{}'.format(e))
        return success
 
           
     #modbus command to write a byte to a given address       
    def modbus_write(self, address, byteToWrite):
        success = False
        try:
            print('Writing {:2X} to {:2X}'.format(byteToWrite, address))
            self.modbus.write_register(address, byteToWrite)
            success = True
        except IOError as e:
            print('IOError occurred while writing...\n{}'.format(e))
        except ValueError as e:
            print('ValueError occurred while writing...\n{}'.format(e))
        return success

    def crc_table_init(self):
        # Initialize crc_table
        self.crc_table = list(range(256))
    #	print('crc table before: {}'.format(crc_table))
        for i in range(0,256):
            crc = 0
            c = i
            for j in range(0, 8):
                if ((crc ^ c) & 0x0001):
                    crc = (crc >> 1) ^ 0xA001
                else:
                    crc = crc >> 1
                c = c >> 1
            self.crc_table[i] = crc
    #	print('crc table after: {}'.format(crc_table))

    def update_crc(self, crc, c):
        int_c = 0x00ff & c
        if (self.crc_table is None):
            # Initialize table
            self.crc_table_init()
        tmp = crc ^ int_c
        crc = (crc >> 8) ^ self.crc_table[tmp & 0xff]
        return crc
    
    #this checks for timeouts
    def __timeout_checker(self, startTime, currTime, timeout=5):
        if (currTime - startTime) >= timeout:
            raise TimeoutError
