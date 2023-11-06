from order import Order # we have access to our abstract base class
from stock_trade import StockTrade

class BuyStock(Order):
    def __init__(self, stock):
        self.stock = stock
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, new_stock):
        if type(new_stock) == StockTrade:
            self.__stock = new_stock
        else:
            raise TypeError('Missing required stock trade instance')
    def execute(self):
        return self.stock.buy()
    
if __name__ == '__main__':
    s = StockTrade()
    bs = BuyStock(s)
    bs.execute()