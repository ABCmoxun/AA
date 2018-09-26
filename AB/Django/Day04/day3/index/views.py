from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def add_views(request):
    # Method 1:
    # Author.objects.create(names='ZhuZiqing',age=65)

    # Method 2:
    # obj = Author(names='laoshe',age=68,email='laoshe@163.com')
    # obj.save()

    # Method 3:
    # dic = {
    #     'names':'MoYan',
    #     'age':59,
    #     'email':'moyan@163.com',
    # }
    # obj = Author(**dic)
    # obj.save()

    #Insert into Book Method 1:
    Book.objects.create(title='BeiYing',publicate_date='1995-10-15')
    #Insert into Book Method2 :
    book = Book(title='ChaGuan',publicate_date='1968-6-5')
    book.save()
    #Insert into Book Method3 :
    dic = {
        'title':'MuQin',
        'publicate_date':'1992-10-10',
    }
    obj = Book(**dic)
    obj.save()
    return HttpResponse('Add3 OK')


def query_views(request):
    # 查询Author实体中的所有信息: .all()
    # auList = Author.objects.all()
    # # print(auList)
    # for au in auList:
    #     print(au.names,",",au.age,",",au.email)


    #查询Author实体中names和age两个列的数据: .values()
    # auList = Author.objects.values('names','age')
    # print(auList)
    # for au in auList:
    #     print(au['names'],',',au['age'])

    #查询Author实体中names和age两个列的数据，
    #返回的数据是列表中封装的元组:.values_list()
    # auList = Author.objects.values_list('names','age')
    # print(auList)



    # 查询排序 : order_by()
    # auList = Author.objects.all().order_by('-age')
    # # print(auList)
    # for au in auList:
    #     print(au.id,",",au.names,",",au.age)


    #对条件取反 : exclude(条件)
    # auList = Author.objects.exclude(id=3)
    # for au in auList:
    #     print(au.id,",",au.names,",",au.age)

    #查询　names属性值中包含　'o' 的所有的记录
    auList = Author.objects.filter(names__contains='o')
    for au in auList:
        print(au.id,",",au.names,",",au.age)
    return HttpResponse('Query OK')


def aulist_views(request):
    auList = Author.objects.all()
    return render(request,'01_aulist.html',locals())

def delete_views(request,id):
    Author.objects.get(id=id).delete()
    return aulist_views(request)