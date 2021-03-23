# This module is written to be run using the python2.7 interpreter to 
# connect with ros Melodic
import socket

host = ''
port = 2500
sock = socket.socket()
sock.bind((host, port))
sock.listen(1)
c, addr = sock.accept()     # Establish connection with client.
while True:
   print('Got connection from: {}', addr)
   c.send('Thank you for connecting'.encode())
   text = c.recv(1024)
   fo = open("Log.txt", "w")
   fo.write(text.decode())
   print("Data: %s" %text.decode())
   if("stop" in text.decode()):
      c.close()                # Close the connection
      break