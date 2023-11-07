from threading import Thread
import random
import time

class MyClass(Thread):
    '''This class inherists from Thread'''
    def __init__(self, n):
        Thread.__init__(self) # we must use this (no optional arguments permitted)
        # super().__init__(self) # calling super always passes a bunch of optional arguments
        self.n = n # we should validate and mangle
    def run(self): # in orderr ot be runnable we override the run method of Thread
        for _ in range(0,10):
            print(f'{self.n} is sleeping')
            time.sleep(random.random()*0.1)

def main():
    '''invoke our class as threads'''
    thread_l = []
    for _ in range(512):
        thread_l.append(MyClass(_)) # this is a Thread
    for thread in thread_l:
        thread.start()
    for thread in thread_l: # we must start all the threads before joining them
        thread.join()

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Total time {end-start} seconds')