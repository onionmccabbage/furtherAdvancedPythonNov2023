# a daemon thread will continue running until the main thread terminates
from threading import Thread
import time

def standardThread():
    print('starting a standard thread')
    time.sleep(5)
    print('ending standard thread')

def daemonThread():
    print('starting a daemon thread')
    while True:
        print('heartbeat')
        time.sleep(0.5)

if __name__ == '__main__':
    s = Thread(target=standardThread)
    d = Thread(target=daemonThread, daemon=True)
    # s.setDaemon(True) # we can make any thread daemon thread
    s.start()
    d.start()
    s.join()
    # by NOT using join on a Daemon we can end it when the main thread ends
    # d.join() # the Daemon will run endlessly so no expectation to rejoin