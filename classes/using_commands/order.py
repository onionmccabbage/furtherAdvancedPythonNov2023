from abc import ABCMeta, abstractmethod

class Order(metaclass=ABCMeta):
    '''we write the architecture without any implementations'''
    @abstractmethod
    def execute(self):
        pass

