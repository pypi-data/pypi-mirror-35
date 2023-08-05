import abc

class AlgorithmInterface(abc.ABC):
    @abc.abstractmethod
    def algo(self):
        pass
