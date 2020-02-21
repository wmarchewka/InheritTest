from logger import Logger
from config import Config

class Gpio(Config, Logger):
    print(__name__)

    def __init__(self):
        super().__init__()
