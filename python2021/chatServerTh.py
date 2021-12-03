import socket
import threading

def acceptClient():
	while True:
		cli_sock, cli_addr = sock.accept() 
		print('클라이언트 접속: ', cli_sock)
		print('접속 정보: ', cli_addr)
		connList.append(cli_sock)
		thread_client = \
			threading.Thread(target= \
				broadcastUser, \
				args=[cli_sock])
		thread_client.start()

def broadcastUser(cli_sock):
	while True:
		try:
			data = cli_sock.recv(1024)
			if data:
				bUser(cli_sock, data)
		except Exception as x:
			print(x)
			break

def bUser(cs_sock, msg):
	for client in connList:
		if client != cs_sock:
			client.send(msg)

if __name__ == '__main__':
	connList = [] # 비어있는 리스트 생성
	HOST = ''
	PORT = 7788

	sock = \
		socket.socket(socket.AF_INET, \
			socket.SOCK_STREAM)
	sock.bind((HOST, PORT))
	sock.listen(5)
	print('서버 대기중...')
	threadServ = \
		threading.Thread(target=acceptClient)
	threadServ.start()