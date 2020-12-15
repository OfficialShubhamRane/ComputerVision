import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1234))

#RECIEVING A MESSAGE
# msg = s.recv(1024)
# print(msg.decode('utf-8'))

# while True:
full_msg = ''
while True:
    msg = s.recv(8)
    if len(msg) == 0:
        break
    full_msg += msg.decode('utf-8')
print(full_msg)