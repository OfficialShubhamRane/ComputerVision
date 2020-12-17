import socket

######### Receiving complete message without HEADER FUNCTION ###########

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.2', 1555))

msg = ''
msg += (s.recv(10)).decode('utf-8')
len1 = len(msg)

while True:
    msg += (s.recv(10)).decode('utf-8')
    len2 = len(msg)
    if len1 == len2:
        print(msg)
        break
    else:
        len1 = len2
s.close()