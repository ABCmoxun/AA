# 2. 写一个lambda 表达式，求两个变量的最大值:
#   mymax = lambda ...
#   print(mymax(55, 63))  # 63


# mymax = lambda x, y: max(x, y)
mymax = lambda x, y: x if x > y else y

print(mymax(55, 63))  # 63
