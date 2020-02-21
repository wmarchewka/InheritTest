from logger import Logger
from config import Config

class Gpio(Config, Logger):
    def __init__(self):
        super().__init__()
