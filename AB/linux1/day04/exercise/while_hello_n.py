
# 问题:
#   请输一个整数n，让程序输出n行的
#   hello 1
#   hello 2
#   ...
#   hello n

n = int(input("请输入一个整数n: "))

i = 1
while i <= n:
    print("hello", i)
    i += 1
