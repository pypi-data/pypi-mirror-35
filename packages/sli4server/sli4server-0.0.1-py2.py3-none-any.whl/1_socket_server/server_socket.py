from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSocket = socket(AF_INET, SOCK_STREAM)
tcpSerSocket.bind(ADDR)
tcpSerSocket.listen(5)

while True:
    print("waiting for connection...")
    tcpCliSocket, addr = tcpSerSocket.accept()
    print("...connected from", addr)

    while True:
        data = tcpCliSocket.recv(BUFSIZE)
        if not data:
            break
        tcpCliSocket.send(bytes("[%s] %s" % (ctime(), data), 'utf-8'))
    tcpCliSocket.close()
tcpSerSocket.close()