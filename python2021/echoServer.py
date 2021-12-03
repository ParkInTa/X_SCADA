from socket import *

HOST = '192.168.0.61'
PORT = 7788
BUF_SIZE = 1024


servSock = socket(AF_INET, SOCK_STREAM)
servSock.bind((HOST, PORT))
servSock.listen(5)
print('서버 대기중...')

conn, addr = servSock.accept()
print('접속한 클라이언트 서켓 정보:', addr)

while True:
    data = conn.recv(BUF_SIZE)
    if not data:
        break
    conn.sendall(data)
    
conn.close()
servSock.close()