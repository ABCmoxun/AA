# sum_1_100_skip_5711.py


# 练习：
#   写一个程序，求1 ~ 100之间所有不能被
#     5,7,11整除的数的和

s = 0
for i in range(1, 101):
    if i % 5 == 0:
        continue
    if i % 7 == 0:
        continue
    if i % 11 == 0:
        continue
    s += i
else:
    print("和是:", s)
