from threading import Thread, Event
import time

# we can use events to communicate from threads
event = Event()

class MyClass:
    def __call__(self, n):
        global event
        print(f'{n} waiting for event...')
        event.wait() # pause until the thread event happens
        print(f'{n} continuing after event')

if __name__ == '__main__':
    m1 = MyClass()
    m2 = MyClass()
    t1 = Thread(target=m1, args=('A',))
    t2 = Thread(target=m2, args=('B',))
    t1.start()
    t2.start()
    # wait on the main thread
    time.sleep(4)
    event.set()# trigger the event to happen

    t1.join()
    t2.join()
