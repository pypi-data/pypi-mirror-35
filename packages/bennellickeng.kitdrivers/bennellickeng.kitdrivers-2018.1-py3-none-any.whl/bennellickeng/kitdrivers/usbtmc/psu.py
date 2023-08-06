from __future__ import print_function
from .usbtmc import Usbtmc
import time


class Psu(object):
    def __init__(self, device_file):
        self.device = Usbtmc(device_file)
        self.name = self.device.get_name()

        print(self.name)

    def output_on(self, output_number):
        self.device.write_str(":OUTP CH{0},ON".format(output_number))

    def output_off(self, output_number):
        self.device.write_str(":OUTP CH{0},OFF".format(output_number))

    def reset(self):
        """Reset the instrument"""
        self.device.send_reset()
