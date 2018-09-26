# myyield.py


def myyield():
    yield 2
    yield 3
    yield 5
    yield 7
    print("生成器函数调用结束")

gen = myyield()
print(gen)  # gen绑定生成器对象,此对象为可迭代对象

for x in gen:
    print(x)
# it = iter(gen)  # 返回迭代器
# x = next(it)
# print(x)
# print(next(it))

