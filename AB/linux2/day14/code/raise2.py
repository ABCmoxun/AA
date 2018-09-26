# raise.py


# 此示例示意raise语句的用法
def make_except(n):
    # 假设n必须是 0~100之间的数
    print("begin...")
    if n > 100:  # 传过的来参数无效，怎么告诉调用者呢？
        raise ValueError
    if n < 0:
        raise ValueError("参数小于零错误:%d" % n)
    print("end")


value = int(input("请输入一个整数:"))
try:
    make_except(value)
except ValueError as e:
    # print("make_except 抛出了错误，此异常状态已处理")
    # print("错误的值是:", e)
    print("发生错误")

print("程序正常完成")
