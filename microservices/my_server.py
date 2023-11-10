# Microservices is a design pattern
# break a system into parts, each solving a specific problem
# each service can iteract with any other service
# we often think of microservices as Applicatin Program Interfaces (API)

import socket

def myServer(): # could be a class
    '''This simple server will respond to client requests
       Echo back the request as upper-case'''
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    setup_t = ('localhost', 9876) # IP and port (127.0.0.1)
    server.bind(setup_t) #tell the serveer which IP and port
    server.listen() # begin listening for requests
    print(f'Server is listening on {setup_t[0]} {setup_t[1]}')
    while True: # this is a run loop
        (client, addr) = server.accept()
        buf = client.recv(1024) # read the first 1024 bytes
        buf_str = buf.decode()
        print(f'Server received {buf_str}')
        # if we receive 'quit' then the server will stop
        if buf == b'quit':
            client.send(b'You killed the server!!!')
            break # this will stop the run loop (and the server will stop)
        else:    
            response_str = buf_str.upper()
            client.send(response_str.encode())

if __name__ == '__main__':
    myServer()
