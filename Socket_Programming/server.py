import socket

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
    clientsocket.send(bytes("Hello client","utf-8"))

    print("Terminating Connection")
    s.close()

