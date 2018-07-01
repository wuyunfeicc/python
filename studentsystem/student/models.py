from django.db import models

# Create your models here.
class Student(models.Model):
    stu_id = models.AutoField(auto_created=True,primary_key=True,db_column='stu_id')
    #学号
    xuehao = models.CharField(max_length=50,default='')
    stuname = models.CharField(max_length=80,default='')
    stusex = models.CharField(max_length=10,default='')
    age = models.IntegerField()
    grade = models.CharField(max_length=20,default='')
    zhuanye = models.CharField(max_length=50)
    address = models.TextField()