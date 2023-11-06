class Agent():
    '''The agent can issue commands (things to do)'''
    def __init__(self):
        self.__order_queue = [] # an empty list
    def place_order(self, order): # we could validate the 'order'
        self.__order_queue.append(order)
        # the queue might be asynchronous, with latency, so things might take time
        order.execute()
  
if __name__ == '__main__':
    pass