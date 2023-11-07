from threading import Thread
import random
import time

def myFn(n):
    '''this is a normal function. Like all functinos it can be inmvoked on a thread'''
    for _ in range(0,10):
        print(f'{n} is sleeping')
        # emulate a long-running series of code steps
        time.sleep(random.random()*0.1) # sleep for up to 0.1 of a sec

def main():
    '''invoke the function on theads'''
    start = time.time()
    # myFn(1) # this will run on the main thread
    # myFn(2)
    # myFn(3)
    # myFn(4)
    # myFn(5)
    t1 = Thread(target=myFn, args=(1,), kwargs={}) # be careful - a one member tuple needs a trailing comma
    t2 = Thread(target=myFn, args=(2,))
    t3 = Thread(target=myFn, args=(3,)) 
    t4 = Thread(target=myFn, args=(4,)) 
    t5 = Thread(target=myFn, args=(5,)) 
    # we need to start the threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    # the main thread wil just carry on unless we...
    t1.join() # always a good idea
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    # now the main thread will pause until the others have (re)joined
    end = time.time()
    print(f'total time {end-start} seconds') # about 2.5 sec

if __name__ == '__main__':
    main()
