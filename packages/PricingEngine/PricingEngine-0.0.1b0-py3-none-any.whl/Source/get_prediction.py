from Source.interface import AlgorithmInterface
from Logger.log_helper import LogHelper as lhelper
from Source.AlgorithmManager import AlgorithmManager


# interface implement
class get_prediction((AlgorithmInterface.AlgorithmInterface)):
    try:
        def __init__(self, data):
            self.data = data
            super(get_prediction, self).__init__()

        def algo(self):
            AlgorithmManager(self.data)
        # implements methods of base class


    except Exception as err:
        lhelper.getlogger().error(err)
