# 1. 算出 100 ~ 999 以内的水仙花数(Narcissistic Number)
#    水仙花数是指百位的3次方 加上 十位的3次方 加上个位的3次方等于原数的数字
#    例如: 
#       153 等于 1**3 + 5**3 + 3**3


# 方法1
# for x in range(100, 1000):
#     gewei = x % 10  # 求个位
#     shiwei = (x % 100) // 10  # 求十位
#     baiwei = x // 100  # 求百位
#     if x == gewei**3 + shiwei**3 + baiwei**3:
#         print(x)

# 方法2 
for baiwei in range(1, 10):
    for shiwei in range(10):
        for gewei in range(10):
            # print(baiwei, shiwei, gewei)
            x = baiwei * 100 + shiwei * 10 + gewei
            if x == gewei**3 + shiwei**3 + baiwei**3:
                print(x)


