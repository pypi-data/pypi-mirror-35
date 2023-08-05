__all__ = ['HmiHandler']

import threading
import serial
import time
from .data_to_byte import *
from .decoder import *
from .util import *

class HmiHandler(threading.Thread):
    _ser = serial.Serial()
    _dataBuffer = list()
    _timeout = int()

    def __init__(
        self,
        port=None,
        baudrate=38400,
        timeout=None
    ):
        super(HmiHandler, self).__init__(name = 'hmi')
        self._ser.port = port
        self._ser.baudrate = baudrate
        self._ser.timeout = 0.01
        self._timeout = timeout
        self.lock = threading.Lock()

    def setSerial(
        port,
        baudrate=38400,
    ):
        self._ser.port = port
        self._ser.baudrate = baudrate

    def run(self):
        de = Decoder()
        self._dataBuffer = list()
        self._ser.open()

        while (self._ser.isOpen()):
            try:
                self.lock.acquire()
                ch = self._ser.read(1)
                self.lock.release()
            except serial.serialutil.SerialException as e:
                raise AsaHmiException()
            else:
                if ch != b'':
                    self.lock.acquire()
                    de.add_text(ch)
                    type, data = de.get()
                    if type is 0:
                        pass
                    else:
                        self._dataBuffer.append((type, data))
                    self.lock.release()

    def putArray(self, data):
        b = encodeArToPac(data)
        self._ser.write(b)

    def putStruct(self, data):
        b = encodeStToPac(data)
        self._ser.write(b)

    def putString(self, data):
        b = data.encode('utf-8')
        self._ser.write(b)

    def putSync(self):
        self._ser.write(b'sync\n')

    def get(self):
        if not self._ser.is_open:
            raise SerialNotOpenException
        if self._timeout is not None and self._timeout != 0:
            timeout = time.time() + self._timeout
        else:
            timeout = None
        data = None
        while self._ser.is_open:
            if len(self._dataBuffer) >= 1:
                data = self._dataBuffer.pop(0)
                break
            # check for timeout now, after data has been read.
            # useful for timeout = 0 (non blocking) read
            if timeout and time.time() > timeout:
                break
        return data

    def getArray(self):
        if not self._ser.is_open:
            raise SerialNotOpenException
        if self._timeout is not None and self._timeout != 0:
            timeout = time.time() + self._timeout
        else:
            timeout = None
        data = None
        while self._ser.is_open:
            if len(self._dataBuffer) >= 1:
                if self._dataBuffer[0][0] == 1:
                    data = self._dataBuffer.pop(0)
                    break
                else:
                    break
            # check for timeout now, after data has been read.
            # useful for timeout = 0 (non blocking) read
            if timeout and time.time() > timeout:
                break
        return data

    def getStruct(self):
        if not self._ser.is_open:
            raise SerialNotOpenException
        if self._timeout is not None and self._timeout != 0:
            timeout = time.time() + self._timeout
        else:
            timeout = None
        data = None
        while self._ser.is_open:
            if len(self._dataBuffer) >= 1:
                if self._dataBuffer[0][0] == 2:
                    data = self._dataBuffer.pop(0)
                    break
                else:
                    break
            # check for timeout now, after data has been read.
            # useful for timeout = 0 (non blocking) read
            if timeout and time.time() > timeout:
                break
        return data

    def getString(self):
        if not self._ser.is_open:
            raise SerialNotOpenException
        if self._timeout is not None and self._timeout != 0:
            timeout = time.time() + self._timeout
        else:
            timeout = None
        data = None
        while self._ser.is_open:
            if len(self._dataBuffer) >= 1:
                if len(self._dataBuffer) >= 1:
                    if self._dataBuffer[0][0] == 3:
                        data = self._dataBuffer.pop(0)
                        break
                    else:
                        break
            # check for timeout now, after data has been read.
            # useful for timeout = 0 (non blocking) read
            if timeout and time.time() > timeout:
                break
        return data

    def getAvailableDataNum(self):
        return len(self._dataBuffer)
