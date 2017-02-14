from socket import *

serverName = "10.98.2.87"
serverPort = 12000 
clientSocket = socket(AF_INET, SOCK_DGRAM) 
message = raw_input(" texte ")
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)                  
print modifiedMessage
clientSocket.close()
     