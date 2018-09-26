# 2. 输入一个学生的三科成绩：
# 　　　1)　打印出最高分是多少分?
#    2) 打印出最低分是多少分?

a = int(input("请输入第一科成绩: "))
b = int(input("请输入第二科成绩: "))
c = int(input("请输入第三科成绩: "))

# 方法1
# # 先假设 a最大
# m = a
# # 再与b比较
# if m < b:
#     m = b
# if m < c:
#     m = c
# print("最高分是: ", m)

# 方法2
if b < a > c:
    print("最高分是: ", a)
elif a < b > c:
    print("最高分是: ", b)
else:
    print("最高分是: ", c)