# 10_keyword_arguments.py


def myfun(a, *, k):
    print('a =', a)
    print('k =', k)

# myfun(100, 200) # 错误
myfun(100, k=200)  # k强制使用关键字传参
myfun(10, **{'k': 20})  # 字典关键字传参


print('===================')


def myfun2(b, *args, c, d):
    print("b=", b)
    print("args=", args)
    print("c=", c)
    print("d=", d)

myfun2(100, 200, 300, 400, d=600, c=500)

