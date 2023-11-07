# semaphores let us specify the maximum number of concurrent threads that can access a resource
from collections.abc import Callable, Iterable, Mapping
import random
import time
import threading
from typing import Any

# a global asset
ticketsAvailable = 100

class TicketSeller(threading.Thread):
    '''use a semaphore to access the tickets'''
    ticketsSold = 0
    def __init__(self, sem): # pass in the semaphore object
        threading.Thread.__init__(self) # or super().__init__() note - no SELF
        self.__sem = sem
    def run(self):
        global ticketsAvailable
        running = True
        while running: # this is a run loop
            self.__sem.acquire()
            self.randomDelay()
            if ticketsAvailable <=0:
                running = False
            else:
                self.ticketsSold +=1
                ticketsAvailable -=1
            self.__sem.release()
        print(f'Ticket seller {self.getName()} sold {self.ticketsSold} tickets')
    def randomDelay(self):
        time.sleep(random.randint(0,4)/16) # 0, 0.25, 0.5, 0.75...

def main():
    '''provide a semaphore permitting several concurrent ticket sellers'''
    sem = threading.Semaphore(8)  # we can choose how many concurrent
    sellers = []
    for i in range(0,4):
        seller = TicketSeller(sem) # pass the semaphore to the class instance
        sellers.append(seller)
        seller.start()
    # once all the threads have started we should join them
    for s in sellers:
        s.join()


if __name__ == '__main__':
    main()