from django.http import HttpResponse
#编写视图处理函数，一个函数相当于是一个视图
def run_views(request):
    #request主要封装了的是请求的信息
    return HttpResponse('<h1>这是我的第一个DJANGO程序</h1>')