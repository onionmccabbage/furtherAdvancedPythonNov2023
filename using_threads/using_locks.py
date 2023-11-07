import threading

# here is a global asset
counter = 0 # could be a file i/o, a DB, an API ....
lock = threading.Lock()

def workerA():
    '''This function will increment the counter'''
    global counter
    lock.acquire() # get unique access to the lock
    try:
        while counter <20:
            counter += 1
            print(f'Worker A increments counter to {counter}')
    except Exception as e:
        print(f'Something went wrong: {e}')
    finally:
        lock.release() # now other threads can use the lock instance

def workerB():
    '''This function will decrement the counter'''
    global counter
    lock.acquire() # get unique access to the lock
    try:
        while counter >-20:
            counter -= 1
            print(f'Worker B decrements counter to {counter}')
    except Exception as e:
        print(f'Something went wrong: {e}')
    finally:
        lock.release() # now other threads can use the lock instance

def main():
    t1 = threading.Thread(target=workerA)
    t2 = threading.Thread(target=workerB)
    t2.start()
    t1.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()