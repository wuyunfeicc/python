from django.conf.urls import url
from . import views

urlpatterns=[
    # url(r'index/',views.hello),
    # url(r'test/',views.test),
    url(r'add',views.add,name='add'),
    url(r'ado',views.ado,name='ado'),
    url(r'xs',views.xs,name='xs'),
    url(r'xq/(?P<pk>[0-9]+)',views.xq,name='xq'),
    url(r'shanchu/(?P<pk>[0-9]+)',views.shanchu,name='shanchu'),
    url(r'bianji/(?P<pk>[0-9]+)',views.bianji,name='bianji'),
    url(r'xiugaido',views.xiugaido,name='xiugaido')
]