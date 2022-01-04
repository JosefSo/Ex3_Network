# import socket module
# 337959928, 209128966
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
# Fill in start

serverSocket.bind(('', PORT))
serverSocket.listen(1)
print ('the web server is up on port:', PORT)

# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() # Fill in start              #Fill in end
    try:
        message = connectionSocket.recv(1024) # Fill in start          #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()  # Fill in start       #Fill in end
        print(outputdata)
        # Send one HTTP header line into socket
        # Fill in start

        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())

        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
# Send response message for file not found
# Fill in start
        connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
        print("HTTP/1.1 404 Not Found\n")
# Fill in end

# Close client socket
# Fill in start
        connectionSocket.close()
# Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data
