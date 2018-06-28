from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'cart_add',views.cart_add,name='cart_add'),
    url(r'gouwuche',views.gouwuche,name='gouwuche'),
    url(r'cart_delate/(?P<pk>\d+)',views.cart_delate,name='cart_delate'),
    url(r'jiacount/(?P<pk>\d+)/(?P<user_id>\d+)',views.jiacount,name='jiacount'),
    url(r'jiancount/(?P<pk>\d+)/(?P<user_id>\d+)',views.jiancount,name='jiancount'),
    url(r'clearcart',views.clearcart,name='clearcart'),
    #下订单
    url(r'xiadan',views.xiadan,name='xiadan'),
    #收货页面
    url(r'address_shouhuo',views.address_shouhuo,name='address_shouhuo'),
    url(r'address_shdo',views.address_shdo,name='address_shdo'),
    #提交订单
    url(r'addorder',views.addorder,name='addorder'),
    url(r'orderdetails',views.orderdetails,name='orderdetails'),
    #提交订单成功
    url(r'successful',views.successful,name='successful'),




    ]