from django.db import models
from django.utils import timezone
# Create your models here.
#创建前台用户数据表
class UserB(models.Model):
    username = models.CharField(max_length=40)
    userpass = models.CharField(max_length=40)
    add_time = models.DateTimeField(default=timezone.now)
    user_id = models.AutoField(auto_created=True, primary_key=True,db_column='user_id')
    #用户头像
    user_pic =models.ImageField(max_length=50,upload_to='media/uploads',null=True)
    #用户邮箱
    user_email = models.CharField(max_length=100,default='')


#系统 发送邮件的表，给每一个新注册的用户
class UserEmail(models.Model):
    mail_id = models.AutoField(auto_created=True,primary_key=True,db_column='mail_id')
    mail_time = models.DateTimeField(timezone.now())
    user=models.ForeignKey(UserB,default='',db_column='user_id')
    title = models.CharField(default='',max_length=200)
    body = models.TextField()