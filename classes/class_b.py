# a 3-d point
from class_a import Point

class Point3(Point):
    '''a point in 3-d space'''
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z # call setter
    @property
    def z(self):
        return self.__z
    @z.setter
    def z(self, z):
        if type(z) in (int, float):
            self.__z
        else:
            raise TypeError

print(__name__)       

if __name__ == '__main__':
    pass
