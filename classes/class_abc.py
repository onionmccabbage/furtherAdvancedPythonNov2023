from abc import abstractmethod
from abc import ABCMeta

# we can declare abstract classes
class Planar(metaclass=ABCMeta):
    '''An abstract class for planaer spacial points'''
    def __init__(self):
        pass
    @abstractmethod
    def hypot(self):
        pass

# in Abstract Base Classes (ABC) we declare the struture with NO implementation
