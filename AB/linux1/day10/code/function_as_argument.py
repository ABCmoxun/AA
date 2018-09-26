

# 此示例示意函数作为参数传递
def f1():
    print("f1函数被调用")


def f2():
    print("f2函数被调用")


def fx(fn):
    print("fn绑定的函数是:", fn)
    # 在fx内调用fn绑定的函数
    fn()


fx(f1)  # 调用fx,把f1作为实参传数
fx(f2)  # 用fx间接调用f2
