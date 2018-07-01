from django.shortcuts import render
from .models import Student
from django.http import HttpResponse,HttpResponseRedirect
import json
# Create your views here.
#系统主页
def index(request):
    list = Student.objects.all()
    return render(request,'student/index.html',{'list':list})
#增加学员
def add(request):
    student = Student.objects.all()
    if request.is_ajax():
        data = json.loads(request.body.decode('utf8'))
        xuehao = data.get('xuehao')
        stuname = data.get('stuname')
        stusex = data.get('stusex')
        age = data.get('age')
        grade = data.get('grade')
        zhuanye = data.get('zhuanye')
        address = data.get('address')
        stu_id = data.get('stu_id')
        a = Student.objects.filter(stu_id=stu_id).get()
        xuehao1 = a.xuehao

        if xuehao1 == xuehao:
            return HttpResponse(json.dumps(2))
        else:
            stu = Student.objects.create(
                xuehao=xuehao,
                stuname=stuname,
                stusex=stusex,
                age=age,
                grade=grade,
                zhuanye=zhuanye,
                address=address
            )
            if stu:
                return HttpResponse(json.dumps(1))
    return render(request,'student/add.html',{"student":student})
#删除学员
def shanchu(request):
    if request.is_ajax():
        data = json.loads(request.body.decode('utf8'))
        stu_id = data.get('stu_id')
        stu = Student.objects.filter(stu_id=stu_id).delete()
        if stu:
            return HttpResponse(json.dumps(1))
#修改信息
def xiugai (request,sid):
    student = Student.objects.filter(stu_id=sid).get()
    return render(request,'student/xiugai.html',{'student':student})
def xiugaido(request):
    if request.is_ajax():
        data = json.loads(request.body.decode('utf8'))
        xuehao = data.get('xuehao')
        stuname = data.get('stuname')
        stusex = data.get('stusex')
        age = data.get('age')
        grade = data.get('grade')
        zhuanye = data.get('zhuanye')
        address = data.get('address')
        stu_id = data.get('stu_id')
        stu = Student.objects.filter(stu_id=stu_id).update(
            xuehao=xuehao,
            stuname=stuname,
            stusex=stusex,
            age=age,
            grade=grade,
            zhuanye=zhuanye,
            address=address
        )
        if stu:
            return HttpResponse(json.dumps(1))

