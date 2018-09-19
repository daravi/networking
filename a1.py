from socket import *

server_address = ('', 6969)

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(10)
print("Server is ready...")

while True:
    connection_socket, client_address = server_socket.accept()
    print("Connecting to", str(client_address), "...")
    request = connection_socket.recv(1024)
    #print(request.decode())
    print("Requested file at:", request.splitlines()[0][4:-9])
    connection_socket.close()
