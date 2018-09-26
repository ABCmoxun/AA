# pass.py

# 输入一个季度，如果输入不是1~4则打印输入错误,
# 否则什么都不做

season = int(input("请输入一个整数(1~4): "))
if 1 <= season <= 4:
    pass
else:
    print("您的输入有错！")