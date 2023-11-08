# the Fibonacci sequence is an interesting mathematical idea
# always aim for performant code
# NB take several readings for performance
# Python includes a profiler tool called cProfile
# use it like this:
# python -m cProfile -o prof_out fib.py
# this will generate a profile report
# we then use Python to read this report

# from memory_profiler import profile
# import timeit

def fib(n):
    '''here is a low performance fibonacci function'''
    if n<=1:
        return 1
    else:
        # iteratively call itself
        return ( fib(n-1)+fib(n-2) )
    
# @profile
def main():
    n=32 # about 1.6sec
    # n=38 # almost 30sec on my laptop
    fib_values_l = []
    # start = timeit.default_timer()
    for _ in range(2, n+1):
        r = fib(_)
        fib_values_l.append(r)
    # end = timeit.default_timer()
    # print(f'Process took {end-start} sec')
    print(fib_values_l)

if __name__ == '__main__':
    main()

