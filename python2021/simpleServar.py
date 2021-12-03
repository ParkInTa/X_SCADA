from socket import *

HOST = '192.168.0.61'
PORT = 7788
ADDR = (HOST, PORT)

#서버 소켓 생성
serverSock = socket(AF_INET, SOCK_STREAM)
print('서버 소켓 생성')
#서버 주소를 서버 소켓에 바인딩
serverSock.bind(ADDR)
print('서버 주소 바인딩')
#클라이언트에서 접속하도록 대기중
serverSock.listen(5)
print('서버 연결 대기중...')
#클라이언트 접속 허용
cliebtSock, addr_info = serverSock.accept()
print('클라이언트 접속 허용')
#접속한 클라이언트, 서버 소켓 종료
cliebtSock.close()
serverSock.close()
print('서버 소켓, 접속한 클라이언트 소켓 종료')