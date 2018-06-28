from django.shortcuts import render
from .models import GoodsInfor,GoodsType,ManagerLogin,GoodsContent,UserB
from django.http import HttpResponseRedirect,HttpResponse
from django.conf import settings
# Create your views here.
def goods_list(request):
    # list = GoodsInfor.objects.raw("select * from goods_goodsinfor,goods_goodstype where goods_goodsinfor.type_id=goods_goodstype.type_id")
    id = str(request.session['manager_id'])
    sql='select * from goods_goodstype inner join goods_goodsinfor on goods_goodstype.type_id=' \
        'goods_goodsinfor.type_id where goods_goodsinfor.manager_id='+id
    list = GoodsInfor.objects.raw(sql)
    return render(request, 'goods/goods_list.html', {'list': list})
def goods_add(request):
    goods_type = GoodsType.objects.order_by('-type_id')
    return render(request,'goods/goods_add.html',{'goods_type':goods_type})
def goods_adddo(request):
    goods_num = request.POST['goods_num']
    goods_name = request.POST['goods_name']
    goods_oprice = request.POST['goods_oprice']
    goods_xprice = request.POST['goods_xprice']
    goods_infor = request.POST['goods_infor']
    goods_method = request.POST['goods_method']
    goods_count = request.POST['goods_count']
    goods_address = request.POST['goods_address']
    goods_content = request.POST['goods_content']
    # goods_pic = request.FILES.get('goods_pic')
    goods_pic = request.FILES['goods_pic']
    type_id = request.POST['type_id']
    #店铺ID
    manager_id = request.session['manager_id']
    #自定义保存路径
    save_path = '%s/media/uploads/%s'%(settings.MEDIA_ROOT,goods_pic.name)
    with open (save_path,'wb') as f:
        for content in goods_pic.chunks():
            f.write(content)
    result = GoodsInfor.objects.create(goods_num=goods_num,
                                       goods_name=goods_name,
                                       goods_oprice=goods_oprice,
                                       goods_xprice=goods_xprice,
                                       goods_infor=goods_infor,
                                       goods_method=goods_method,
                                       goods_count=goods_count,
                                       goods_address=goods_address,
                                       goods_content=goods_content,
                                       # goods_pic=goods_pic,
                                       goods_pic='media/uploads/%s'%goods_pic.name,
                                       type_id=type_id,
                                       manager_id=manager_id)
    if result:
        return HttpResponseRedirect('goods/goods_list')
    else:
        return HttpResponse('添加失败')
def goods_del(request,pk):
    list = GoodsInfor.objects.get(pk=pk)
    result = list.delete()
    if result:
        return HttpResponseRedirect('goods/goods_list')
    else:
        return HttpResponse('删除失败')
def goods_caozuo(request,pk):
    list = GoodsInfor.objects.get(pk=pk)
    goods_type = GoodsType.objects.order_by('-type_id')
    return render(request,'goods/goods_caozuo.html',{'list':list,"goods_type":goods_type})
def goods_caozuodo(request):
    goods_num = request.POST['goods_num']
    goods_name = request.POST['goods_name']
    goods_oprice = request.POST['goods_oprice']
    goods_xprice = request.POST['goods_xprice']
    goods_infor = request.POST['goods_infor']
    goods_method = request.POST['goods_method']
    goods_count = request.POST['goods_count']
    goods_address = request.POST['goods_address']
    goods_content = request.POST['goods_content']
    goods_pic = request.FILES['goods_pic']
    goods_id = request.POST['id']
    type_id = request.POST['type_id']
    #自定义图片得保存路径
    save_path = '%s/media/uploads/%s' % (settings.MEDIA_ROOT, goods_pic.name)
    with open(save_path,'wb') as f:
        for content in goods_pic.chunks():
            f.write(content)
    result = GoodsInfor.objects.filter(id = goods_id).update(goods_num=goods_num,
                                       goods_name=goods_name,
                                       goods_oprice=goods_oprice,
                                       goods_xprice=goods_xprice,
                                       goods_infor=goods_infor,
                                       goods_method=goods_method,
                                       goods_count=goods_count,
                                       goods_address=goods_address,
                                       goods_content=goods_content,
                                       goods_pic='media/uploads/%s' % goods_pic.name,
                                       type_id=type_id,)

    if result:
        return HttpResponseRedirect('goods/goods_list')
    else:
        return HttpResponse('修改失败')
def goods_type(request):
    list = GoodsType.objects.all()
    goods_list = GoodsInfor.objects.all()
    return render(request,'goods/goods_type.html',{'list':list,"goods_list":goods_list})
def type(request,pk):
    list = GoodsType.objects.all()
    list1 = GoodsInfor.objects.filter(type_id=pk).all()
    return render(request,"goods/goods_type1.html",{'list':list,'list1':list1})
def goods_xiangqing(request,pk):
    #单条数据查询
    shop = GoodsInfor.objects.filter(id=pk).get()
    # return HttpResponse(shop.goods_content)
    #取出当前商品的所在商家ID
    manager_id = shop.manager_id
    #查询当前商家里面除了本商品以为的其他商品并显示5条数据，后面的中括号相当于SQL语句中的limit(限制）
    list = GoodsInfor.objects.filter(manager_id=manager_id).exclude(id=pk).all()[0:5]
    #查询该商家信息 单条数据查询
    manager = ManagerLogin.objects.filter(manager_id=manager_id).get()
    #获取商品ID
    goods_id = shop.id
    # return HttpResponse(user_id)
    #获取评价的用户的信息
    sql = 'select * from goods_goodscontent inner join users_userb on goods_goodscontent.user_id=users_userb.user_id where goods_id='+str(goods_id)
    user = UserB.objects.raw(sql)
    #通过商家ID 用户ID 商品ID
    content = GoodsContent.objects.filter(goods_id=goods_id,manager_id=manager_id).all()
    return render(request,'goods/goods_xq.html',{'list':list,'shop':shop,'manager':manager,'content':content,'user':user})



