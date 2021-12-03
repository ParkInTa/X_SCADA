import socket

s=socket.socket()
HOST = '192.168.0.56'
PORT = 7788
BUF_SIZE = 1024

s.connect((HOST, PORT))
s.send(b'Hello servar!')

with open('received_file', 'wb') as f:
    print('file open')
    while True:
        data = s.recv(BUF_SIZE)
        if not data:
            break
        f.write(data)
f.close()
s.close()