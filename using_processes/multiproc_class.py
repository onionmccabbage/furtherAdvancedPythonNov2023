from collections.abc import Callable, Iterable, Mapping
import multiprocessing
import os
import time
from typing import Any

class MyProc(multiprocessing.Process):
    '''inherit from the Process class'''
    def __init__(self):
        super(MyProc, self).__init__()
    def run(self):
        '''overide the built in run method'''
        print(f'Child process ID is {os.getpid()} aka {multiprocessing.current_process()}') # .pid

def main():
    '''start a few processes'''
    procs_l = []
    for p in range(0, os.cpu_count()-1):
        proc = MyProc()
        procs_l.append(proc)
        proc.start()
    for _ in procs_l:
        _.join() # this is optional

if __name__ == '__main__':
    main()
    print(f'Main process id is {os.getpid()}')