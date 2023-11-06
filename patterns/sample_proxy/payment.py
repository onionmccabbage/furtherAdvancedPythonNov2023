from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def doPay(self):
        pass  # never implement in the abstract