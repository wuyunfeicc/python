from django.shortcuts import render
from cart.models import CartMessage,GoodsAddress,Order,OrderDetails
from django.http import HttpResponseRedirect,HttpResponse
from django.db.models import Sum
from django.utils import timezone
import random
from datetime import datetime
# Create your views here.
def cart_add(request):
    #记录前台用户的用户ID
    username = request.session.get('user_id')
    # return HttpResponse(username)
    # 判断前台用户是否登录
    # 没登录
    if username==None:
        return HttpResponseRedirect('users/denglu')
    #登录
    else:
        #收集表单提交的数据
        gname = request.POST['gname']
        gxprice = request.POST['gxprice']
        gpic = request.POST['gpic']
        manager_id = request.POST['manager_id']
        goods_id = request.POST['goods_id']
        user_id = request.session['user_id']
        goods_num = request.POST['count']
        xiaoji =float(gxprice)*float(goods_num)
        #return HttpResponse(user_id)
        # 查看购物车中当前商品id的商品的数量
        count = CartMessage.objects.filter(goods_id=goods_id,user_id=user_id,manager_id=manager_id).count()
        if count > 0:
            message = CartMessage.objects.get(goods_id=goods_id,user_id=user_id)
            message.goods_num = int(goods_num)+int(message.goods_num)
            message.goods_xiaoji = message.goods_xprice*message.goods_num
            message.save()
        else:
            #如果购物车中没有该商品则将数据添加进表
            CartMessage.objects.create(goods_name=gname,
                                       goods_xprice=gxprice,
                                       goods_pic=gpic,
                                       manager_id=manager_id,
                                       goods_id=goods_id,
                                       user_id=user_id,
                                       goods_xiaoji=xiaoji,
                                       goods_num=goods_num)
    return HttpResponseRedirect('/cart/gouwuche')
#购物车
def gouwuche(request):
    #获取当前用户名称
    username = request.session.get('username')
    if username==None:
        # return HttpResponse(1)
        return HttpResponseRedirect('users/denglu')
    else:
        #获取当前用户的ID
        user_id = request.session['user_id']
        #获取当前用户数据库中购物车中的所有信息
        cartlist = CartMessage.objects.filter(user_id=user_id).all()
        #获取当前用户购物车中所有商品的总价
        sum_score = cartlist.aggregate(total=Sum('goods_xiaoji'))
        # return HttpResponse(sum_score)
        return render(request,'cart/gouwuche.html',{'cartlist':cartlist,'sum_score':sum_score})
    #购物车清空
def cart_delate(request,pk):
    list = CartMessage.objects.get(cart_id=pk)
    # return HttpResponse(list)
    list.delete()
    return HttpResponseRedirect('cart/gouwuche')
#增加数量在购物车页面
def jiacount(request,pk,user_id):
    #通过传递过来的商品ID值来查询购物车中的该商品的所有信息
    cart = CartMessage.objects.get(goods_id=pk,user_id=user_id)
    cart.goods_num = cart.goods_num + 1
    cart.goods_xiaoji=cart.goods_num*cart.goods_xprice
    cart.save()
    # return HttpResponse(cart)
    return HttpResponseRedirect('cart/gouwuche')
#在购物车界面减少数量
def jiancount(request,pk,user_id):
    cart = CartMessage.objects.get(goods_id=pk,user_id=user_id)
    # return HttpResponse(pk+','+num)
    if cart.goods_num==1:
        cart.goods_num=1
    else:
        cart.goods_num = cart.goods_num-1
        cart.goods_xiaoji = cart.goods_num * cart.goods_xprice
        cart.save()
        return HttpResponseRedirect('cart/gouwuche')
    #清空购物车
def clearcart(request):
    user_id = request.session.get('user_id')
    list = CartMessage.objects.filter(user_id=user_id).all()
    list.delete()
    return HttpResponseRedirect('cart/gouwuche')
#下订单
def xiadan(request):
    #获取当前用户ID
    user_id = request.session.get('user_id')
    #获取当前用户购物车中的商品数量
    count = CartMessage.objects.filter(user_id=user_id).count()
    #判断数量。空的话去添加，不能继续下单
    if count == 0:
        return HttpResponse('请先将物品加入购物车中。。谢谢！！')
    else:
        list = CartMessage.objects.filter(user_id=user_id).all()
        list1 = GoodsAddress.objects.filter(user_id=user_id).all()
        # cartlist = CartMessage.objects.filter(user_id=user_id).all()
        sum_score = list.aggregate(total=Sum('goods_xiaoji'))
        return render(request,'cart/dingdan.html',{'list':list,'list1':list1,'sum_score':sum_score})
#提交订单，进入到订单详情页面
def addorder(request):
    user_id = request.session.get('user_id')
    # return HttpResponse(user_id)
    #判断是否登录
    if user_id==None:
        return HttpResponseRedirect('users/denglu')
    else:
        address_id = request.POST.get('address_id')
        if address_id==None:
            return HttpResponseRedirect('cart/address_shouhuo')
        # return HttpResponse(address_id)
        # #订单状态 1代表未付款 2代表未发货 3代表收货 4代表已评价
        else:
            address_id = request.POST['address_id']
            order_status = 1
            # 订单编号，通过当前时间和随机数字组合而成
            order_num = timezone.now().strftime("%Y%m%d%H%M%S") + str(random.randint(10000, 99999))
            # 下单时间
            order_time = datetime.now()
            # 订单总价
            total = request.POST['total']
            #用户ID
            user_id = user_id
            #通过订单表单提交的数据将数据添加到订单表中
            result = Order.objects.create(address_id=address_id,
                                          order_num=order_num,
                                          order_status=order_status,
                                          order_time=order_time,
                                          total=total,
                                          user_id=user_id)
            if result:
                return HttpResponseRedirect('cart/orderdetails')
            else:
                return HttpResponse('添加失败')
#新增收货地址
def address_shouhuo(request):
    return render(request,'cart/shouhuo.html')
def address_shdo(request):
    uname = request.POST['uname']
    phone = request.POST['phone']
    address = request.POST['address']
    user_id = request.session['user_id']
    result = GoodsAddress.objects.create(uname=uname,phone=phone,address=address,user_id=user_id)
    if result:
        return HttpResponseRedirect('cart/xiadan')
    else:
        return HttpResponse('添加失败')
#订单详情
def orderdetails(request):
    user_id = request.session.get('user_id')
    if user_id == None:
        return HttpResponseRedirect('/users/denglu')
    else:
        order = Order.objects.filter(user_id=user_id).last()
        order_id = order.order_id
        cart = CartMessage.objects.filter(user_id=user_id).all()
        for i in cart:
            details = OrderDetails.objects.create(
                        order_id = order_id,
                        manager_id = i.manager_id,
                        goods_id = i.goods_id,
                        goods_name = i.goods_name,
                        goods_pic = i.goods_pic,
                        goods_price= i.goods_xprice,
                        goods_num= i.goods_num,
                        goods_xiaoji = i.goods_xiaoji
            )
        if details:
            #清空购物车
            message = CartMessage.objects.filter(user_id=user_id).all()
            message.delete()
            # return HttpResponse("恭喜您下单成功")
            return HttpResponseRedirect('/cart/successful')
        else:
            return HttpResponse("下单失败")
def successful(request):
    user_id = request.session['user_id']
    #根据当前ID查询订单
    list = Order.objects.filter(user_id=user_id).last()
    return render(request,'cart/successful.html',{'list':list})



