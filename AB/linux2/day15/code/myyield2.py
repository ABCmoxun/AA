# myyield.py


def myyield():
    print("即将生成2")
    yield 2
    print("即将生成3")
    yield 3
    print("即将生成5")
    yield 5
    print("即将生成7")
    yield 7
    print("生成器函数调用结束")

gen = myyield()
it = iter(gen)
print(next(it))
print(next(it))  # myyield将从上一次停止的位置开始执行


