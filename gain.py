from logger import Logger
from config import Config
from spi import Spi

class Gain(Config, Logger, Spi):
    def __init__(self):
        super().__init__()
