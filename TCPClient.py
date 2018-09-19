from socket import *

server_address = ("localhost", 6969)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(server_address)

message = input("Write something! ")

client_socket.send(message.encode())

# wait for response
rcvd_message = client_socket.recv(2048)

print(rcvd_message.decode())

client_socket.close()
