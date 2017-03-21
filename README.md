# tp1

PINEAU

- 1 

###Code pour le client UDP : 
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
###Code pour le serveur UDP : 
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

En utilisant la commande netcat, on remplace le programme pour le client par : ``` nc -u localhost 12000 ``` et le programme pour le serveur par : ``` nc -u -l -p 12000 ```.
Le 'nc' signifie que l'on est en Netcat, le '-u' en UDP, le 'localhost' pour le nom du serveur et '12000' pour le numéro du port et le '-l' signifie listen pour le serveur.
Cette commande permet de configurer un client et un serveur pour qu'il communique, elle ne fais rien d'autre.

- 3 

###Code pour le client TCP : 
```python
from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence
clientSocket.close()
```
###Code pour le serveur TCP : 
```python
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)
	connectionSocket.close()
 ```
Dans le terminal du client, on rentre un texte et le serveur nous renvoie ce texte en majuscule.

- 4 

En utilisant la commande netcat, on remplace le programme pour le client par : ``` nc localhost 12000 ``` et le programme pour le serveur par : ``` nc -l -p 12000 ```.
Le 'nc' signifie que l'on est en Netcat, le 'localhost' pour le nom du serveur et '12000' pour le numéro du port et le '-l' signifie listen pour le serveur.
Cette commande permet de configurer un client et un serveur pour qu'il communique, elle ne fais rien d'autre.

- 5 

###Code pour le filtre : 
```python
from socket import *

serverPortIn = 12001
serverPortOut = 13001

serverName = "localhost"


serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPortIn))
serverSocket.listen(1)

serverSocket2 = socket(AF_INET,SOCK_STREAM)
serverSocket2.bind(('',serverPortOut))
serverSocket2.listen(1)

while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	modifiedSentence = sentence.upper()
	connectionSocket.send(modifiedSentence)
	print modifiedSentence
	connectionSocket.close()
# client 2
	while 1:
		connectionSocket, addr = serverSocket2.accept()
		connectionSocket.send(modifiedSentence)
		connectionSocket.close()
```
Mais nous avons exactement le même code pour le serveur sauf que l'on change son numéro de port (13000).

###Code pour le serveur : 
```python
from socket import *
serverPort = 13000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	connectionSocket.send(sentence)
	print sentence
	connectionSocket.close()
```
Enfin nous avons le code pour le client qui reste exactement le même : 

###Code pour le client : 
```python
from socket import *
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence
clientSocket.close()
```
