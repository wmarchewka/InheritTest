from logger import Logger

class Config(Logger):
    print(__name__)
    def __init__(self):
        super().__init__()
        self.log = Logger.log
        self.log.debug("In {}".format(__name__))
