# 1. 写一个程序，以电子时钟的格式显示时间:
#   HH:MM:SS

import time

def show_time():
    while True:
        t = time.localtime()  # t绑定时间元组
        s = "\r  %02d:%02d:%02d" % (t[3], t[4], t[5])
        print(s)
        s = "\r  %02d:%02d:%02d" % t[3:6]
        print(s, end='')
        time.sleep(1)

show_time()
