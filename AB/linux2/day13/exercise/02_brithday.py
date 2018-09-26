# 2. 写一个程序，输入你的生日，
#   1) 计算出你出生的那天是星期几?
#   2）计算出你已经出生了多少天?

import time

y = int(input("输入出生的年:"))
m = int(input("输入出生的月:"))
d = int(input("输入出生的日:"))

t = time.mktime((y, m, d, 0, 0, 0, 0, 0, 0))
print("UTC时间的秒数:", t)

time_tuple = time.localtime(t)
week = time_tuple[6]
L = ['星期一',
     '星期二',
     '星期三',
     '星期四',
     '星期五',
     '星期六',
     '星期日']

print("这一天是:", L[week])


t = time.time() - t  # 从生日到现在过了多少秒

d = t / (60 * 60 * 24)  # t / 一天的秒数

print("您已出生", d, "天")

