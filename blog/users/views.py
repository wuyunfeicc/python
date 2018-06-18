from django.shortcuts import render
from .models import UserBiao
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def zhuce(request):
    return render(request,'users/zhuce.html')
def zcdo(request):
    usename = request.POST['usename']
    usepass = request.POST['usepass']
    age = request.POST['age']
    sex = request.POST['sex']
    hobby = request.POST.getlist('hobby')
    result = UserBiao.objects.create(usename=usename,usepass=usepass,age=age,sex=sex,hobby=hobby)
    if result:
        return HttpResponseRedirect('users/denglu')
    else:
        return HttpResponse('注册失败')
def denglu(request):
    return render(request,'users/denglu.html')
def dldo(request):
    usename = request.POST['usename']
    usepass = request.POST['usepass']
    users = UserBiao.objects.filter(usename=usename,usepass=usepass)
    if users:
        request.session['usename'] = usename
        return HttpResponseRedirect('users/index')
    else:
        return HttpResponse('登录失败')
def index(request):
    return render(request,'users/index.html')
def zhuxiao(request):
    del request.session['usename']
    return HttpResponseRedirect('users/index')

