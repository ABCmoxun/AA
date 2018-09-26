
# 练习：
#   写一个程序，让用户输入很多个正整数，当输入小于零的数时结束输入
#   1)  输出这些数的和
#   2)  输出这些数的最大的数和第二大的数
#   3)  删除最小的一个数
#   4)  按原来输入的顺序打印出剩余的这些数

L = []
while True:
    n = int(input("请输入一个正整数:"))
    if n < 0:  # 如果是负数，结束输入
        break
    L.append(n)

print(L)

# 1)  输出这些数的和 sum
print("这些数的和是: ", sum(L))
# 2)  输出这些数的最大的数和第二大的数
#     max,  L.remove  或 排序 后取[0] [1]
L2 = L.copy()  # 复制原来的列表
L2.sort(reverse=True)
print("最大的数是: ", L2[0])
print("第二大的数是: ", L2[1])

# 3)  删除最小的一个数
#      min. L.remove
m = min(L)  # 先找到最小的数
L.remove(m)  # 删除最小的数
# 4)  按原来输入的顺序打印出剩余的这些数
for i in L:
    print(i)

    