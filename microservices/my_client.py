import sys # we will read the system argument variables
import socket

def myClient(): # could be a class
    '''This simple client will make a request'''
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    setup_t = ('localhost', 9876) # IP and port (127.0.0.1)
    cli.connect(setup_t)
    if len(sys.argv) > 1: # we ignore member zero (the file name)
        msg = ', '.join(sys.argv[1:]) # exclude the first member
    else:
        msg = 'default'
    cli.send(msg.encode())
    response = cli.recv(1024)
    # we might choose to decode the response
    print(f'Client received {response}')
    cli.close() # all done for this client
    

if __name__ == '__main__':
    print(sys.argv)
    myClient()