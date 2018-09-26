# break.py

# 此程序示意break跳出循环

i = 1
while i < 10:
    print("循环开始时的i =", i)
    if i == 5:
        break  # 跳出当前while语句
    print("循环结束时的i =", i)
    i += 1
else:
    print("我是while语句的else子句的print")

print("程序即将退出, i =", i)
