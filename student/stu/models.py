from django.db import models

# Create your models here.
class Student(models.Model):
    stu_id =models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    nianji = models.CharField(max_length=50)
    zhuanye = models.CharField(max_length=50)
    address =models.CharField(max_length=50)