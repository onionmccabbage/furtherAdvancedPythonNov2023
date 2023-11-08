import multiprocessing
import os
# to measure performance we cantime stuff
import time
import timeit # a more accurate timer, it tries to ignire non-Python stuff

def whichProc():
    '''declare which process ID this is running on'''
    print(f'Running on process ID {os.getpid()}')

if __name__ == '__main__':
    print(f'This device has {os.cpu_count()} processors')
    procs_l = []
    # it is sensible to limit proceses to the number of processors
    start_a = time.time()
    start_b = timeit.default_timer()
    # each process must start a new copy of Python - so only use whewn there is a LOT of work to handle
    for n in range(0, os.cpu_count()-1):
        p = multiprocessing.Process(target=whichProc)
        procs_l.append(p)
        p.start()
    for _ in procs_l:
        _.join()
    # what about the main thread?
    whichProc()
    time_b = (timeit.default_timer())-start_b
    time_a = (time.time())-start_a
    # we can format to decimal places
    print(f'The module took {time_a:0.2f} {time_b}')