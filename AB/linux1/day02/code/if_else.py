# if 语句示意


# 输入一个整数，判断这个数是正数，负数，还是零
s = input("请输入一个数: ")
num = int(s)  # 将字符串转为整数

if num > 0:
    print("正数")
elif num < 0:
    print("负数")
else:
    print("零")


