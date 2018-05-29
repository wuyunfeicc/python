#面向对象，用字典写学生管理系统
class Student():
	name = ''
	age = ''
	name_code = ''
	stu = {}
	#增加信息
	def add_info(self):
		self.name = input('请输入姓名：')
		self.age = input('请输入年龄：')
		self.name_code = input('请输入学号：')
		if self.name_code in self.stu:
			return False
		self.stu[self.name_code]={'name':self.name,'age':self.age,'name_code':self.name_code}
		print(self.stu)
		return True
		
	#删除信息
	def del_info(self):
		print(self.stu)
		name_code=input('输入学号：')
		if name_code not in self.stu:
			return False
		del self.stu[name_code]
		return True
	#更改信息
	def edit_info(self):
		print(self.stu)
		name_code=input('输入学号：')
		if name_code not in self.stu:
			return False
		new_name_code = input('输入新学号：')
		new_name = input('输入新姓名：')
		new_age = input('输入新年龄：')
		if new_name_code==name_code:
			self.stu[name_code]={'name':self.name,'age':self.age,'name_code':self.name_code}
		else:
			print(self.stu)
			if new_name_code in self.stu:
				return False
			else:
				del self.stu[name_code]
				print(self.stu)
				self.stu[new_name_code]={'name':new_name,'age':new_age,'name_code':new_name_code}
				print(self.stu)
		return True
		
	#查看信息
	def inspect_info(self):
		print(self.stu)
		name_code=input('输入学号：')
		if name_code not in self.stu:
			return False
		# self.stu[name_code]={'name':self.name,'age':self.age,'name_code':self.name_code}
		print(self.stu[name_code]['name'])
		print('学号{}，姓名{},年龄{}'.format(self.stu[name_code]['name_code'],self.stu[name_code]['name'],self.stu[name_code]['age']))
		return True

	print('欢迎来到学生管理系统')
	
while True:
	
	print('请选择要进行的操作')
	checked = input('增加（A），删除(D)，更改(E)，查看(I)，退出(Q)')
	student = Student()
	if checked.lower()=='a':
		
		bool = student.add_info()
		if bool==True:
			print('增加成功')
		else:
			print('失败')
	elif checked.lower()=='d':
		
		bool = student.del_info()
		if bool==True:
			print('删除成功')
		else:
			print('失败')

	elif checked.lower()=='e':
		bool = student.edit_info()
		if bool==True:
			print('修改成功')
		else:
			print('失败')

	elif checked.lower()=='i':
		bool = student.inspect_info()
		if bool==True:
			print('查看成功')
		else:
			print('失败')

	elif checked.lower()=='q':
		print('欢迎下次光临')
		exit()
	else:
		print('无效操作')
		pass
