import socket

######### Receiving complete message without HEADER FUNCTION ###########

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.2', 1555))
s.listen(4)

while True:
    clientsocket, address = s.accept()
    print(f'Now connected to {address}')
    clientsocket.send(bytes("You are connected to server now",'utf-8'))

    clientsocket.close()