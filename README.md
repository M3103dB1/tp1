# tp1

PINEAU

- 1 

###Code pour le client : 
```python
from socket import *
 serverName = ‘hostname’ 
 serverPort = 12000 
 clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM) 
 message = raw_input(’Input lowercase sentence:’)
 clientSocket.sendto(message,(serverName, serverPort))
 modifiedMessage, serverAddress = clientSocket.recvfrom(2048)                  
 print modifiedMessage
clientSocket.close()
```
###Code pour le serveur : 
```python
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((’’, serverPort))
print ”The server is ready to receive”
while 1:
      message, clientAddress = serverSocket.recvfrom(2048)
      modifiedMessage = message.upper()
      serverSocket.sendto(modifiedMessage, clientAddress)
```
On peut voir que quand on envoie un texte dans le client, le serveur nous renvoie exactement le même texte mais en majuscule.
- 2
- 3 
- 4 
