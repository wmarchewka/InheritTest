from logger import Logger
from config import Config
from gpio import Gpio
from spi import Spi

class Rotary(Config, Logger, Gpio, Spi):
    print(__name__)
    def __init__(self):
        super().__init__()