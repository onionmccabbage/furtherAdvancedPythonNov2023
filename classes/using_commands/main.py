from stock_trade import StockTrade
from agent import Agent
from buy_stock import BuyStock
from sell_stock import SellStock

def main(): # main is a convention for the main module and main method
    '''call the other classes and issue commands (may be async)'''
    stock = StockTrade()
    buy   = BuyStock(stock)
    sell  = SellStock(stock)
    agent = Agent()
    # invoke commands
    agent.place_order(buy)
    agent.place_order(sell)

if __name__ == '__main__':
    main()