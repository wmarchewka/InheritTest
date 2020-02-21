from logger import Logger
from config import Config
from gpio import Gpio
from spi import SPI

class Rotary(Config, Logger, Gpio):
    def __init__(self):
        super().__init__()