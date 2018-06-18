from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import BlogArticle
from datetime import datetime
# Create your views here.
# def hello(request):
#     return HttpResponse('hello world')
# def test(request):
#     return render(request,'index.html')
def add(request):
    return render(request,'add.html')
def ado(request):
    #第一：先收集数据
    title = request.POST['title']
    autor = request.POST['autor']
    content = request.POST['content']
    add_time=datetime.now()
    #第二：添加数据
    result= BlogArticle.objects.create(title=title,autor=autor,content=content,add_time=add_time)
    #第三：判断是否添加成功
    if result:
        #如果添加成功的话，跳转页面，跳转到boke 下的 xs
        return HttpResponseRedirect('boke/xs')
    else:
        return HttpResponse('数据添加失败')
def xs(request):
    # 获取数据
    list=BlogArticle.objects.order_by('-id')
    return render(request,'xianshi.html',{'list':list})
def xq(request,pk):
    article = BlogArticle.objects.get(pk=pk)
    return render(request,'xiangqingye.html',{'article':article})
def shanchu(request,pk):
    list = BlogArticle.objects.get(pk=pk)
    result=list.delete()
    if result:
        return HttpResponseRedirect('boke/xs')
    else:
        return HttpResponse('删除数据失败')
def bianji(request,pk):
    list = BlogArticle.objects.get(pk=pk)
    return render(request,'xiugai.html',{'list':list})
def xiugaido(request):
    title = request.POST['title']
    autor = request.POST['autor']
    content = request.POST['content']
    add_time = datetime.now()
    id=request.POST['id']
    result =BlogArticle.objects.filter(id=id).update(title=title,autor=autor,content=content,add_time=add_time)
    if result:
        return HttpResponseRedirect('boke/xs')
    else:
        return HttpResponse('数据修改失败')
