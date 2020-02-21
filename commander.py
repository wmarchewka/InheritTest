print(__name__)
from speed import Speed
from gain import Gain
from gui import Gui

class Commander(Speed, Gain, Gui):
    print(__name__)
    def __init__(self):
        super().__init__()


c = Commander()
# it prints the lookup order
print(Commander.__mro__)
print(Commander.mro())