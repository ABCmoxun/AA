# 练习：
#   写程序，任意输入一行字符串，打印这个符串内有多少个空格' '(要求用for语句，不能用S.count方法)

#   思考：
#     上题能否用while语句实现?

s = input("请输入一行字符串: ")
# 用for语句实现
# count = 0  # 创建一个变量，准备计数,初始值是0
# for x in s:
#     if x == ' ':
#         count += 1
# else:
#     print("空格的个数是:", count)

# 用while语句实现
count = 0  # 创建一个变量，准备计数,初始值是0
length = len(s)  # 得到长度
i = 0  # 索引的起始值
while i < length:
    x = s[i]
    if x == ' ':
        count += 1
    i += 1
else:
    print("空格的个数是:", count)