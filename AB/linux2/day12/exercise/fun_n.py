# 请编写函数 fun(n) 其功能是计算并输出下列多项式的和
#   Sn = 1 + 1/1! + 1/2! + 1/3! + 1/4! +... +1/n!
# 

from math import factorial as fac

# 方法1
# def fun(n):
#     s = 0
#     for i in range(n + 1):
#         s += 1 / fac(i)
#     print(s)


# 方法2
def fun(n):
    s = sum(map(lambda i: 1 / fac(i), range(n + 1)))
    print(s)

fun(20)

