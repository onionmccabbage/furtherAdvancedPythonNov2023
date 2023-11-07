from _off import Off

class Laptop:
    def __init__(self):
        self.state=Off() # an instance of a computer state
    def change(self, change_to):
        self.state.switch(change_to)
