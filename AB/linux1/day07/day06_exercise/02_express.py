# 2. 求 100 以内有哪儿些整数与自身+1 的乘积 再对 11求余的结果等于8?
#      x * (x + 1) % 11 == 8
#   打印这些数，
#   将这些数存于列表中（偿试使用列表推导式)

# for x in range(100):
#     if x * (x + 1) % 11 == 8:
#         print(x)

L = [x for x in range(100) if x * (x + 1) % 11 == 8]

for x in L:
    print(x)
