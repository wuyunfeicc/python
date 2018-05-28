
#引入模块
from socket import *
import re
from multiprocessing import Process
class MySever(object):
	def __init__(self):
		super().__init__()
	#创建一个套接字
		self.server_socket = socket(AF_INET,SOCK,STREAM)
	#绑定地址
		address = ('',4563)
		self.server_socket.bind(address)
	def start(self):
		while True:
		#监听
			self.server_socket.listen(128)
		#阻塞
		 	client_server,client_address = self.server_socket.accept()
		 #创建一个进程
		 	p = Process(target=handle_server,args=(client_server,))
		 	p.start()
		 	p.join()
		 	client_server.close()
	def handle_server(client_server):
		#接受信息
		resquest = client_server.recv(2048)
		#解析信息
		resquest_start_line = resquest.splitline()
		resquest_line = resquest_start_line[0].decode('utf-8')
		#用正则表达式匹配信息
		file_name = re.match('/w+ +([^ ]*)',resquest_line).group(1)
		#
		try:
			file = open('./'+file_name,'rb+')
		except IOError:
			response_start_line='http/1.1 404 Not Found\r\n'
			response_header='Server:My Server \r\n'
			response_body ='Not Found'
		else:
			file1 = file.read()
			file.close()
			response_start_line='http/1.1 200 ok\r\n'
			response_header = 'Server:My Server\r\n'
			response_body = file1
		response = response_start_line+response_header+'\r\n'+response_body
		#发送信息
		client_server.send(response.encode('utf-8'))
def main():
	if __name__=='__main__':
		#实例化
		m = MyServer()
		m. start()
main()


