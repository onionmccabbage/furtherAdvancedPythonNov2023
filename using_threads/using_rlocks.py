# rlock is a re-entrant lock
# if we need to acquire and release a lock frequently, use a rlock
import threading
import time

class MyWorker():
    '''Modify data using re-entant lock'''
    def __init__(self):
        self.a = 1
        self.b = 2
        self.rlock = threading.RLock() # could be a global asset
    def modifyA(self):
        with self.rlock: # when the 'with' operator completes, it wil lrelease any resources
            print(f'RLock acquired {self.rlock._is_owned()} to modify A')
            self.a += 1
            time.sleep(1)
    def modifyB(self):
        with self.rlock: # when the 'with' operator completes, it wil lrelease any resources
            print(f'RLock acquired {self.rlock._is_owned()} to modify B')
            self.b -= 1
            time.sleep(1)
        # no need to release the RLock - it will be relased when the 'with' ends 
    def modifyBoth(self):
        self.modifyA()
        self.modifyB()

def main():
    w = MyWorker() # this is not a thread
    w.modifyA()
    w.modifyB()
    w.modifyBoth()

if __name__ == '__main__':
    main()