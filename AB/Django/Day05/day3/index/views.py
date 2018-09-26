from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.db.models import F,Q

# Create your views here.
def add_views(request):
    # Method 1:
    Author.objects.create(names='ZhuZiqing',age=65)

    # Method 2:
    obj = Author(names='laoshe',age=68,email='laoshe@163.com')
    obj.save()

    # Method 3:
    dic = {
        'names':'MoYan',
        'age':59,
        'email':'moyan@163.com',
    }
    obj1 = Author(**dic)
    obj1.save()

    #Insert into Book Method 1:
    # Book.objects.create(title='BeiYing',publicate_date='1995-10-15')
    # #Insert into Book Method2 :
    # book = Book(title='ChaGuan',publicate_date='1968-6-5')
    # book.save()
    # #Insert into Book Method3 :
    # dic = {
    #     'title':'MuQin',
    #     'publicate_date':'1992-10-10',
    # }
    # obj = Book(**dic)
    # obj.save()
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
    auList = Author.objects.filter(isActive=True)
    return render(request,'01_aulist.html',locals())

def delete_views(request,id):
    # 以删除的方式删除数据
    # Author.objects.get(id=id).delete()
    # 以修改数据isActive状态值的方式来表示删除数据
    au = Author.objects.get(id=id)
    au.isActive = False
    au.save()
    # 转发
    # return aulist_views(request)

    # 重定向
    return HttpResponseRedirect('/03_aulist/')

def upshow_views(request,id):
    #根据id查询指定Author的信息
    au = Author.objects.get(id=id)
    return render(request,'02_update.html',locals())

def upage_views(request):
    #修改所有人的年龄，都＋１０岁
    Author.objects.all().update(age=F('age')+10)
    return HttpResponseRedirect('/03_aulist/')

def doQ_views(request):
    auList = Author.objects.filter(Q(id=6)|Q(age__gte=70),isActive=True)
    return render(request,'01_aulist.html',locals())

def raw_views(request):
    sql='select * from index_author where id>=8'
    auList = Author.objects.raw(sql)
    # print(auList)
    for au in auList:
        print(au.names,',',au.age)
    return HttpResponse('Execute raw success!')

def oto_views(request):
    # 正向查询：通过　wife 找　author
    #1.获取id为１的Wife的信息
    # wife = Wife.objects.get(id=1)
    #2.再获取wife对应的Author
    # author = wife.author

    # 反向查询：通过　author 找　wife
    # 1.获取　id 为14的author的信息
    author = Author.objects.get(id=14)
    # 2.再获取author对应的wife
    wife = author.wife

    return render(request,'03_oto.html',locals())