# in Python everything is an object
# only use a class when nothing else will do
a = 1
b = 3.4
c = True
s = 'hello' # immutable collection of characters
print(s[0:5:2]) # slicing [start:stop-before:step]
l = [] # mutable indexed collection
t = (l,) # immutable indexed collection
d = {} # non-indexed collection of key:value pairs

class Point(): # implicitly or explicitly inherit from object
    '''A point in 2-d space'''
    __slots__ = ('__x','__y') # we can restrict the permitted properties
    def __init__(self, x, y):
        self.x = x # this calls the x setter method
        self.y = y 
    # for validation we use get/set methods
    @property
    def x(self): # getter method (accessor)
        # __x is NOT accessible outside this class (like private)
        return self.__x # name-mangling
    @x.setter
    def x(self, x:int)->None: # setter (mutator)
        '''using static types is ONLY for linting and code hints
        i.e. static types are only interesting at DESIGN time not RUN time'''
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
    def __str__(self): # print always uses __str__ so we can overwrite it
        '''this is the method by which this class can be printed'''
        # return 'Point is at x:{} y:{}'.format(self.x, self.y)
        return f'Point is at x:{self.x} y:{self.y}'

# immediate code
print(__name__)

if __name__ == '__main__':
    p1 = Point(33.33, -99.432)
    p1.x = 3333
    # try to access __x
    # p1.__x = 'oops' # we can attach any arbitrary property to an object
    # print( p1.__x )
    print(Point.__dict__)
    # we CAN access the mangled members
    p1._Point__x = 'changed'
    print(p1)