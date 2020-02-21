from speed import Speed
from gain import Gain
#from gui import Gui
from logger import Logger

class InheritanceTest1(Speed, Gain, Logger):
    def __init__(self):
        super().__init__()
