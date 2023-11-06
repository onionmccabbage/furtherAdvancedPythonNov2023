# a decorator
def showArgs(f): # take a function as an argument
    '''This function can be used to decorate ANY other function
    It will reveal all positional and keyword arguments for that function'''
    def newFunc(*args, **kwargs):
        '''lock aspects of the function call to a text file'''
        try:
            # we use a file access object - a means to access file system assets (via the O/S)
            fout = open('log.txt', 'a') # append text (text is default)
            log_msg = ''
            log_msg += f'Running a function called {f.__name__}\n'  # 'dunder' means double underscore
            log_msg +=  f'The positional arguments are {args}\n'
            log_msg +=  f'The keyword arguments are {kwargs}'
            print( log_msg, file=fout ) # remember print always adds a new line
            fout.close() # tidy up when done
            # return f(*args, **kwargs) # call the original function
        # handle specific exception first
        except FileExistsError as fe:
            print(f'File already exists {fe}')
        # then handle more generic exceptino last
        except Exception as err:
            print( f'Something went wring {err}' )
    return newFunc # we do not call this function, just return it

# here are two simple functions
# @showArgs
def isOdd(n):
    '''return True if odd, False if not odd'''
    return n%2 !=0 # n%2 is modulo arithmetic

# @showArgs
def squares(m,n):
    '''return a list of the squares of every integer from m to n'''
    s = []
    for i in range(m, n): # top before n
        s.append(i*i)
    return s


if __name__ == '__main__':
    # for i in range(0, 55):
    #     print(isOdd(n=i), end=', ')
    # print( squares(-10, n=11) )
    # # can we apply 'decorators' without using @
    # showArgs( isOdd(3) ) # this call our decorator directly
    # # can we assign a decorator like this...
    isOdd = showArgs(isOdd)
    isOdd(9) # does this work??? Nope - no arguments wil lever be shown