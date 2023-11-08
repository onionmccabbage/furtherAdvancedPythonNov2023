# we can write a decorator to bew applied to ANY function to make it thread safe
# in this case thread safe means use a lock

from threading import Lock # or RLock or Semaphore

lock = Lock()

def lock_a_method(meth):
    '''This method can be used as a decorator to apply a lock to any method or function'''
    def locked_method(self, *args, **kwargs): # resolve this not operating as expected
        try:
            lock.acquire()
            result = meth(*args, **kwargs)
            lock.release()
            return result
            # with lock: # no need to release - 'with' will releas the lock when done
            #     return meth(self, *args, **kwargs) # unpack any positional and keyword args
        except Exception as e:
            print(e)
    lock_a_method.__name__ = f'Locked_method_{meth.__name__}'
    locked_method.__is_locked = True # a marker to indicate our method is locked
    return locked_method

def make_thread_safe(cls, meth_l, lock): # NB Lock is a factory (it returns a lock)
    '''we can provide a list of methods of the class to be locked'''
    init = cls.__init__ # take a copy of the original __init__ method
    def new_init(self, *args, **kwargs):
        init(self, *args, **kwargs)
        self.__lock = lock # provide a lock factory
    cls.__init__ = new_init
    # iterate over the meth_l and lock each method fro mthe list
    for meth in meth_l:
        old_meth = getattr(cls, meth)
        new_meth = lock_a_method(old_meth)
        setattr(cls, meth, new_meth) # make sure our new (locked) method matches the old one
    return cls # our new version of the class, with specific methods locked

# to use as a decorator for a class...
def lock_a_class(meth_list, lock):
    return lambda cls: make_thread_safe(cls, meth_list, lock)

# here we apply our decorator, to lock the 'add' and the 'remove' methods of this class
@lock_a_class(['add', 'remove'], Lock)
class MySet(set):
    '''This class inherits from 'set'. Remember 'set' has add and remove 
    We may need to make methods of our class thread safe (lock)'''
    def __init__(self, new_set):
        set.__init__(self, new_set)
    @lock_a_method # apply our decorator (which will usse a lock in the following function)
    def someMethod(self, new_value):
        '''check the new_value is an int'''
        if type(new_value)==int:
            print('adding a member')
            self.add(new_value)
        else:
            pass

def main():
    ms = MySet({3,2,6,6,6,3,8,2,6,True, 'this my set', True})
    ms.someMethod(22)
    print(ms) # does it contain 22
    print(ms.someMethod.__is_locked) # True
    print(ms.add.__is_locked) # True
    print(ms.remove.__is_locked) # True



if __name__ == '__main__':
    s = {3,2,6,6,6,3,8,2,6,True, 'this is a set', True}
    s.add(12)
    print(s) # only unique values
    main()