'''
test-based server
'''

import socket

host = '127.0.1.1'
port = 5560

storedValue = "dummy data"

#set up the socket

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind complete.")
    return s

#set up the connection
def setupConnection():
    s.listen(1) #allow one connection at a time, one on one connection
    con, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1])) #dummy stat.
    return conn

def get():
    reply = storedValue
    return reply

#return the rest of the data message
def repeat(dataMessage):
    reply = dataMessage[1]
    return reply

#loop to send/receive data until told not to
def dataTransfer(conn):
    while True:
        #rec. the data
        data = conn.recv(1024) #recv the data, buffer fed in
        data = data.decode('utf-8') #decode the data to a string
        dataMessage = data.split(' ', 1) #split data by space one time
        #(cont) separated command from the rest of the data
        command = dataMessage[0]

        if command == 'get':
            reply = get()
        elif command == 'repeat':
            reply = repeat(dataMessage)
        elif command == 'exit':
            print("Client disconnected")
            break
        elif command == 'kill':
            print("Server shutting down")
            s.close()
            break
        else:
            reply = 'Unknown command!'

        #send reply back to the client
        conn.sendall(str.encode(reply))
        print("Data sent")
    conn.close()
    
s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        print("Transfer failed!")
        break


    


          
    
    
