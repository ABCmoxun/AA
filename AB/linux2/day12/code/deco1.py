# deco1.py


def mydeco(fn):  # <<==装饰器函数
    def fx():
        print("hello world!")
    return fx


@mydeco
def hello():   # <<== 被装饰函数
    print("hello tarena!")

# 此时将hello 变量绑定在了mydeco返回的函数上
# hello = mydeco(hello)  # 此种做法可以用装饰器@语法解决


hello()  # 调用者