# may need to pip install memory_profiler (or conda install...)
from memory_profiler import profile
import collections # a bunch of additonal data structures

@profile # invoke the memory profiler
def myFn(n):
    '''manage a double ended queue'''
    my_deq = collections.deque('98765432')
    print(my_deq)
    # we can deliberately consume a lot of memory
    for i in range(0, n):
        my_deq.append(i)
        my_deq.appendleft(i)
    return my_deq

if __name__ == '__main__':
    # de = collections.deque('tenet')
    # de.append('s')
    # de.appendleft('s')
    # print(type(de), de)
    # de.pop()
    # de.popleft()
    n = int(float( input('how many?') )) # all inputs are string
    r = myFn(n)
    # print(r)