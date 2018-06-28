from django.shortcuts import render
from .models import ManagerLogin
from goods.models import GoodsType,GoodsContent
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from goods.models import GoodsInfor
from cart.models import OrderDetails,Order,GoodsAddress
from django.db.models import Sum
import json
#卖家登录模板页面
def denglu(request):
    return render(request,'manager/login.html')
def dludo(request):
    username = request.POST['username']
    userpass = request.POST['userpass']
    # result = ManagerLogin.objects.filter(userpass=userpass,username=username)
    #调用model做查询，通过和数据库对比是否相同
    users = ManagerLogin.objects.filter(userpass=userpass,username=username)
    if users:
        #登录成功后记录商家用户名和商家ID
        # 单条数据查询，获取当前卖家的卖家ID
        manager_id = ManagerLogin.objects.get(username=username, userpass=userpass).manager_id
        request.session['managername'] = username
        request.session['manager_id'] = manager_id
        return HttpResponseRedirect('manager/main')
    else:
        return HttpResponse('登录失败')
    #登录成功后的后台主页
def main(request):
    #记录当前商家ID
    manager_id= request.session['manager_id']
    # #找到对应ID商家下的货品数量
    goods_count = GoodsInfor.objects.filter(manager_id= manager_id).count()
    #后台主页显示会员数
    user_count = OrderDetails.objects.select_related('Order').filter(manager_id=manager_id).count()
    goods = GoodsInfor.objects.filter(manager_id= manager_id,goods_count__lte=50).count()
    #将获取到的该商家的货品数量传到前台页面
    return render(request,'manager/houtai.html',{'goods_count':goods_count,'goods':goods,'user_count':user_count})
#卖家管理后台的注销
def loginout(request):
    #清除商家登录的信息
    del request.session['manager_id']
    del request.session['managername']
    return HttpResponseRedirect('/manager/denglu')
#卖家注册
def zhuce(request):
    return render(request,'manager/zhuce.html')
#卖家注册
def zhucedo(request):
    #获取表单提交的数据
    username = request.POST['username']
    nicheng = request.POST['nicheng']
    shop_name = request.POST['shop_name']
    shop_logo = request.FILES['shop_logo']
    address = request.POST['address']
    #自定义商店图标得保存路径 static/media/uploads
    save_path = "%s/media/uploads/%s"%(settings.MEDIA_ROOT,shop_logo.name)
    with open(save_path,'wb') as f:
        for content in shop_logo.chunks():
            f.write(content)
    #判断用户名是否存在
    user = ManagerLogin.objects.filter(username=username)
    if user:
        return HttpResponse('用户名已存在')
    else:
        # 店铺登陆得初始密码是‘000000’
        userpass = '000000'
        result = ManagerLogin.objects.create(shop_logo=shop_logo,
                                             username=username,
                                             userpass=userpass,
                                             nicheng=nicheng,
                                             shop_name=shop_name,
                                             shop_address=address, )
        if result:
            request.session['managername'] = username
            return HttpResponseRedirect('manager/denglu')
        else:
            return HttpResponse('注册失败')
#修改密码
def updatepass(request):
    list = ManagerLogin.objects.order_by('manager_id')
    # return HttpResponse(list)
    return render(request,'manager/updatepass.html',{'list':list})
def updatepsdo(request):
    # userypass = request.POST['userypass']
    # userpass = request.POST['userpass']
    # user_id = request.POST['id']
    # #通过ID和判断是否为原密码来更改密码
    # user = ManagerLogin.objects.filter(manager_id=user_id,userpass=userypass).update(userpass=userpass)
    # if user:
    #     return HttpResponseRedirect('manager/main')
    # else:
    #     return HttpResponse('修改失败')
    #使用ajax来写
    manager_id = request.session['manager_id']
    manager = ManagerLogin.objects.filter(manager_id=manager_id).get()
    userypass = manager.userpass
    if request.is_ajax():
        data = json.loads(request.body.decode('utf8'))
        usepass = data.get('userypass')
        userpass = data.get('userpass')
        userqrpass = data.get('userqrpass')
        if usepass != userypass:
            return HttpResponse(json.dumps(1))
        elif userpass == userypass:
            return HttpResponse(json.dumps(2))
        else:
            result = ManagerLogin.objects.filter(manager_id=manager_id).update(userpass=userpass)
            if result:
                return HttpResponse(json.dumps(3))
#卖家修改商品类型
def xiugaitype(request):
    list = GoodsType.objects.order_by('-type_id')
    return render(request,'manager/xiugaitype.html',{'list':list})
#删除商品类型
def type_del(request,pk):
    list =GoodsType.objects.get(pk=pk)
    result = list.delete()
    if result:
        return HttpResponseRedirect('manager/xiugaitype')
    else:
        return HttpResponse('删除失败')
#后台商品类型编辑操作
def typebj(request,pk):
    list = GoodsType.objects.get(pk=pk)
    return render(request,"manager/typebj.html",{'list':list})
def typebjdo(request):
    type_name = request.POST['type_name']
    type_sort = request.POST['type_sort']
    type_id =request.POST['id']
    result = GoodsType.objects.filter(type_id=type_id).update(type_name=type_name,type_sort=type_sort)
    if result:
        return HttpResponseRedirect('manager/xiugaitype')
    else:
        return HttpResponse('修改失败')
#后台商品类型增加操作
def typeadd(request):
    #只获取type_id列
    list = GoodsType.objects.all().values('type_id')
    return render(request,'manager/typeadd.html',{'list':list})
def tpadddoo(request):
    type_name = request.POST['type_name']
    type_sort = request.POST['type_sort']
    # type_id = request.POST['type_id']
    result = GoodsType.objects.create(type_name=type_name,type_sort=type_sort)
    # result = GoodsType.objects.create(type_name=type_name, type_id=type_id)
    # cursor = connection.cursor()
    # result = cursor.execute("insert into goods_goodstype(type_name,type_sort) values("+type_name+','+type_sort+')')
    # result = GoodsType.objects.raw("insert into goods_goodstype(type_name,type_sort) values("+type_name+','+type_sort+')')

    if result:
        # return HttpResponse(type_name+","+type_sort+","+type_id)
        return HttpResponseRedirect('manager/xiugaitype')
    else:
        return HttpResponse('增加失败')
#订单列表
def dingdanlist(request):
    manager_id =request.session['manager_id']
    # return HttpResponse(manager_id)
    # sql = " select * from cart_order where order_id  in " \
    #       "(select order_id from cart_orderdetails where manager_id ="+manager_id+");"
    sql = "select distinct cart_order.order_id,cart_order.order_num,cart_order.order_time,cart_order.order_status" \
          " from cart_order left join cart_orderdetails on cart_order.order_id=cart_orderdetails.order_id" \
          " where cart_orderdetails.manager_id="+str(manager_id)
    list = Order.objects.raw(sql)
    sum_shouru = OrderDetails.objects.filter(manager_id=manager_id).aggregate(total=Sum('goods_xiaoji'))
    # return HttpResponse(list)
    return render(request,'manager/dingdanlist.html',{'list':list,'sum_shouru':sum_shouru})
def dingdanxq(request,pk,aid):
    manager_id = request.session['manager_id']
    # sql = "select * from cart_order inner join cart_orderdetails on cart_order.order_id=cart_orderdetails.order_id" \
    #       " inner join cart_goodsaddress on cart_order.address_id=cart_goodsaddress.address_id where cart_order.order_id ="+ str(pk) +" and manager_id ="+str(manager_id)
    # list = OrderDetails.objects.raw(sql)
    #通过商家ID和前台页面传过来的订单ID来查询该订单详情
    order = OrderDetails.objects.filter(manager_id=manager_id,order_id=pk).all()
    #通过前台页面传递过来的该订单的地址来查询该订单的地址详情
    address_list = GoodsAddress.objects.filter(address_id=aid).get()
    return render(request,'manager/dingdanxq.html',{'address_list':address_list,'order_id':pk,'order':order})
#后台点击发货，更改状态值
def updatestatus(requset):
    manager_id = requset.session.get('manager_id')
    pk = requset.POST['order_id']
    details_id = requset.POST['details_id']
    # #获取订单详情的信息
    # orderdetails = OrderDetails.objects.filter(details_id=details_id).all()
    # return HttpResponse(orderdetails.details_id)
    status = Order.objects.filter(order_id=pk).get()
    if status.order_status == 1:
        result =Order.objects.filter(order_id=pk).update(order_status=2)
        OrderDetails.objects.filter(manager_id=manager_id,order_id=pk).update(order_status=1)
        if result:
            return HttpResponseRedirect('/manager/dingdanlist')
        else:
            return HttpResponse('发货失败')
    elif status.order_status == 3 :
        return HttpResponse('无法操作，该订单已结束')
    else:
        return HttpResponse('无法操作，请等待买家付款后再进行操作')
#评论管理列表
def pinglunlist(request):
    manager_id = request.session['manager_id']
    sql = "select goods_goodscontent.content_id," \
          "goods_goodscontent.comment_content," \
          "goods_goodscontent.comment_time," \
          "users_userb.username,goods_goodsinfor.goods_name,users_userb.user_pic" \
          " from goods_goodscontent inner join users_userb on goods_goodscontent.user_id = users_userb.user_id  " \
          "inner join goods_goodsinfor on goods_goodscontent.goods_id = goods_goodsinfor.id where goods_goodscontent.manager_id="+str(manager_id)
    list = GoodsContent.objects.raw(sql)
    return render(request,'manager/pinglunlist.html',{"list":list})
#查看评论的内容
def chakan_pinglun(request,pk):
    # return HttpResponse(pk)
    #查看该评论表信息
    content = GoodsContent.objects.filter(content_id=pk).get()
    return render(request,'manager/pinglun.html',{'content':content})
#待补货数
def goodsless(request):
    manager_id = request.session['manager_id']
# '''
#             获取制定范围的数据
#             __gt 大于
#             __gte 大于等于
#             __lt 小于
#             __lte 小于等于
#             用法：在检索查询时，字段名后跟上检索条件，例如：Goodsinfor.objects.filter(goods_num__lt=50).all()
# '''
    goods = GoodsInfor.objects.filter(goods_count__lte=50,manager_id=manager_id).all()
    return render(request,'manager/goodsless.html',{'goods':goods})
#补充货源
def goodsbuchong(request,gid):
    return render(request,'manager/buchonghuoyuan.html',{'goods_id':gid})
def buchongdo(request):
    if request.is_ajax():
        data = json.loads(request.body.decode('utf8'))
        goods_count = data.get('goods_count')
        goods_id = data.get('goods_id')
        goods = GoodsInfor.objects.filter(id=goods_id).get()
        goods.goods_count = int(goods.goods_count)+int(goods_count)
        goods.save()
        return HttpResponse(json.dumps(1))




