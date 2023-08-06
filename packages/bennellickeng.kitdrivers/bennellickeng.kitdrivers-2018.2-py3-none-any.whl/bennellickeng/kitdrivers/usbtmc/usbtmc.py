import os
import time
from fcntl import ioctl


class Usbtmc(object):
    _USBTMC_IOC_NR = 91 # From include/uapi/linux/usb/tmc.h

    def __init__(self, device):
        self.device = device
        self.FILE = os.open(device, os.O_RDWR)

        # TODO: Test that the file opened

    def close(self):
        os.close(self.FILE)

    def write(self, command):
        os.write(self.FILE, command)
        # Reads straight after a write end up throwing a 'Connection Timed Out' exception without this delay :(
        time.sleep(0.001)

    def write_str(self, command):
        self.write(command.encode())

    def read(self, length=4000):
        try:
            return os.read(self.FILE, length)
        except TimeoutError as e:
            self.clear()
            raise e

    def read_str(self, length=4000):
        return self.read(length).decode()

    def get_name(self):
        self.write_str("*IDN?")
        return self.read_str(300)

    def send_reset(self):
        self.write_str("*RST")

    def _ioctl(self, nr):
        ioctl(self.FILE, (self._USBTMC_IOC_NR << 8) | nr)

    def clear(self):
        """Perform an 'initial clear' request"""
        self._ioctl(2)

    def indicate(self):
        self._ioctl(1)
