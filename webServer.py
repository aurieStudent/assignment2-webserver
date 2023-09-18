# import socket module
from socket import *
# In order to terminate the program
from signal import signal, SIGPIPE, SIG_DFL
#from io import BytesIO
signal(SIGPIPE,SIG_DFL)
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", port))

    # Fill in start
    serverSocket.listen(1)
    # Fill in end

    while True:
        # Establish the connection

        #print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()  ## Address is where are they coming from? Client socket is a socket object to send information to. #Fill in start -are you accepting connections?     #Fill in end
        #print("Connection established from: ")
        #print(addr)
        #connectionSocket.send('Welcome to the server!\r\n'.encode())
        #connectionSocket.send('charset=utf-8\r\n'.encode())
        #connectionSocket.send('Content-Type: text/html\r\n'.encode())

        try:
            message = connectionSocket.recv(1024)  # Buffer size to receive packets #Fill in start -a client is sending you a message   #Fill in end
            #print(message.decode("utf-8"))
            #print(message) # for testing
            #connectionSocket.send(message.decode("utf-8"))



            #print("Welcome to the server!")
            filename = message.split()[1]
            #filename = message

            # opens the client requested file.
            # Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
            f = open(filename[1:])

            data = f.read()# fill in start #fill in end


            # fill in end

            #outputdata = f.read()  #
            outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"
            outputdata2 = b"Server: Apache/2.4.1 (Unix); charset=UTF-8\r\n"
            outputdata3 = b"Connection: keep-alive; charset=UTF-8\r\n"
            # Fill in start -This variable can store your headers you want to send for any valid or invalid request.
            # Content-Type above is an example on how to send a header as bytes. There are more!
            # Fill in end

            # Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok?
            # Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
            # Fill in start

            connectionSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n", "UTF-8"))
            #print(response.encode())
            connectionSocket.send(bytes("<html><head></head><body><h1>200 OK</h1></body></html>\r\n", "UTF-8"))

            #response = 'HTTP/1.1 200 OK\nConnection: close\n\n' + outputdata
            #connectionSocket.send(response.decode())
            #print(response.decode("utf-8"))
            #connectionSocket.send(bytes('HTTP/1.1\n\n 200 OK Content-Type: text/html'))
            #connectionSocket.send(bytes('HTTP/1.1 200 OK\nContent-Type: text/html\n\n'))
            # Fill in end
            connectionSocket.send(bytes(data.encode("utf-8")))
            connectionSocket.send(bytes(outputdata))
            connectionSocket.send(bytes(outputdata2))
            connectionSocket.send(bytes(outputdata3))
            # Send the content of the requested file to the client
            for i in f:
                
                connectionSocket.send(data.encode())
                connectionSocket.send("\r\n".encode())
                # for line in file
                # Fill in start - send your html file contents #Fill in end
            connectionSocket.close()  # closing the connection socket

        except IOError:
            # Send response message for invalid request due to the file not being found (404)
            # Remember the format you used in the try: block!
            # Fill in start
            #print(message.decode("HTTP/1.1 404 Not Found"))
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n", "UTF-8"))
            connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n", "UTF-8"))
            #response = 'HTTP/1.1 404 Not Found'
            #connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n", "UTF-8"))
            #print(response.encode("utf-8"))
            #connectionSocket.send(bytes('HTTP/1.1 404 Not Found Content-Type: text/html\n\n'))
            #connectionSocket.send(bytes('HTTP/1.1 404 Not Found\r\n\r\n'.encode()))
            # Fill in end

            # Close client socket
            # Fill in start
            connectionSocket.close()
            # Fill in end
        except BrokenPipeError:
            print('BrokenPipeError caught')




if __name__ == "__main__":
    webServer(13331)
