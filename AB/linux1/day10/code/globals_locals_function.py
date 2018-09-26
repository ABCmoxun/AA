# globals_locals_function.py

# 此示例示意globals 和 locals 函数的用法

a = 100
b = 200


def fx(b, c):
    print(a, b, c)
    # 思考在此函数内部能否获取到全局变量b绑定的值?
    print("全局变量的字典是:", globals())
    print("局部变量的字典是:", locals())
    print("此处访问全局的b的值是:", globals()['b'])


fx(300, 400)


