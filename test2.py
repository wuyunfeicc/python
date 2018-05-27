#线程面向对象
from threading import Thread
import time
class MyThread(Thread):
	def __init__(self,a,b):
		super().__init__()
		self.a=a
		self.b=b
	def run(self):
		for i in range(self.a):
			print('线程{}'.format(i+1))
			time.sleep(self.b)
def main():
	if __name__=='__main__':
		m = MyThread(10,1)
		m.start()
main()
