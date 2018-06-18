from django.shortcuts import render
from .models import Student
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def add(request):
    return render(request, 'student/add.html')
def ado(request):
    stu_id= request.POST ['stu_id']
    username= request.POST['username']
    sex= request.POST ['sex']
    age= request.POST ['age']
    nianji= request.POST ['nianji']
    zhuanye= request.POST ['zhuanye']
    address= request.POST ['address']
    result = Student.objects.create(stu_id=stu_id,username=username,sex=sex,age=age,nianji=nianji,zhuanye=zhuanye,address=address)
    if result:
        return HttpResponseRedirect('stu/xs')
    else:
        return HttpResponse('操作失败')
def xs(request):
    list = Student.objects.order_by('-id')
    return render(request, 'student/xianshi.html', {'list': list})
def shanchu(request,pk):
    list = Student.objects.get(pk=pk)
    result = list.delete()
    if result:
        return HttpResponseRedirect('stu/xs')
    else:
        return HttpResponse('操作失败')
def xiugai(request,pk):
    list = Student.objects.get(pk=pk)
    return render(request, 'student/xiugai.html', {'list': list})
def xiugaido(request):
    stu_id = request.POST['stu_id']
    username = request.POST['username']
    sex = request.POST['sex']
    age = request.POST['age']
    nianji = request.POST['nianji']
    zhuanye = request.POST['zhuanye']
    address = request.POST['address']
    id = request.POST['id']
    result = Student.objects.filter(id=id).update(stu_id=stu_id, username=username, sex=sex, age=age, nianji=nianji, zhuanye=zhuanye,
                                    address=address)
    if result:
        return HttpResponseRedirect('stu/xs')
    else:
        return HttpResponse('操作失败')