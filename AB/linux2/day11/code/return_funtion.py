# def fx():
#     def hello():
#         print("hello world")
#     return hello

# fh = fx()  #  fh绑定 fx内部创建的函数
# fn = fx()  # fn 也同样绑定fx创建的函数hello


# 以下用列表来说明 def 的作用是创建新的函数:
def fx():
    # def hello():
    #     print("hello world")
    hello = [1, 2, 3]
    return hello


fh = fx()  # fh绑定 fx内部创建的函数
fn = fx()  # fn 也同样绑定fx创建的函数hello
print('fh=', fh)  # [1,2,3]
print('fn=', fn)  # [1,2,3]
fh[1] = 2.2
print('fh=', fh)  # [1,2.2,3]
print('fn=', fn)  # [1,2,3]
