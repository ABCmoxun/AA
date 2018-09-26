# 输入一个开始的整数用begin绑定
# 输入一个结束的整数用end绑定
# 打印 begin ~ end之间所有的奇数

begin = int(input("请输入开始的整数: "))
end = int(input("请输入结束的整数: "))

# 方法1
i = begin
while i < end:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1

# 方法2
# i = begin
# while i < end:
#     if i % 2 == 1:
#         print(i)
#     i += 1
