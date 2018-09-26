# closure.py


# 此程序示意闭包的用法
# 1. fn为内嵌函数
# 2. fn 用到了fn外部的变量y
# 3. make_power将 fn绑定的函数对象返回给调用者
def make_power(y):
    def fn(x):
        return x ** y
    return fn


pow2 = make_power(2)
#pow2 等同于:
# def pow2(x):
#     return x ** 2

print("5的平方是:", pow2(5))  # 25
print("9的平方是:", pow2(9))  # 81

# def pow4(x):
#     return x**4
pow4 = make_power(4)
print('5的四次方是:', pow4(5))
