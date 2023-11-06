# in Python everything is an object


class Point(): # implicitly or explicitly inherit from object
    '''A point in 2-d space'''
    def __init__(self, x, y):
        self.x = x # this calls the x setter method
        self.y = y 
    # for validation we use get/set methods
    @property
    def x(self): # getter method (accessor)
        return self.__x # name-mangling
    @x.setter
    def x(self, x): # setter (mutator)
        if type(x) in (int, float): # if type(x) == int or type(x) == float:
            self.__x = x
        else:
            raise TypeError
    @property
    def y(self): # getter method (accessor)
        return self.__y # name-mangling
    @y.setter
    def y(self, y): # setter (mutator)
        if type(y) in (int, float):
            self.__y = y
        else:
            raise TypeError


if __name__ == '__main__':
    p1 = Point(3.456, -99.432)
    p1.x = 3333