# This module is written to be run using the python2.7 interpreter to 
# connect with ros Melodic
import socket

host = ''
port = 2500
sock = socket.socket()
sock.bind((host, port))
sock.listen(5)
while True:
   c, addr = sock.accept()     # Establish connection with client.
   print('Got connection from: {}', addr)
   c.send('Thank you for connecting')
   c.close()                # Close the connection