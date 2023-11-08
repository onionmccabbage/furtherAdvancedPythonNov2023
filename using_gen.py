# a generator is efficient memory snce it never persists all values in memory
def demo():
    for _ in range(32):
        print(_) # we never persist all these values...

# we can build our own custom generator
def tally(incr=1, max=False):
    '''keep an endless tally'''
    score = 0
    while True:
        yield score # by using yield we have a generator
        score += incr
        if max  and score > max:
            raise StopIteration # this is the correct way to end  generator

def main():
    # Python can create a generator for us
    even_g = (i for i in range(100) if i%2==0) # not a tuple
    # careful - this list ALL exists in memory
    # even_l = [i for i in range(100) if i%2==0]
    print(type(even_g))
    print(even_g.__next__()) # 0
    print(even_g.__next__()) # 2
    print(next(even_g)) # 4
    # we can use our endless tally
    game=tally(5) # override the score increment
    try:
        print(type(game)) # a generator
        print(game.__next__()) # 0
        print(game.__next__()) # 5
        print(next(game)) # 10
        # we can close any generator like this
        game.close() # this will cause any further calls to raise stop iteration
        print(game.__next__()) # nope
    except StopIteration as si:
        pass



if __name__ == '__main__':
    main()