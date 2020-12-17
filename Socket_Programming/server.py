import socket

HEADER_SIZE = 10

#CREATING SOCKET AND GIVING IT TYPE
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#BINDING SOCKET TO A ADDRESS, THAE ADDRESS SHOULD BE A TUPLE
s.bind(('127.0.0.1', 1234))

#MADE A QUEUE OF 5 AS A BUFFER
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    # SENDING A MESSAGE

    msg = "Msg with header"
    msg = f'{len(msg) :< {HEADER_SIZE}}' + msg

    clientsocket.send(bytes(msg,"utf-8"))

    # print("Terminating Connection")
    #clientsocket.close()

