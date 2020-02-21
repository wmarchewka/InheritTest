# from logger import Logger
# from config import Config
# # from spi import Spi
# # from rotary import Rotary
# # from decoder import Decoder
from gpio import Gpio

class Codegen(Gpio):
    print(__name__)
    def __init__(self):
        super().__init__()
        self.log = Logger.log