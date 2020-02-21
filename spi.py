print(__name__)
from config import Config
from logger import Logger

class Spi(Config,Logger):
    print(__name__)
    def __init__(self):
        super().__init__()

