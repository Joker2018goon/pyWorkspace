# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "hi/index.html")


# 登录
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            response= HttpResponseRedirect('/hi/event_manage/')
            # 添加浏览器的coolkie,添加用户
            # response.set_cookie('user',username,3600)
            # 将session信息记录到浏览器中
            request.session['user']=username
            return response
        else:
            return render(request, "hi/index.html", {'error': 'username or password worng'})

#登录成功后管理页面
@login_required # 限制该视图必须登录才能访问
def event_manage(request):
    # 从cookie中拿到user的value
    # username=request.COOKIES.get('user','')
    # 读取浏览器中的session
    username=request.session.get('get','')
    return render(request,'hi/event_manage.html',{'user':username})