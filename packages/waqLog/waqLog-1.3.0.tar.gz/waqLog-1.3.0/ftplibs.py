import re
import socket


class Ftp(object):
	def __init__(self, host=None, port=None, user=None, pwd=None):
		self.host = '47.95.120.193'
		self.port = 21
		self.user = 'asdwan'
		self.pwd = 'qws168'
		self.sock = socket.socket()
		if host:
			self.host = host
			self.port = port
			self.connect()
			if user:
				self.user = user
				self.pwd = pwd
				self.login()

	def get_return(self, s):
		data = s.recv(1024)
		return data

	def gb2str(self):
		data = self.get_return(self.sock)
		print(data)
		print(data.decode('gb2312', 'ignore'))
		return data.decode('gb2312', 'ignore')

	def connect(self):
		self.sock.connect((self.host, self.port))
		self.gb2str()

	def login(self):
		self.sock.sendall('USER {}\r\n'.format(self.user).encode())
		self.gb2str()
		self.sock.sendall('PASS {}\r\n'.format(self.pwd).encode())
		self.gb2str()
		self.sock.sendall(b'PASV\r\n')
		rev = self.gb2str()
		ports = re.findall('\d+', rev)
		self.newPort = int(ports[5]) * 256 + int(ports[6])
		print(self.newPort)

		self.newSock = socket.socket()
		self.newSock.connect((self.host, self.newPort))

	def download(self, filename):
		self.create_sock()
		print(b'RETR %b\r\n' % filename.encode())

		self.sock.sendall(b'RETR %b\r\n' % filename.encode())

		text = b''
		with open(filename, 'wb') as f:
			while True:
				data = self.newSock.recv(1024)
				if data != b'':
					text += data
				else:
					print(text)
					break
			f.write(text)
		self.gb2str()

	def cd(self, path):
		self.sock.sendall(b'CWD %b\r\n' % path.encode())
		self.gb2str()

	def create_sock(self):
		self.newSock.close()
		self.sock.sendall(b'PASV\r\n')
		rev = self.gb2str()
		ports = re.findall('\d+', rev)
		self.newPort = int(ports[5]) * 256 + int(ports[6])
		self.newSock = socket.socket()
		self.newSock.connect((self.host, self.newPort))

	def get_dir(self):
		self.sock.sendall(b'NLST\r\n')
		self.gb2str()
		data = self.newSock.recv(102400)
		print(data.decode())
		self.gb2str()
		self.create_sock()


if __name__ == '__main__':
	s = Ftp('47.95.120.193', 21, 'asdwan', 'qws168')
	s.cd('usedcar')
	s.get_dir()
	s.download('gf_car_used_20180903.txt')
	s.download('gf_car_used_20180904.txt')
	s.download('gf_car_used_20180901.txt')
	s.download('gf_car_used_20180902.txt')
