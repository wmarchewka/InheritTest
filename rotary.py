from logger import Logger
# from config import Config
from gpio import Gpio
#from spi import Spi

class Rotary(Gpio):
    print(__name__)
    def __init__(self):
        super().__init__()
        self.log = Logger.log
