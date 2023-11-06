# a decorator
def showArgs(f): # take a function as an argument
    '''This function can be used to decorate ANY other function
    It will reveal all positional and keyword arguments for that function'''
    def newFunc(*args, **kwargs):
        print( f'Running a function called {f.__name__}' ) # 'dunder' means double underscore
        print( f'The positional arguments are {args}' )
        print( f'The keyword arguments are {kwargs}' )
        return f(*args, **kwargs) # call the original function
    return newFunc # we do not call this function, just return it


# here are two simple functions
def isOdd(n):
    '''return True if odd, False if not odd'''
    return n%2 !=0 # n%2 is modulo arithmetic

@showArgs
def squares(m,n):
    '''return a list of the squares of every integer from m to n'''
    s = []
    for i in range(m, n): # top before n
        s.append(i*i)
    return s


if __name__ == '__main__':
    for i in range(0, 55):
        print(isOdd(n=i), end=', ')
    print( squares(-10, n=11) )