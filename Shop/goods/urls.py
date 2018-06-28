from django.conf.urls import url
from . import views
urlpatterns = [
    #商品列表
    url(r'goods_list/',views.goods_list,name='goods_list'),
    #商品添加
    url(r'goods_add/',views.goods_add,name='goods_add'),
    url(r'goods_adddo',views.goods_adddo,name='goods_adddo'),
    #商品删除
    url(r'goods_del/(?P<pk>\d+)',views.goods_del,name='goods_del'),
    #商品操作
    url(r'goods_caozuo/(?P<pk>\d+)',views.goods_caozuo,name='goods_caozuo'),
    url(r'goods_caozuodo',views.goods_caozuodo,name='goods_caozuodo'),
    #商品类型
    url(r'goods_type',views.goods_type,name='goods_type'),
    url(r'type/(?P<pk>\d+)',views.type,name='type'),
    #商品详情
    url(r'goods_xiangqing/(?P<pk>\d+)',views.goods_xiangqing,name='goods_xiangqing'),
]