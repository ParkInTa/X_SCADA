import socket, threading

def send(uname):
	while True:
		msg = input('\nMe > ')
		data = uname + '>' + msg
		cli_sock.send(data.encode())

def receive():
	while True:
		data = cli_sock.recv(1024).decode()
		print('\t' + str(data))

if __name__ == '__main__':
	cli_sock = \
		socket.socket(socket.AF_INET, \
			socket.SOCK_STREAM)

	HOST = '192.168.0.56'
	PORT = 7788
	uname = input('ID 입력 > ')
	cli_sock.connect((HOST, PORT))
	print('TCP 서버 접속...')

	thread_send = \
		threading.Thread(target=send, \
			args=[uname])
	thread_send.start()

	thread_receive = \
		threading.Thread(target=receive)
	thread_receive.start()