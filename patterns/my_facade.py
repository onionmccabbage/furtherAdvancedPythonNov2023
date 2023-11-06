# a facade brings together disparate entities via a single facade
# remember these classes should be in separate modules
class Coder():
    '''creates code to solve problems'''
    def __init__(self):
        print('write sme code')
    def __is_available(self): # this is mangled (__)  so it is only visible within instances
        '''we could check if the coder resource is available'''
        print('coding skills are available')
        return True # or False
    def book_time(self):
        if self.__is_available():
            print('coder has been booked')

class Tester():
    '''tests code to ensure diligence'''
    def __init__(self):
        print('preparing some test')
    def testing(self):
        print('test are in place')

class Technician():
    def __init__(self):
        print('preparing equipment for the team')
    def doStuff(self):
        print('network, machines, cloud all in place')

class Artisan():
    '''design stuff'''
    def __init__(self):
        print('designing things')
    def make_prototype(self):
        print('wireframes are ready')

class Manager():
    '''This is a facade to the other classes'''
    def __init__(self):
        print('Manager says I can arrange the team')
    def arrange(self):
        '''The facade will provide instances of all the other subsystems/microservices etc.'''
        self.coder      = Coder()
        self.tester     = Tester()
        self.technician = Technician()
        self.artsan     = Artisan()
        # we could easily add additional assets here
        # put the assets to work
        self.coder.book_time() # if not available we should handle ...
        self.tester.testing()
        self.technician.doStuff()
        self.artsan.make_prototype()

class Client():
    '''Client needs resources to solve a problem'''
    def __init__(self):
        print('We need a team for our project')
    def askManager(self):
        print('lets talk to the manager')
        self.manager = Manager() # we now have access to our facade
        self.manager.arrange()
    def __del__(self): # every class will run __del__ whn done
        print('All done')

if __name__ == '__main__':
    '''a facade can make ugly stuff easier to look at'''
    customer = Client()
    customer.askManager()
