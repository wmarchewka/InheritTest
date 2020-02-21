from rotary import Rotary
#from config import Config
from spi import Spi
from decoder import Decoder

class Gain(Rotary, Spi, Decoder):
    print(__name__)
    def __init__(self):
        super().__init__()
