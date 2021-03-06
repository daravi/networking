from socket import *

server_port = 6969

# server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(('', server_port)) # '' means ANY, i.e. bind to all network interfaces

server_socket.listen(1)

print("The server is ready to receive... ")

while True:
	connection_socket, addr = server_socket.accept()
	# msg, addr = server_socket.recvfrom(2048)
	msg = connection_socket.recv(1024)
	print("Recieved: ")
	print(msg.decode())
	# response = msg.decode().upper()
	# server_socket.sendto(response.encode(), addr)
	# connection_socket.send(response.encode())
	connection_socket.close()
