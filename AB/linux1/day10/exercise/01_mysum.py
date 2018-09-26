# 1. 写一个函数 mysum 此函数的功能是返回:
#    1 + 2 + 3 + 4 + 5 + ..... + n 的和
# def mysum(n):
#     ....

# print(mysum(100))  # 5050


def mysum(n):
    # 定义一个局部变量,让其值初始化为0
    s = 0
    for x in range(1, n + 1):
        s += x
    # 返回结果
    return s

print(mysum(100))  # 5050

print(mysum(10000))
