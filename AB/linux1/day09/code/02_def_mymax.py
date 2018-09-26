# 02_def_mymax.py


# 此示例示意定义一个带有参数的函数:
def mymax(a, b):
    if a > b:
        print("最大数是", a)
    else:
        print("最大数是", b)


# 调用带有参数的函数, 第一个实参100给形参a, 第二个...
mymax(100, 200)

mymax(10000, 5000)  # 最大数是10000
mymax(4 + 7, 5 + 5)  # 最大数是11

mymax("ACD", "ABCD")  # 最大数是 ACD

