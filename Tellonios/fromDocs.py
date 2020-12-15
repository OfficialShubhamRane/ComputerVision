
##################### Sending commands at once ###########################

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('',9000))                        #server side

tello_addr = ('192.168.10.1',8889)

sock.sendto(b'command',tello_addr)

sock.sendto(b'takeoff',tello_addr)


sock.sendto(b'right 100',tello_addr)


sock.sendto(b'battery?',tello_addr)         #This one needs to receives response; thats why below code.
response, ip = sock.recvfrom(1024)


print("Will be landing now.")
sock.sendto(b'land',tello_addr)

sock.close()