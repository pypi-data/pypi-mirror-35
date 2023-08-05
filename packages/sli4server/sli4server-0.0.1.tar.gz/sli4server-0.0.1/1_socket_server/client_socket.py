from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSocket = socket(AF_INET,SOCK_STREAM)
tcpCliSocket.connect(ADDR)
while True:
    data = input('> ')
    if not data:
        break
    tcpCliSocket.send(bytes(data, 'utf-8'))
    data = tcpCliSocket.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSocket.close()