

# function_variable.py
def test():
    x = 100  # 此变量是局部变量,只能在函数内部使用
    print(y)  # 这是合法的,此函数可以访问函数以外的全局变量


y = 200

test()  # 调用test

# print(x)  # 此时没有x这个变量, 出错

