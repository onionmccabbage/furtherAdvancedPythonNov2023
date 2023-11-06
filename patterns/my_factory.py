# The factory pattern lets us manufacture required entities
class Animal(): # could be abstract
    '''All our creatures will inherit from this class'''
    def make_a_noise(self):
        pass

# here are some concrete creatures (better that they exist in separate modules)
class Dog(Animal):
    def make_a_noise(self):
        return 'woof'
class Cat(Animal):
    def make_a_noise(self):
        return 'miaow'
class Lion(Animal):
    def make_a_noise(self):
        return 'roar'
class Bat(Animal):
    def make_a_noise(self):
        return '____'

# here is a creature factory
class CreatureFactory():
    '''This is a single point of access for all our creatures'''
    def make_sound(self, obj):
        '''we evaluate the object then invoke the class'''
        return eval(obj)().make_a_noise()
    
if __name__ == '__main__':
    cf = CreatureFactory()
    creature = input('Which creature? ') # careful - we should validate!
    noise = cf.make_sound(creature)
    print(f'The {creature} says {noise}')