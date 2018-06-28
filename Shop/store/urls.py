from django.conf.urls import url
from . import views
urlpatterns = [
    #店铺详情
    url(r'storedetails/(?P<pk>\d+)',views.storedetails,name='storedetails'),
    #店铺下的商品分类
    url(r'store_goodstype/(?P<pk>\d+)',views.store_goodstype,name='store_goodstype'),
    #进入店铺主页
    url(r'store',views.store,name='store'),
]