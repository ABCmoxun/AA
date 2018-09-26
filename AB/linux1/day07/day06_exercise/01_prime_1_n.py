# 练习：
#   1. 输入一个整数n 代表结束的数.
#   将 1 ~ n之间所有的素数计算出来并存入到列表L 中
#     1) 最后打印此列表中的全部素数
#     2) 打印这些素数的和

n = int(input("请输入一个整数: "))
L = []
for x in range(1, n + 1):
    # 判断如果x为素数，则加入到一个列表L中
    if x < 2:  # 跳过小于2的数
        continue
    for i in range(2, x):  # i从2开始到 x-1结束
        if x % i == 0:  # x不是素数
            break
    else:
        L.append(x)

print(L)
print(1, '到', n, "所有素数的和是:", sum(L))
