#进程面向对象
from multiprocessing import Process
import os
import time
# def zjc():
# 	print('子进程{}'.format(os.getpid()))
# if __name__=='__main__':
# 	print('主进程{}'.format(os.getpid()))
# 	p = Process(target= zjc)
# 	p.start()
# 	p.join()
class MyProcess(Process):
	def __init__(self,b):
		super().__init__()

		self.b = b
	def run(self):
		print('父{} 子{}'.format(os.getppid(),os.getpid()))
		time.sleep(self.b)
def main():
	if __name__=='__main__':
		for i in range(10):
			m = MyProcess(0.5)
			m.start()
			m.join()
main()
