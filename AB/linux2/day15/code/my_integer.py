

# 写一个生成器函数my_integer(n)生成 1 到 n的整数:
def my_integer(n):
    i = 1  # 先初始化变量i将其设置为起始数
    while i < n:  # 循环判断是否已到终止点，如果未到则生成
        yield i  # 生成整数
        i += 1  # 控制循环条件


for x in my_integer(10000):
    print(x)  # 1  2  3  4
