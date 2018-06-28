from django.conf.urls import url
from . import views
#前台用户
urlpatterns = [
    #注册
    url(r'zhuce',views.zhuce,name='zhuce'),
    url(r'zcdo',views.zcdo,name = 'zcdo'),
    #登录
    url(r'denglu',views.denglu,name='denglu'),
    url(r'dldo',views.dldo,name = 'dldo'),
    #进入主页
    url(r'index',views.index,name='index'),
    #注销用户
    url(r'tuichu', views.tuichu, name='tuichu '),
    #个人中心
    url(r'user_center',views.user_center,name='user_center'),
    #修改密码
    url(r'userupdateps',views.userupdateps,name='userupdateps'),
    url(r'updatepsdo',views.updatepsdo,name='updatepsdo'),
    #确认收货
    url(r'qrshouhuo/(?P<pk>\d+)/(?P<did>\d+)/(?P<num>\d+)/(?P<gid>\d+)',views.qrshouhuo,name='qrshouhuo'),
    #商品评价
    url(r'pingjia/(?P<pk>\d+)/(?P<did>\d+)',views.pingjia,name='pingjia'),
    url(r'pingjiado',views.pingjiado,name='pingjiado'),
    #查看订单详情
    url(r'dingdanxq/(?P<pk>\d+)/(?P<did>\d+)',views.dingdanxq,name='dingdanxq'),
    #收货地址
    url(r'shouhuo',views.shouhuo,name='shouhuo'),
    #添加收货地址
    url(r'tjaddress',views.tjaddress,name='tjaddress'),
    url('tianjiadizhido',views.tianjiadizhido,name='tianjiadizhido'),
    #删除地址
    url(r'delatedizhi',views.delatedizhi,name='delatedizhi'),
    #编辑地址
    url(r'bianjiaddress(?P<aid>\d+)',views.bianjiaddress,name='bianjiaddress'),
    url(r'bianjidizhido',views.bianjidizhido,name='bianjidizhido'),
    #会员列表
    url(r'uservip',views.uservip,name='uservip'),
    #查看消费记录
    url(r'chakanpay/(?P<uid>\d+)',views.chakanpay,name='chakanpay'),
    #查看订单编号中详情
    url(r'chakanxq/(?P<oid>\d+)',views.chakanxq,name='chakanxq'),
    #发送邮件
    url(r'fasong_mail',views.fasong_mail,name='fasong_mail'),
    #查看邮件
    url(r'chakanemail',views.chakanemail,name='chakanemail'),

]