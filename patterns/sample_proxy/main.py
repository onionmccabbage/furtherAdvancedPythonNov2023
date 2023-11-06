# this facade provides access to other elements

from bank import Bank
from customer import Customer
def main():
    customer = Customer()
    customer.makePayment()

if __name__ == '__main__':
    main()