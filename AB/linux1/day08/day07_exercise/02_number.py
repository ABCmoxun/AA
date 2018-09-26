# 2. 任意输入一些大于零数，存于列表中L,当输入-1时结束输入
#   L = [1, 3, 5, 3, 7, 9, 3, 7, 6, 5]
#   1) 打印出这些数
#   2) 打印出这些数的和
#   3) 去掉列表L中重复第二次或之后出现的数，再次存到另一个列表L2中
#      L2 = [1, 3, 5, 7, 9, 6]
#      打印这些数
#   4) 打印L2列表中的数据的和
#   5) 将 L列表中，出现两次的数存到另一个列表L3中
#        L3 = [5, 7]

L = []
while True:
    x = int(input("请输入: "))
    if x == -1:
        break
    L.append(x)

print("输入后的列表是:", L)
print("这些数的和是:", sum(L))
L2 = []
for x in L:  # 去重的算法
    if x not in L2:
        L2.append(x)
print(L2)
print(sum(L2))
L3 = []
for x in L:
    if L.count(x) == 2:  # 判断出现次数
        if x not in L3:  # 判断是否是存在L3
            L3.append(x)

print(L3)




