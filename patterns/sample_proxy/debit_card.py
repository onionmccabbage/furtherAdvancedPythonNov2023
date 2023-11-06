from payment import Payment
from bank import Bank

class DebitCard(Payment):
    '''This debit card is a proxy for the bank'''
    def __init__(self):
        self.bank = Bank()
    def doPay(self):
        card = input('Swipe, tap, insert or what?')
        self.bank.setCard(card)
        # we should be doing loads of validation
        return self.bank.doPay() # True or False