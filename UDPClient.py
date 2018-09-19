from socket import *

serverName = 'localhost'
serverPort = 12000

serverAddress = (serverName, serverPort)

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentence:')

clientSocket.sendto(message.encode(), serverAddress)

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())

clientSocket.close()s

