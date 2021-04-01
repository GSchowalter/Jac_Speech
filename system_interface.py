# This module is written to be run using the python2.7 interpreter to 
# connect with ros Melodic
import socket
import rospy
from std_msgs.msg import Int8, String, Bool
from navigation_msgs import VehicleState, Stop

host = ''
port = 2500
sock = socket.socket()
sock.bind((host, port))
sock.listen(1)
c, addr = sock.accept()     # Establish connection with client.
print('Got connection from: {}', addr)

class sys_interface(object):
   def __init__(self):
        rospy.init_node('speech_detector')
        self.speech_text = rospy.Publisher('/speech_text', String, queue_size=10)
        self.stop_cart = rospy.Publisher('/stop', Stop, queue_size=10)
        cart_stopped = False
   
   def anounce(self, text):
      print("Publishing")
      self.speech_text.publish(text)

anouncer = sys_interface()

while True:
   text = c.recv(2048)
   fo = open("Log.txt", "w")
   fo.write(text.decode())
   print("Data: %s" %text.decode())
   anouncer.anounce(text.decode())
   if("halt" in text.decode()):
      c.close()                # Close the connection
      break
   if("stop" in text.decode()):
      stop_msg = Stop()
      cart_stopped = True
      stop_msg.stop = True
      stop_msg.sender_id = "voice"
      stop_pub.publish(stop_msg)
   if("resume" in text.decode() and cart_stopped):
      stop_msg = Stop()
      cart_stopped = False
      stop_msg.stop = False
      stop_msg.sender_id = "voice"
      stop_pub.publish(stop_msg)
