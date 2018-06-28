from django.db import models
from users.models import UserB
from manager.models import ManagerLogin
from goods.models import GoodsInfor
from django.utils import timezone
# Create your models here.
#创建购物车表结构
class CartMessage(models.Model):
    #购物车主键id
    cart_id = models.AutoField(auto_created=True,primary_key=True,db_column='cart_id')
    #商品名称
    goods_name = models.CharField(max_length=100)
    #商品数量
    goods_num = models.IntegerField(default=0)
    #商品小计
    goods_xiaoji = models.FloatField()
    #商品现价
    goods_xprice = models.FloatField()
    #商品图片
    goods_pic = models.CharField(max_length=200)
    #前台用户ID,作为购物车的外键
    user = models.ForeignKey(UserB,db_column='user_id',default='')
    #商家ID（外键）
    manager = models.ForeignKey(ManagerLogin,db_column='manager_id',default='')
    #商品ID
    goods = models.ForeignKey(GoodsInfor,db_column='goods_id',default='')
#创建收货表
class GoodsAddress(models.Model):
    #主键ID
    address_id = models.AutoField(auto_created=True,primary_key=True,db_column='address_id')
    #收货人
    uname = models.CharField(max_length=30)
    #收货地址
    address = models.CharField(max_length=200)
    #联系电话
    phone = models.CharField(max_length=11)
    #用户ID（外键）
    user = models.ForeignKey(UserB,db_column='user_id',default='')
#创建的订单表
class Order(models.Model):
    #订单主键id
    order_id = models.AutoField(auto_created=True,primary_key=True,db_column='order_id')
    #订单编号
    order_num = models.CharField(max_length=50)
    #收货地址ID（外键）
    address = models.ForeignKey(GoodsAddress,db_column='address_id',default='')
    # 用户ID（外键）
    user = models.ForeignKey(UserB, db_column='user_id', default='')
    #订单总计
    total = models.FloatField()
    #下单时间
    order_time = models.DateTimeField(default=timezone.now)
    #订单状态
    order_status = models.IntegerField(default=0)#订单状态
    order_status = models.IntegerField(default=0)
#创建订单详情表
class OrderDetails(models.Model):
    #主键ID
    details_id = models.AutoField(primary_key=True,auto_created=True,db_column='details_id')
    #订单ID（外键）
    order = models.ForeignKey(Order,db_column='order_id',default='')
    #商品ID(外键）
    goods = models.ForeignKey(GoodsInfor,db_column='goods_id',default='')
    #商品名称
    goods_name = models.CharField(max_length=200)
    #商品单价
    goods_price = models.FloatField()
    #商品数量
    goods_num = models.IntegerField()
    #商品小计
    goods_xiaoji = models.FloatField()
    #商家ID
    manager = models.ForeignKey(ManagerLogin,db_column='manager_id',default='')
    #商品图片
    goods_pic = models.CharField(max_length=200)
    # 订单状态
    order_status = models.IntegerField(default=0)
