from socket import *
import sys

HOST = '192.168.0.61'
PORT = 7788 # 1~1024 : well known port(사용불가)
ADDR = (HOST, PORT)

# 소켓 : 가상으로 네트워크를 통해서 서로간의 연결
# 클라이언트 소켓 생성
# AF_INET : 네트워크 패밀리

clientSocket = socket(AF_INET, SOCK_STREAM)
try:
    clientSocket.connect(ADDR)
    print('서버 접속 시도')
    clientSocket.close()
    print('클라이언트 종료')
except Exception as e:
    print('%s:%s' %ADDR)
    sys.exit()