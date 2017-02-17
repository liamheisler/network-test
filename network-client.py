'''
test-based client
'''

import socket

host = '127.0.1.1'
port = 5560

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = input("Enter your command: ")
    if command == 'exit':
        #send exit command
        s.send(str.encode(command))
    elif command == 'kill':
        #send kill command
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply = s.recv(1024)
    print(reploy.decode('utf-8'))

s.close()
