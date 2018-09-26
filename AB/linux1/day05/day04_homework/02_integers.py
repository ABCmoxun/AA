# 02_integers.py

# 2. 写一个程序。
#   输入一个开始的整数值用变量begin绑定
#   输入一个结束的整数值用变量end绑定
#   打印从begin到end(不包含end)的每个整数(打印在一行内)
#   如:
#   请输入开始值: 8
#   请输入结束值: 30
#   打印结果:
#     8 9 10 11 12 ...... 28 29
#   附加思考:
#     如何实现每5个数字打印在一行内?

begin = int(input("请输入开始值: "))
end = int(input("请输入结束值: "))

i = begin  # 新创建一个循环变量，用于控制循环
count = 0  # 此变量用于记录，每次加1,当能被5整除时换行
while i < end:
    print(i, end=' ')
    count += 1
    if count % 5 == 0:
        print()
    i += 1
else:
    print()


