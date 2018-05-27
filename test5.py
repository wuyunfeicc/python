#用列表做学生管理系统，面向对象
#先定义一个学生类
class Student():
	lis = []
	name = ''
	age = ''
	name_code =''
		#增加信息
	def add_info(self):
		self.name=input('输入名字:')
		self.age=int(input('输入年龄:'))
		self.name_code=input('输入学号:')
		if self.name_code in self.lis:
			return False
		self.lis.append([self.name_code,[[self.name],[self.age],[self.name_code]]])
		return True


		#删除信息
	def del_info(self):
		print(self.lis)
		name_code=input('输入学号:')
		if name_code in self.lis:
			return False
		for i in self.lis:
			if i[0] == name_code:
				self.lis.remove(i)
				print(self.lis)
				return True


		#更改信息
	def edit_info(self):
		name_code=input('输入学号:')
		if name_code not in self.lis[0]:
			return False
		new_name_code = input('输入新学号：')
		for i in self.lis:
			if i[0] == name_code:
				self.lis.remove(i)
				self.lis.append([new_name_code,[[self.name],[self.age],[new_name_code]]])
				return True

		#查看信息
	def inspect_info(self):
		name_code=input('输入学号:')
		if name_code not in self.lis[0]:
			return False
		for i in self.lis:
			if i[0]==name_code:
				print(i[0])
				print('学号{}，姓名{}，年龄{}'.format(i[0],i[1][0][0],i[1][1][0]))
				return True

print('学生管理系统')
while True:
	print("请选择您要进行的操作")
	checked = input('添加(A),删除（D），更改（E)，查看（I），退出（Q)')
	student = Student()
	if checked.lower()=='a':
		bool = student.add_info()
		if bool==True:
			print('添加成功')
		else:
			print('添加失败')
	elif checked.lower()=='d':
		bool =student.del_info()
		if bool==True:
			print('删除成功')
		else:
			print('删除失败')
		
	elif checked.lower()=='e':
		bool = student.edit_info()
		if bool==True:
			print('更改成功')
		else:
			print('更改失败')
		
	elif checked.lower()=='i':
		bool = student.inspect_info()
		if bool==True:
			print('查看成功')
		else:
			print('查看失败')
	elif checked.lower()=='q':
		print('再见')
		exit()
	else:
		print('无效操作')
		pass
