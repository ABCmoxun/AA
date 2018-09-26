from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def login_views(request):
    return render(request,'login.html')

def register_views(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        #接收用户的手机号,判断号码是否存在
        uphone = request.POST['uphone']
        users = Users.objects.filter(uphone=uphone)
        if users:
            #手机号已经注册过，给出提示，回到注册页面
            errMsg = '手机号码已经注册'
            return render(request,'register.html',locals())
        else:
            upwd = request.POST['upwd']
            uname = request.POST['uname']
            uemail = request.POST['uemail']

            Users.objects.create(uphone=uphone,
                upwd=upwd,uname=uname,uemail=uemail)
            return HttpResponse('注册成功!')
