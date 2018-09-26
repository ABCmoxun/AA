# iterator.py

L = [2, 3, 5, 7]
# 用for循环来访问可迭代对象中的数据
for x in L:
    print(x)

print('-------------------------')
# 用while循环能否访问可迭代对象中的数据?
# 第一步，让L给我们一个迭代器
it = iter(L)
# 第二步，循环用it迭代器去获取L中的数据，
#   直到StopIteration为止
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break



