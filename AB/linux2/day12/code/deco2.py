# deco1.py


def mydeco(fn):  # <<==装饰器函数
    def fx():
        print("++++++++++++")
        fn()
        print('------------')
    return fx


# @mydeco
def hello():   # <<== 被装饰函数
    print("hello tarena!")

hello()  # 调用者