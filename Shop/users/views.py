from django.shortcuts import render
from .models import UserB,UserEmail
from goods.models import GoodsInfor,GoodsContent
from django.http import HttpResponseRedirect,HttpResponse
from datetime import datetime
from cart.models import GoodsAddress
from django.db.models import Sum
from cart.models import Order,OrderDetails
from django.conf import settings
import json
from cart.models import OrderDetails
from django.core.mail import send_mail
# Create your views here.
def zhuce(request):
    return render(request,'user/zhuce.html')
def zcdo(request):
    #收集表单提交的数据
    username = request.POST['username']
    userpass = request.POST['userpass']
    querenps = request.POST['querenps']
    add_time = datetime.now()
    user_pic = request.FILES['user_pic']
    user_email = request.POST['user_email']
    #自定义图片的保存路径
    save_path = '%s/media/uploads/%s'% (settings.MEDIA_ROOT, user_pic.name)
    with open(save_path, 'wb') as f:
        for content in user_pic.chunks():
            f.write(content)
    #判断用户名是否存在
    user = UserB.objects.filter(username=username)
    # 判断用户名是否存在
    if user:
        return HttpResponse('注册失败，用户名已存在')
    else:
        if userpass==querenps:
            # 创建表数据
            UserB.objects.create(username=username, userpass=userpass, add_time=add_time,
                                 user_pic='media/uploads/%s' % user_pic.name, user_email=user_email)
            # 获取当前账户的id
            user_id = UserB.objects.get(username=username, userpass=userpass).user_id
            username = UserB.objects.get(username=username, userpass=userpass).username
            # 记录当前账户的用户名和ID
            request.session['username'] = username
            request.session['user_id'] = user_id
            return HttpResponseRedirect('/users/fasong_mail')
        else:
            return HttpResponse('注册失败')
def denglu(request):
    return render(request,'user/denglu.html')
def dldo(request):
    #获取页面数据
        username = request.POST['username']
        userpass = request.POST['userpass']
        users = UserB.objects.filter(username=username, userpass=userpass)
        #判断用户名，密码是否符合
        if users:
            # 获取当前账户的id
            user_id = UserB.objects.get(username=username, userpass=userpass).user_id
            #记录当前账户的用户名和ID
            request.session['username']=username
            request.session['user_id']=user_id
            # return HttpResponse(user_id)
            return HttpResponseRedirect('users/index')
        else:
            return HttpResponse('登录失败')
def index(request):
    #获取商品的所有信息
    sql = "select goods_pic,goods_name,goods_xprice,id,manager_managerlogin.manager_id,shop_name from goods_goodsinfor" \
          " inner join manager_managerlogin on goods_goodsinfor.manager_id=manager_managerlogin.manager_id group by manager_managerlogin.manager_id limit 10"
    list = GoodsInfor.objects.raw(sql)
    return render(request,'goods_ye/goods_index.html',{'list':list})
def tuichu(request):
    #判断是否登录
    username = request.session.get('username')
    if username!=None:
        del request.session['username']
        del request.session['user_id']
        return HttpResponseRedirect('users/denglu')
    else:
        return HttpResponse('未登陆')
#会员中心
def user_center(request):
    user_id = request.session.get('user_id')
    if user_id == None:
        return HttpResponseRedirect('/users/denglu')
    else:
        #通过uesr_id获取订单表中的信息
        list = Order.objects.filter(user_id=user_id).all()
        #获取订单详情表中的信息
        list1 = OrderDetails.objects.all()
        return render(request,'user/user_center.html',{'list':list,"list1":list1})
def userupdateps(request):
    return render(request,'user/userupdateps.html')
def updatepsdo(request):
    # user_id = request.session.get('user_id')
    # userpass = request.POST['userpass']
    # userxpass = request.POST['userxpass']
    # user = UserB.objects.filter(user_id=user_id,userpass=userpass).update(userpass=userxpass)
    # if user:
    #     return HttpResponseRedirect('/users/user_center')
    # 通过AJAX来判断表单的内容是否符合规定
    user_id = request.session['user_id']
    user = UserB.objects.filter(user_id=user_id).get()
    userpass = user.userpass
    if request.is_ajax():
        # json.loads将已编码的JSON字符串解码为PYTHON 对象 JSON.LOAD（）加载一个字符串
        data = json.loads(request.body.decode('utf8'))
        use_pass = data.get('userpass')
        userxpass = data.get('userxpass')
        userqrpass = data.get('userqrpass')
        if use_pass!=userpass:
            return HttpResponse(json.dumps(1))
        elif use_pass == userxpass:
            return HttpResponse(json.dumps(2))
        else:
            result = UserB.objects.filter(user_id=user_id).update(userpass=userxpass)
            if result:
                return HttpResponse(json.dumps(3))
def qrshouhuo(request,pk,did,num,gid):
    #确认收货，获取当前订单状态值
    status = Order.objects.filter(order_id=pk).get()
    if status.order_status == 2 :
        result = Order.objects.filter(order_id=pk).update(order_status=3)
        OrderDetails.objects.filter(details_id=did).update(order_status=2)
        if result:
            #获取该商品库存值，当确认收货后，在数据库中减去该值
            goods = GoodsInfor.objects.filter(id=gid).get()
            goods.goods_count=int(goods.goods_count)-int(num)
            goods.save()
            return HttpResponseRedirect('/users/user_center')
        else:
            return HttpResponse('出现状况了 ╯﹏╰ 粉无奈~~，请重新确认')
    # elif status.order_status ==3:
    #     return HttpResponseRedirect('users/pingjia')
    elif status.order_status == 3:
        OrderDetails.objects.filter(details_id=did).update(order_status=2)
        return HttpResponseRedirect('/users/user_center')
    elif status.order_status == 4:
        OrderDetails.objects.filter(details_id=did).update(order_status=2)
        return HttpResponseRedirect('/users/user_center')
    else:
        return HttpResponse('错误操作')
    #评价
def pingjia(request,pk,did):
    #当前订单的详细信息，通过订单详情中的主键
    sql = "select * from cart_orderdetails join cart_order on cart_order.order_id=cart_orderdetails.order_id " \
          "where cart_orderdetails.details_id="+str(did)
    order = OrderDetails.objects.raw(sql)
    return render(request,'goods/pingjia.html',{'order':order})
#执行评价的操作
def pingjiado(request):
    comment_content = request.POST['comment_content']
    user_id = request.POST['user_id']
    manager_id = request.POST['manager_id']
    # return HttpResponse(manager_id)
    details_id=request.POST['details_id']
    goods_id = request.POST['goods_id']
    order_id = request.POST['order_id']
    result = GoodsContent.objects.create(
        comment_content=comment_content,
        user_id=user_id,
        manager_id=manager_id,
        goods_id = goods_id
    )
    if result:
        Order.objects.filter(order_id=order_id).update(order_status=4)
        OrderDetails.objects.filter(details_id = details_id).update(order_status=3)
        return HttpResponseRedirect('/users/user_center')
    else:
        return HttpResponse('评价失败')
#查看订单详情
def dingdanxq(request,pk,did):
    details = OrderDetails.objects.filter(details_id=did).get()
    details_id = details.details_id
    order = Order.objects.filter(order_id=pk).get()
    address_id = order.address_id
    address = GoodsAddress.objects.filter(address_id=address_id).get()
    list = OrderDetails.objects.filter(order_id=pk).all()
    total = OrderDetails.objects.filter(order_id=pk).aggregate(total=Sum('goods_xiaoji'))
    details = OrderDetails.objects.filter(details_id=details_id).get()
    return render(request,'user/dingdanxq.html',{'address':address,'order':order,'list':list,'total':total,'details':details})

#收货地址
def shouhuo(request):
    user_id = request.session['user_id']
    address = GoodsAddress.objects.filter(user_id=user_id).all()
    return render(request,'user/shouhuo.html',{'address':address})
#添加收货地址
def tjaddress(request):
    return render(request,'user/tianjiashouhuo.html')
def tianjiadizhido(request):
    user_id = request.session['user_id']
    if request.is_ajax():
        data = json.loads(request.body.decode('utf8'))
        uname = data.get('uname')
        address = data.get('address')
        phone = data.get('phone')
        result = GoodsAddress.objects.create(
            uname=uname,
            address=address,
            phone=phone,
            user_id=user_id
        )
        if result:
            return HttpResponse(json.dumps(1))
#删除地址
def delatedizhi(request):
    if request.is_ajax():
        data = json.loads(request.body.decode('utf8'))
        address_id = data.get('address_id')
        result = GoodsAddress.objects.filter(address_id=address_id).delete()
        if result:
            return HttpResponse(json.dumps(1))
#编辑地址
def bianjiaddress(request,aid):
    address = GoodsAddress.objects.filter(address_id=aid).get()
    return render(request,'user/bianjidizhi.html',{"address":address})
def bianjidizhido(request):
    if request.is_ajax():
        data = json.loads(request.body.decode('utf8'))
        uname = data.get('uname')
        address = data.get('address')
        phone = data.get('phone')
        address_id = data.get('address_id')
        result = GoodsAddress.objects.filter(address_id=address_id).update(
            uname=uname,
            address=address,
            phone=phone,
        )
        if result:
            return HttpResponse(json.dumps(1))
#会员列表
def uservip(request):
    manager_id = request.session['manager_id']
    sql = "select * from users_userb inner join cart_order on cart_order.user_id = users_userb.user_id " \
          "inner join cart_orderdetails on cart_orderdetails.order_id = cart_order.order_id where cart_orderdetails.manager_id="\
          +str(manager_id)+" group by cart_order.user_id"
    list = OrderDetails.objects.raw(sql)
    return render(request,'user/uservip.html',{'list':list})
def chakanpay(request,uid):
    #通过会员ID来查询订单编号，下单时间
    manager_id = request.session['manager_id']
    sql ="SELECT users_userb.user_id,cart_order.user_id,cart_order.order_num,cart_order.order_id,cart_orderdetails.details_id," \
         "cart_orderdetails.manager_id,cart_orderdetails.order_id,cart_orderdetails.goods_xiaoji" \
         " FROM users_userb INNER JOIN cart_order ON cart_order.user_id = users_userb.user_id " \
         "INNER JOIN cart_orderdetails ON cart_orderdetails.order_id = cart_order.order_id " \
         "where cart_orderdetails.manager_id="+str(manager_id)+" and cart_order.user_id="+str(uid)+" and cart_order.order_status=4 group by order_num"
    list = Order.objects.raw(sql)
    return render(request,'user/chakanpay.html',{'list':list})
#查看订单编号详情
def chakanxq(request,oid):
    manager_id = request.session['manager_id']
    list = OrderDetails.objects.filter(order_id=oid,manager_id=manager_id).all()
    sum_score = list.aggregate(total = Sum('goods_xiaoji'))
    return render(request,'user/dingdanpianhao.html',{'list':list,'sum_score':sum_score})
#发送邮件
def fasong_mail(request):
    user = UserB.objects.last()
    email = user.user_email
    id = user.user_id
    time = datetime.now()
    result = send_mail('全球生鲜商城欢迎您',
              '会员您好，欢迎注册全球生鲜商城，希望您购物愉快！！',
              'wuyunfei199205@163.com',[email],fail_silently=True)
    if result:
        UserEmail.objects.create(user_id=id,mail_time = time,
                                title='全球生鲜商城欢迎您',
                                body='会员您好，欢迎注册全球生鲜商城，希望您购物愉快！！')
        return HttpResponseRedirect('/users/chakanemail')
#查看邮件
def chakanemail(request):
    return render(request,'user/chakanemail.html')
