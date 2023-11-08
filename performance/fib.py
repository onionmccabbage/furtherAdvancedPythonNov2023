# the Fibonacci sequence is an interesting mathematical idea
# always aim for performant code
# NB take several readings for performance
# Python includes a profiler tool called cProfile
# use it like this:
# python -m cProfile -o prof_out fib.py
# this will generate a profile report
# we then use Python to read this report

# from memory_profiler import profile
import timeit
from functools import reduce

def fib(n):
    '''here is a low performance fibonacci function'''
    if n<=1:
        return 1
    else:
        # iteratively call itself
        return ( fib(n-1)+fib(n-2) )
    
def fib2(n):
    '''a more performant solution'''
    sequence = (0,1)
    for _ in range(2, n+2): # remember we need to return the sum of the last TWO members
        '''repeatedly add the last two values of the sequence'''
        # NB here we have a one-member tuple (so remember the trailing comma)
        sequence += (reduce( lambda a,b: a+b, sequence[-2:] ),) # works for a tuple
    # we must return
    return sequence[-1] # the last member

def fib3(n): # on my laptop this is fastest
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

# @profile
def main():
    n=32 # about 1.6sec
    # n=38 # almost 30sec on my laptop
    fib_values_l = []
    start = timeit.default_timer()
    for _ in range(2, n+1):
        # r = fib(_)
        r = fib3(_)
        # r = fib3(_)
        fib_values_l.append(r)
    end = timeit.default_timer()
    print(f'Process took {end-start} sec')
    print(fib_values_l)

if __name__ == '__main__':
    main()

