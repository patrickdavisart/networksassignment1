#Davis_Patrick_Assignment1.py

from socket import *

#Start main()
def main():

    #Specify port 80
    serverPort = 80
    #socket process
    serverSocket = socket(AF_INET,SOCK_STREAM)
    #bind
    serverSocket.bind(('',serverPort))

    #Listen for the connection
    serverSocket.listen(1)

    #Print the port address
    print("Web Server On Port",serverPort)

    #while loop begins
    while True:

        #Establish the connection
        print("Server Process Is Ready")

        #Create connection socket for accepted client
        connectionSocket,address = serverSocket.accept()

        #Starting the try block.
        try:

            #Recieve message.
            message = connectionSocket.recv(1024)

            #Print the connection message
            print(message)

            #Determine the filename
            filename = message.split()[1]

            #Print the file name
            print(filename[1])

            print(filename,'||',filename[1])

            #Open the file
            f = open(filename[1:])
            outputdata = f.read()

            #DEBUG to check output data
            print(outputdata)

            #Send one HTTP header line into socket
            connectionSocket.send("""HTTP/1.0 200 OK
                Content-Type: text/html

            <html>
            
            <head>
            <title>Success</title>
            </head>
            <body>
            Your file Exist!
            </body>
            </html>
            """.encode());

            #connectionSocket.send(outputdata)

            #connectionSocket.send(message)
            connectionSocket.close()

        #If IOError
        except IOError:

            #Send response message for the file not found.
            print ("404 Not Found")
            connectionSocket.send("""HTTP/1.0 404 Not Found\r\n""".encode());
            pass

        #Temp break
        break
    pass

if __name__ =="__main__":
    main()
