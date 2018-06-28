from django.db import models
from django.utils import timezone
# Create your models here.
#创建后台卖家信息数据表
class ManagerLogin(models.Model):
    username = models.CharField(max_length=40)
    userpass = models.CharField(max_length=40)
    #商家昵称
    nicheng = models.CharField(max_length=40,null=True)
    #店铺名称
    shop_name = models.CharField(max_length=50,null=True)
    #店铺logo
    shop_logo = models.ImageField(max_length=50,upload_to='media/uploads',null=True)
    #店铺地址
    shop_address = models.CharField(max_length=100,null=True)
    #后台商家得主ID
    manager_id = models.AutoField(auto_created=True, primary_key=True, db_column='manager_id')
