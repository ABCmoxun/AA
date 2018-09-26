# 练习：
#   写入一个生成器函数, myodd(start, stop) 用于生成start开始到stop结束(不包含stop)的所有奇数

#   L = [x for x in myodd(1, 10)]
#   print(L)  # [1,3,5,7,9]
#   for x in myodd(10, 20):
#       print(x)  # 11, 13, 15, 17, 19


def myodd(start, stop):
    i = start
    while i < stop:
        if i % 2:  # 等同于 if i % 2 == 1:
            yield i
        i += 1


L = [x for x in myodd(1, 10)]
print(L)  # [1,3,5,7,9]
for x in myodd(10, 20):
    print(x)  # 11, 13, 15, 17, 19

