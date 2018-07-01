from django.conf.urls import url
# from django.contrib import admin
from . import views
urlpatterns =[
    #系统主页
    url(r'index',views.index,name='index'),
    #增加学员
    url(r'add',views.add,name='add'),
    #删除
    url(r'shanchu',views.shanchu,name='shanchu'),
    #修改
    url(r'xiugai/(?P<sid>\d+)',views.xiugai,name='xiugai'),
    url(r'xiugaido',views.xiugaido,name='xiugaido'),
]