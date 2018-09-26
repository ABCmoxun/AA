# 1. 编写函数 myfac(x) 计算x的阶乘x!
#    5! = 5 * 4 * 3 * 2 * 1

#   print(myfac(5))  # 120

# 方法1用循环来实现
# def myfac(x):
#     s = 1
#     for i in range(2, x + 1):
#         s *= i
#     return s

# 方法2用递归来实现
def myfac(x):
    if x == 1:
        return 1
    return x * myfac(x - 1)

print(myfac(5))  # 120

