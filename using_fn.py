# functional programming uses functions rather than classes

def isEven(n):
    '''True if even, False if not'''
    return n%2 == 0

def addThem(m, n):
    return m+n

def main():
    '''Python has map and filter asd functional features'''
    # map objects do NOT maintain all the values in memory, they yield on demand
    results = map(isEven, range(-10, 11))
    print(results) # we have a map object - we can iterate over it
    print(results.__next__() ) # True (yields the next value from the map object)
    print(results.__next__() ) # False
    print(results.__next__() ) # True
    for _ in results: # this will pick up where we left off (-7 in this case)
        print(f'Even: {_}')
    # filter...
    matching = filter(isEven, range(-10, 11))
    print(matching.__next__()) # -10
    print(matching.__next__()) # -8
    print(matching.__next__()) # -6
    # for _ in matching:
    #     print(_, end=', ')
    # we have exhausted the map and filter objects
    # print(results.__next__()) # nope
    while True: # be careful!!
        try:
            print(matching.__next__())
        except StopIteration as s: # common to handle stop iteration like this
            pass
            break
        finally:
            pass


if __name__ == '__main__':
    main()