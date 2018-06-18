from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'zhuce',views.zhuce,name='zhuce'),
    url(r'zcdo',views.zcdo,name='zcdo'),
    url(r'denglu',views.denglu,name='denglu'),
    url(r'dldo',views.dldo,name='dldo'),
    url(r'index',views.index,name='index'),
    url(r'zhuxiao',views.zhuxiao,name='zhuxiao'),
]