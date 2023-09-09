
##################### Sending commands at once ###########################

import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0',9000))                        #server side

receiving_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiving_sock.bind(('',8890))

tello_addr = ('192.168.10.1',8889)
rcv_addr = ('192.168.10.1',8890)
video_addr = ('192.168.10.1',11111)

print("command")
sock.sendto(b'command',tello_addr)
response1, ip = receiving_sock.recvfrom(1024)
print(response1.decode('utf-8'))

sock.sendto(b'streamon',tello_addr)

print("takeoff")
sock.sendto(b'takeoff',tello_addr)
response2, ip = receiving_sock.recvfrom(1024)
print(response2.decode('utf-8'))
# time.sleep(5)

print("right 30")
sock.sendto(b'right 30',tello_addr)
response3, ip = receiving_sock.recvfrom(1024)
print(response3.decode('utf-8'))

# print("battery?")
# receiving_sock.sendto(b'battery?',rcv_addr)         #This one needs to receives response; thats why below code.
# response4, ip = receiving_sock.recvfrom(1024)          # ok
# print(response4.decode('utf-8'))
# response5, ip = receiving_sock.recvfrom(1024)         # battery percentage
# print(response5.decode('utf-8'))

print("land")
sock.sendto(b'land',tello_addr)
response6, ip = sock.recvfrom(1024)
print(response6.decode('utf-8'))

sock.sendto(b'streamoff',tello_addr)

sock.close()