from socket import *

HOST = '192.168.0.61'
PORT = 7788
BUF_SIZE = 1024
str = '안녕하세요'

clientSock = socket(AF_INET, SOCK_STREAM) #TCP 프로토콜
clientSock.connect((HOST, PORT))

clientSock.sendall(str.encode('utf-8'))
data = ((clientSock.recv(BUF_SIZE)).decode('utf-8'))
print('데이터 수신:', data)
clientSock,close()