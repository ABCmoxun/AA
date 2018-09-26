# 2. 写一个函数 mysum2 此函数可以传入一个参数,两个参数和三个参数:
# 1) 当传入一个参数时,这个参数代表 终止数
# 2) 当传入两个参数时,第一个参数代表起始值,第二个参数代表终止值
# 3) 当传入三个参数时,第三个参数代表步长
# 此函数的功能是返回从开始到终止值的和
# 如:

# print(mysum2(5))  # 10  (0+1+2+3+4)
# print(mysum2(4, 6))  # 9 (4+5)
# print(mysum2(5, 10, 2))  # 21 (5+7+9)

# 方法1
# def mysum2(*args):
#     if len(args) == 1:  # 处理只有一个参数传入的情况
#         s = 0
#         for x in range(args[0]):
#             s += x
#         return s
#     elif len(args) == 2:
#         s = 0
#         for x in range(args[0], args[1]):
#             s += x
#         return s
#     elif len(args) == 3:
#         s = 0
#         for x in range(args[0], args[1], args[2]):
#             s += x
#         return s

# 方法2
# def mysum2(*args):
#     s = 0
#     if len(args) == 1:  # 处理只有一个参数传入的情况
#         r = range(args[0])
#     elif len(args) == 2:
#         r = range(args[0], args[1])
#     elif len(args) == 3:
#         r = range(args[0], args[1], args[2])
#     else:
#         return None

#     for x in r:
#         s += x
#     return s

# 方法3 使用缺省参数定义形参
# def mysum2(start, stop=None, step=1):
#     # 如果没有传入第二个实参,则重新定义start,和stop
#     if stop is None:
#         stop = start
#         start = 0
#     s = 0
#     for x in range(start, stop, step):
#         s += x
#     return s


# 方法4 使用缺省参数定义形参
# def mysum2(start, stop=None, step=1):
#     # 如果没有传入第二个实参,则重新定义start,和stop
#     if stop is None:
#         stop = start
#         start = 0
#     return sum(range(start, stop, step))

# 方法五
def mysum2(*args):
    return sum(range(*args))

print(mysum2(5))  # 10  (0+1+2+3+4)
print(mysum2(4, 6))  # 9 (4+5)
print(mysum2(5, 10, 2))  # 21 (5+7+9)
# print(mysum2(1,2,3,4,5,6,6))

