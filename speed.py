from logger import Logger
from config import Config
from spi import Spi
from rotary import Rotary

class Speed(Rotary, Spi):
    print(__name__)
    def __init__(self):
        print(Speed.__mro__)
        super().__init__()
