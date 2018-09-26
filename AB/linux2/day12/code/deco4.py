# deco3.py

# 本示例示意一个函数可以使用两个或两个以上的装饰器来装饰

# 以下是一个装饰器函数，在fn调用之前加一个权限验证的功能
def priv_check(fn):
    def fx(name, x):
        print("正在权限验证...")
        fn(name, x)
    return fx


def message_send(fn):
    def fy(name, x):
        # 先办其它业务
        fn(name, x)
        print("短信: ", name, "发生了", x, "元的操作，余额是xxx")
    return fy

# 存钱对应的函数
@priv_check
def save_money(name, x):
    print(name, "存钱", x, "元")

# 取钱对应的函数
@message_send
@priv_check
def withdraw(name, x):
    print(name, "正在办理取钱", x, '元的业务')

# 小郭程序员
save_money("小张", 200)
save_money("小赵", 500)


withdraw("小李", 300)