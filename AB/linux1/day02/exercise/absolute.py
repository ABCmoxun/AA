# 练习：
#   1. 写一个程序，输入一个数，用if语句计算并打印这个数的绝对值(注：不允许使用abs函数)
#   2. 写一个程序，输入一个数，用条件表达式计算并打印这个数的绝对值

n = int(input("请输入一个整数: "))

# 方法1 用if语句
# if n < 0:
#     print(-n)
# else:
#     print(n)

# 方法2
# if n < 0:
#     n = -n
# print(n)

# 方法3 用条件表达式实现

print(n if n > 0 else -n)
