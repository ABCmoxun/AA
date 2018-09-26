# 2. 输入一个圆的面积，打印出这个圆的半径
#    面积 = pi * 半径的平方
#   (要求用math模块内的函数和变量)

import math

area = float(input("请输入圆的面积: "))

# r = math.sqrt(area / math.pi)
r = (area / math.pi) ** 0.5

print("半径是: ", r)
