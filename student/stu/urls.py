from django.conf.urls import url
# from django.contrib import admin
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'add',views.add,name='add'),
    url(r'ado',views.ado,name='ado'),
    url(r'xs',views.xs,name='xs'),
    url(r'shanchu/(?P<pk>[0-9]+)', views.shanchu, name='shanchu'),
    url(r'xiugai/(?P<pk>[0-9]+)', views.xiugai, name='xiugai'),
    url(r'xiugaido', views.xiugaido, name='xiugaido'),
]