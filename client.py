from socket import *

# server_address = ("localhost", 6969)
server_address = ("init-p01st.push.apple.com", 80)

# client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(server_address)

# message = input("Write something! ")
message = "GET http://init-p01st.push.apple.com/bag HTTP/1.1\nHost: init-p01st.push.apple.com\nProxy-Connection: keep-alive\nAccept: */*\nUser-Agent: Mac OS X/10.13.6 (17G65)\nAccept-Language: en-us\nAccept-Encoding: gzip, deflate\nConnection: keep-alive\n\n"

# client_socket.sendto(message.encode(), server_address)
client_socket.send(message.encode())

# wait for response
# rcvd_message, address = client_socket.recvfrom(2048)
rcvd_message = client_socket.recv(2048)

print(rcvd_message.decode())

client_socket.close()