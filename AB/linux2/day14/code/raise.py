# raise.py


# 此示例示意raise语句的用法
# 以下示意其它语言中不用异常机制，用返回值方式返回错误问题
def make_except(n):
    # 假设n必须是 0~100之间的数
    print("begin...")
    if n > 100:  # 传过的来参数无效，怎么告诉调用者呢？
        return -1
    if n < 0:
        return -2
    print("end")
    return 0


value = int(input("请输入一个整数:"))
r = make_except(value)
if r < 0:
    print("发生错误")
else:
    print("程序正常完成")
