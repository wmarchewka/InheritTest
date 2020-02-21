from config import Config
from rotary import Rotary
from spi import Spi
from decoder import Decoder
#from gpio import Gpio

class Speed(Rotary, Spi, Decoder):
    print(__name__)
    def __init__(self):
        super().__init__()
        self.config = Config
        self.rotary = Rotary
