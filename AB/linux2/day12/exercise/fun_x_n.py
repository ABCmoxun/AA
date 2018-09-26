# 请编写函数 fun(x, n) 它的功能是计算下载多数项的和并返回:
#   s = 1 + x + x**2/2! + x**3/3! + x**n/n!

#   print(fun(3.1, 10))

from math import factorial as fac


def fun(x, n):
    s = sum(map(lambda i: x ** i / fac(i),
                range(n + 1)))
    return s

print(fun(3.1, 10))
print(fun(1, 10))
