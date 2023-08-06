import sys
import glob
import serial
import json
from struct import *
from .minimalmodbusosensa import Instrument, SecurityError
import time
from datetime import datetime
from dateutil import tz

def hexify(data):
    print(' '.join(['{:02X}'.format(ord(c)) for c in data]))

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

def view_records(records, show_accelerometer, show_gyroscope):
    d_ = []
    for r in records:
        d_ += r.floats
    d = list(map(list, zip(*d_)))
    import matplotlib.pyplot as plt
    import numpy as np
    t = np.linspace(0,len(d_)*0.00125, len(d_)).tolist()
    plt.xlabel('time (seconds)')
    if show_accelerometer:
        plt.plot(t, d[3], label='accel X')
        plt.plot(t, d[4], label='accel Y')
        plt.plot(t, d[5], label='accel Z')
    if show_gyroscope:
        plt.plot(t, d[0], label='gyro X')
        plt.plot(t, d[1], label='gyro Y')
        plt.plot(t, d[2], label='gyro Z')
    plt.legend(loc='best')
    plt.show()

def save_records(records, filename):
    datastring = ''
    for r in records:
        datastring += r.tocsv()
    file = open(filename, 'w')
    file.write(datastring)
    file.close()

def find_docks():
    import serial.tools.list_ports_windows
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    docks = list(filter(lambda x: x.serial_number.startswith('PTDK'), ports))
    return (list(map(lambda x: x.serial_number, docks)))

def dock_port(dock_serial_number):
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    return (list(filter(lambda x: x.serial_number == dock_serial_number, ports))[0]).device

def connect(dock_serial_number, baudrate=115200, modbus_id=247):
    portname = dock_port(dock_serial_number)
    pod = Pod(portname, modbus_id=modbus_id, baudrate=baudrate)
    pod.dictionary()
    pod.time_sync()
    return pod

class Record():
    def __init__(self, datab):
        self.databytes = datab
        self.crc_table = None
        # Split into data groups
        self.recordType = datab[0:2]
        self.uuid = datab[2:18]
        self.unixtime = datab[18:26]
        self.data = datab[26:-2]
        self.crc = datab[-2:]
        # Check if CRC is valid
        _crccheck = 0xFFFF
        for b in datab:
            _crccheck = self.update_crc(_crccheck, b)
        self.isvalid = (_crccheck == 0)
        # Parse data into gyro/accel short floats
        self.floats = []
        self.gdata = []
        self.adata = []
        i = 0
        while i < len(self.data):
            f = unpack('eeeeee', self.data[i:i+12])
            self.floats.append(f)
            # print('len: {:2d}\t({})'.format(len(self.data[i:i+6]), self.data[i:i+6]))
            self.gdata.append(unpack('eee', self.data[i:i+6]))
            i += 6
            # print('len: {:2d}\t({})'.format(len(self.data[i:i+6]), self.data[i:i+6]))
            self.adata.append(unpack('eee', self.data[i:i+6]))
            i += 6
        pass
    
    def print(self, include_headers=False):
        if (include_headers):
            print('Record type: {}'.format(self.recordType))
            print('UUID: {}'.format(self.uuid))
            print('Unix time: {}'.format(self.unixtime))
            print('')
        for i in range(len(self.gdata)):
            print('g: ({:+9.4f}, {:+9.4f}, {:+9.4f})     a: ({:+9.4f}, {:+9.4f}, {:+9.4f})'.format(self.gdata[i][0], self.gdata[i][1], self.gdata[i][2], self.adata[i][0], self.adata[i][1], self.adata[i][2]))
    
    def tocsv(self, include_headers=False):
        csv_string = ''
        if (include_headers):
            csv_string += 'Record type: {}\n'.format(self.recordType)
            csv_string += 'UUID: {}\n'.format(self.uuid)
            csv_string += 'Unix time: {}\n'.format(self.unixtime)
            csv_string += '\ngx,gy,gz,ax,ay,az\n'
        for i in range(len(self.gdata)):
            csv_string += '{:f},{:f},{:f},{:f},{:f},{:f}\n'.format(self.gdata[i][0], self.gdata[i][1], self.gdata[i][2], self.adata[i][0], self.adata[i][1], self.adata[i][2])
        return csv_string


    # Initialize CRC table
    def crc_table_init(self):
        # Initialize crc_table
        self.crc_table = list(range(256))
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

    # Calculate CRC value
    def update_crc(self, crc, c):
        int_c = 0x00ff & c
        if (self.crc_table is None):
            # Initialize table
            self.crc_table_init()
        tmp = crc ^ int_c
        crc = (crc >> 8) ^ self.crc_table[tmp & 0xff]
        return crc
    

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
    
    def version(self):
        ver = self.read('version')[0]
        return float(ver/100)


    ###################
    # Basic communication methods
    ###################
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

    def write(self, key, value):
        self.modbus_write(self.main_dictionary[key]['address'], value)

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

    ###################
    # Flash methods
    ###################
    def read_flash(self, address, nbytes):
        if (nbytes > 8192):
            print('Number of requested bytes exceeds limit of 8192')
            return None
        try:
            return self.modbus.read_flash(address, nbytes)
        except IOError as e:
            print(e)
            return None

    def erase_flash(self, pause=0.2):
        # Disable logging first
        self.log_enable(False)
        time.sleep(pause)
        # Send command to erase
        self.modbus.custom_command(0xABCD, 0x0000)
        time.sleep(pause)
        # Wait until status is no longer 3 and/or KeyboardInterrupt is triggered
        try:
            status = self.read('flash_status')[0]
            while status == 3:
                print('\t...waiting for erase to finish (Status: {})'.format(status))
                time.sleep(pause)
                status = self.read('flash_status')[0]
            print('Erase complete (Status: {})'.format(status))
        except KeyboardInterrupt:
            pass

    def read_flash_record(self, page_number):
        adr = page_number*512
        nbytes = 508
        response = self.read_flash(adr, nbytes)
        # Remove modbus header and CRC
        response = response[4:-2]
        # Convert to byte array
        datab = bytes([ord(c) for c in response])
        # Check if CRC is valid
        _crccheck = 0xFFFF
        for b in datab:
            _crccheck = self.update_crc(_crccheck, b)
        if (_crccheck != 0):
            print('Data record is corrupted! (CRC: {})'.format(_crccheck))
            return None
        else:
            print(len(datab))
            return Record(datab)

    def _read_flash_records(self, page_start, npages):
        if npages < 1:
            raise AttributeError('Number of pages cannot be less than 0')
        if npages > 16:
            raise AttributeError('Number of pages cannot exceed 16 (8192 bytes)')
        page_size = 512
        adr = page_start*page_size
        nbytes = npages*page_size
        response = self.read_flash(adr, nbytes)
        response = response[4:-2]
        # Convert to byte array
        datab = bytes([ord(c) for c in response])
        # Split response into pages
        pages = []
        for i in range(npages):
            start = i*page_size
            end = start+508
            pages.append(Record(datab[start:end]))
        return pages

    def read_flash_records(self, page_start, npages):
        pages = []
        count = 0
        while count < npages:
            read_pages = ((npages - count) % 5) + 1
            print('\t\t...reading pages {}-{}'.format(page_start+count, page_start+count+read_pages-1))
            pages.extend(self._read_flash_records(page_start+count, read_pages)) 
            count += read_pages
        # Return list of records            
        return pages


    ###################
    # Other wrapper methods
    ###################
    def serialize(self, records):
        databytes = b''
        for r in records:
            databytes += r.databytes
        return databytes

    def log_enable(self, enable):
        key = 'setup_flags'
        if enable:
            self.write(key, 1)
        else:
            self.write(key, 0)
        
    def disk_usage(self):
        p = self.read('disk_pointer')[0]
        m = self.read('disk_space_max')[0]
        print('{: 3.3f}%    ({} B, {} B)'.format(p/m*100, p, m))

    def disk_page(self):
        p = int(self.read('disk_pointer')[0]/512)
        m = int(self.read('disk_space_max')[0]/512)
        print('Page {:d} out of {:d}'.format(p, m))
        return p

    def loop(self, key, pause=0.2):
        try:
            while True:
                print(self.read(key))
                time.sleep(pause)
        except KeyboardInterrupt:
            pass

    def time_now(self, use_utc_zone=False, format_24h=False):
        # Detect zones
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()
        # Build UTC time
        unixtime = self.read('unix_time')[0]
        utc = datetime.utcfromtimestamp(unixtime)
        utc = utc.replace(tzinfo=from_zone)
        # Convert to local time zone
        local = utc.astimezone(to_zone)
        if (use_utc_zone):
            outzone = utc
        else:
            outzone = local
        if (format_24h):
            print(outzone.strftime('%Y-%m-%d %H:%M:%S'))
        else:
            print(outzone.strftime('%Y-%m-%d %I:%M:%S %p'))

    def time_sync(self):
        # Get current unix time
        unixtime = time.time()
        # Send sync command
        self.modbus.synchronize(unixtime)

        

    ###################
    # Backend methods
    ###################
    # modbus for reading the number of bytes you want
    # 2 addresses are 4 bytes which is 2 registers
    def modbus_read(self, address, n_bytes): 
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
    #takes a value to write
    def modbus_write_val(self, address, value, serialization): 
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
            # print('Writing {:2X} to {:2X}'.format(byteToWrite, address))
            self.modbus.write_register(address, byteToWrite)
            success = True
        except IOError as e:
            print('IOError occurred while writing...\n{}'.format(e))
        except ValueError as e:
            print('ValueError occurred while writing...\n{}'.format(e))
        return success

    # Initialize CRC table
    def crc_table_init(self):
        # Initialize crc_table
        self.crc_table = list(range(256))
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

    # Calculate CRC value
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
