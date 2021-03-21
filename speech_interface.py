import socket               # Import socket module

sock = socket.socket()         # Create a socket object
host = '127.0.0.1' # Get local machine name
port = 2500
print(host)                # Reserve a port for your service.

sock.connect((host, port))
print(sock.recv(1024))
sock.close()                     # Close the socket when done