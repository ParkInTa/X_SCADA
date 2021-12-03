import socket

HOST = '192.168.0.61'
PORT = 7788
BUF_SIZE = 1024

s=socket.socket()
s.bind((HOST, PORT))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('접속정보:', addr)
    data = conn.recv(BUF_SIZE).decode()
    print('메세지:', data)
    
    fileName = '/home/pi/work/test.txt'
    f=open(fileName, 'rb')
    fileData = f.read(BUF_SIZE)
    while fileData:
        conn.send(fileData)
        fileData = f.read(BUF_SIZE)
    f.close()
    print('파일 전송 완료')
    conn.close()