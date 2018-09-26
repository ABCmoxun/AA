# deco3.py
# 本示例示意带有参数的装饰器及其用法

# 以下是一个装饰器函数，在fn调用之前加一个权限验证的功能
def priv_check(fn):
    def fx(name, x):
        print("正在权限验证...")
        fn(name, x)
    return fx

# 存钱对应的函数
@priv_check
def save_money(name, x):
    print(name, "存钱", x, "元")

# 取钱对应的函数
@priv_check
def withdraw(name, x):
    print(name, "正在办理取钱", x, '元的业务')

# 小郭程序员
save_money("小张", 200)
save_money("小赵", 500)


withdraw("小李", 300)