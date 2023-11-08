# we can write a decorator to bew applied to ANY function to make it thread safe
# in this case thread safe means use a lock

from threading import Lock # or RLock or Semaphore

lock = Lock()

def lock_a_method(meth):
    '''This method can be used as a decorator to apply a lock to any method or function'''
    def locked_method(self, *args, **kwargs):
        try:
            # lock.acquire()
            # result = meth(self, args, kwargs)
            # lock.release()
            # return result
            with lock: # no need to release - 'with' will releas the lock when done
                return meth(self, args, kwargs)
        except Exception as e:
            print(e)
    lock_a_method.__name__ = f'Locked_method_{meth.__name__}'
    locked_method.__is_locked = True # a marker to indicate our method is locked
    return locked_method

class MySet(set):
    '''This class inherits from 'set'. Remember 'set' has add and remove 
    We may need to make methods of our class thread safe (lock)'''
    def __init__(self, new_set):
        set.__init__(self, new_set)
    @lock_a_method # applyy our decorator (which will usse a lock in the following function)
    def someMethod(self, new_value):
        '''check the new_value is an int'''
        if type(new_value)==int:
            self.add(new_value)
        else:
            pass

def main():
    ms = MySet({3,2,6,6,6,3,8,2,6,True, 'this my set', True})

    print(ms.someMethod.__is_locked) # True



if __name__ == '__main__':
    s = {3,2,6,6,6,3,8,2,6,True, 'this is a set', True}
    s.add(12)
    print(s) # only unique values
    main()