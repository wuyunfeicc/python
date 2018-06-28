from django.conf.urls import url
from . import views
urlpatterns = [
    #卖家登录路由
    url(r'denglu',views.denglu,name='denglu'),
    #卖家登录时获取数据
    url(r'dludo',views.dludo,name='dludo'),
    #跳转到后台主页
    url(r'main',views.main,name='main'),
    #卖家管理后台注销
    url(r'loginout',views.loginout,name='loginout'),
    #卖家注册获取数据
    url(r'zhucedo',views.zhucedo,name='zhucedo'),
    #卖家注册
    url(r'zhuce',views.zhuce,name='zhuce'),
    #卖家更改密码
    url(r'updatepass',views.updatepass,name='updatepass'),
    url(r'updatepsdo',views.updatepsdo,name='updatepsdo'),
    #卖家修改商品类型
    url(r'xiugaitype',views.xiugaitype,name='xiugaitype'),
    #删除商品类型
    url(r'type_del/(?P<pk>\d+)',views.type_del,name='type_del'),
    #后台商品类型编辑
    url(r'typebj/(?P<pk>\d+)',views.typebj,name='typebj'),
    #后台商品类型增加
    url(r'typeadd',views.typeadd,name='typeadd'),
    url(r'typebjdo',views.typebjdo,name='typebjdo'),
    url(r'tpadddoo',views.tpadddoo,name='tpadddoo'),
    #订单列表
    url(r'dingdanlist',views.dingdanlist,name='dingdanlist'),
    #订单详情
    url(r'dingdanxq/(?P<pk>\d+)/(?P<aid>\d+)',views.dingdanxq,name='dingdanxq'),
    #更改订单状态
    url(r'updatestatus',views.updatestatus,name='updatestatus'),
    #后台评论列表管理
    url(r'pinglunlist',views.pinglunlist,name='pinglunlist'),
    #查看评论的内容
    url(r'chakan_pinglun/(?P<pk>\d+)',views.chakan_pinglun,name='chakan_pinglun'),
    #待补货
    url(r'goodsless',views.goodsless,name='goodsless'),
    #补充货源
    url(r'goodsbuchong/(?P<gid>\d+)',views.goodsbuchong,name='goodsbuchong'),
    url(r'buchongdo',views.buchongdo,name='buchongdo'),

]