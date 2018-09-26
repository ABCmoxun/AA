# 练习2:
#   写一个函数print_even, 传入一个数参n代表终止整数(不包含n)
#   打印:
#      2 4 6 ... n之间所有偶数:
#   函数定义格式如下:
#     def print_even(n):
#         .... <<<--- 此处自己完成
#     # 测试调用:
#     print_even(9)
#     2
#     4
#     6
#     8

def print_even(n):
    for x in range(2, n):
        if x % 2 == 0:
            print(x)


print_even(9)

# print(x)
