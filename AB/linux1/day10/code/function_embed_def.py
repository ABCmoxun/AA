

# 此示例示意函数的嵌套定义 
def get_func(value):
    if value == 1:
        def myadd(x, y):
            return x + y
        return myadd
    elif value == 2:
        def mysub(x, y):
            return x - y
        return mysub


fx = get_func(1)
print(fx(400, 300))  # 700
fx = get_func(2)
print(fx(400, 300))  # 100
