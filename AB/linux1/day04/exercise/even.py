# 练习：
#   1. 写程序输入一个整数n:
#     打印n以内的全部大于0的偶数（不包含n)

n = int(input("请输入一个整数: "))

# 方法1
# i = 2
# while i < n:
#     print(i)
#     i += 2  # 增长值为2

i = 1
while i < n:
    if i % 2 == 0:
        print(i)
    i += 1
    # a = 100 + i
    # del a