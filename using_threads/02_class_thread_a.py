from threading import Thread
import random
import time

class MyClass:
    '''overriding __call__ makes this class callable (e.g. by a thread)'''
    def __call__(self, n):
        for _ in range(0,10):
            print(f'{n} is sleeping')
            time.sleep(random.random()*0.1)

def main():
    '''invoke our class as threads'''
    c1 = MyClass()
    thread_l = []
    # the O/S is responsible for managing a pool of threads
    for i in range(512): # more than this (on my laptop) slows down significantly
        thread_l.append( Thread(target=c1, args=(i,)) )
    for thread in thread_l:
        thread.start() # we must start thjem all before we join them all
    for thread in thread_l:
        thread.join()

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Total time {end-start} seconds')