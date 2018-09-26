# global_local_variable.py


# 此示例用来说明全局变量和局部变量的作用域范围及生命周期
a = 100
b = 200

def fn(c):
    d = 400
    # print(a, b, c, d)  # 有错,此时a变量还不存在
    a = 500  # 用来创建一个局部变量,
    print(a, b, c, d)  # 500, 200, 300, 400

fn(300)
print('a =', a)  # 100
print('b =', b)
