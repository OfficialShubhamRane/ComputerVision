
##################### Sending commands at once ###########################

import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('',9000))                        #server side

tello_addr = ('192.168.10.1',8889)
print("command")
sock.sendto(b'command',tello_addr)

# sock.sendto(b'streamon',video_socket)
print("takeoff")
sock.sendto(b'takeoff',tello_addr)
# time.sleep(5)

print("right 30")
sock.sendto(b'right 30',tello_addr)

print("battery?")
sock.sendto(b'battery?',tello_addr)         #This one needs to receives response; thats why below code.
# response, ip = sock.recvfrom(1024)          # ok
# response2, ip = sock.recvfrom(1024)         # battery percentage
# print(response2.decode('utf-8'))

print("land")
sock.sendto(b'land',tello_addr)
response, ip = sock.recvfrom(1024)

# sock.sendto(b'streamoff',video_socket)

sock.close()