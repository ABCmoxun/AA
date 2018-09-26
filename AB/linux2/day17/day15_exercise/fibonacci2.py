# fibonacci.py


# 练习：
#   1. 用生成器函数生成斐波那契数列的前n个数:
#     1 1 2 3 5 8 13 ....

#       def fibonacci(n):
#           ...
#           yield ..
#       1) 输出前 20 个数
#       2) 求前 30 个数的和

def fibonacci(n):
    count = 0  # 记录当前已生成的数的个数
    # 判断当前已生成的个数大于等于需要的个数时，直接返回
    if count >= n:
        return
    yield 1  # 生成1
    count += 1  # 已生成的个数加1

    if count >= n:  # 再次判断已生成数的个数
        return
    yield 1  # 生成一个1
    count += 1  # 已生成个数加1

    # 用列表生成第三个起的数
    a = 1  # a代表倒数第二个数
    b = 1  # b代表倒数第一个数
    # 如果已生成的个数小于需要的个数，则继续生成
    while count < n:
        # 从第三个起
        a, b = b, a + b  # a+b是需要生成的数
        yield b  # 返回刚生成的数
        count += 1  # 已生成的个数加1

# 1) 输出前 20 个数
for x in fibonacci(20):
    print(x)

# 2) 求前 30 个数的和
print(sum(fibonacci(30)))
