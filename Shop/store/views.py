from django.shortcuts import render
from goods.models import GoodsInfor,GoodsType
from manager.models import ManagerLogin
# Create your views here.
#店铺详情
def storedetails(request,pk):
    list =GoodsInfor.objects.filter(manager_id=pk).all()
    type = GoodsType.objects.all()
    return render(request,'store/storedetails.html',{"list":list,"type":type})
def store_goodstype(request,pk):
    #获取商品类型
    type = GoodsType.objects.all()
    #根据类型ID来显示商品信息
    list = GoodsInfor.objects.filter(type_id=pk).all()
    return render(request,'store/goodstype.html',{'type':type,'list':list})
#进入店铺主页
def store(request):
    list = ManagerLogin.objects.all()
    return render(request,'store/storeindex.html',{'list':list})
