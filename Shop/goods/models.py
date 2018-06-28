from django.db import models
from manager.models import ManagerLogin
from users.models import UserB
from django.utils import timezone

# Create your models here.
#创建商品类型表
class GoodsType(models.Model):
    #类型ID 自定义主键
    type_id = models.AutoField(auto_created=True,primary_key=True,db_column='type_id')
    #类型名称
    type_name = models.CharField(default='',null=False,max_length=50)
    #类型顺序
    type_sort = models.IntegerField(default=0)




class GoodsInfor(models.Model):
    #商品编号
    goods_num = models.CharField(max_length=20,default='')
    #商品名称
    goods_name = models.CharField(max_length=200,default='')
    #商品原价
    goods_oprice = models.FloatField()
    #商品现价
    goods_xprice = models.FloatField()
    #商品库存
    goods_count = models.IntegerField(default=0)
    #商品介绍
    goods_infor = models.CharField(max_length=100)
    #商品图
    goods_pic = models.ImageField(default='',upload_to='media/uploads')
    #商品存储方法
    goods_method = models.CharField(default='',max_length=50)
    #商品地址
    goods_address = models.CharField(default='',max_length=200)
    #商品内容
    goods_content = models.TextField()
    #商品类型
    type = models.ForeignKey(GoodsType,default='',db_column='type_id')
    #店铺ID
    manager = models.ForeignKey(ManagerLogin,default='',db_column='manager_id')


#创建评论数据表
class GoodsContent(models.Model):
    #主键ID
    content_id = models.AutoField(auto_created=True,primary_key=True,db_column='content_id')
    #商品ID
    goods = models.ForeignKey(GoodsInfor,db_column='goods_id',default='')
    #卖家ID
    manager = models.ForeignKey(ManagerLogin,db_column='manager_id',default='')
    #用户id
    user = models.ForeignKey(UserB,default='',db_column='user_id')
    #评论内容
    comment_content = models.TextField()
    #评论时间
    comment_time = models.DateTimeField(default=timezone.now)

