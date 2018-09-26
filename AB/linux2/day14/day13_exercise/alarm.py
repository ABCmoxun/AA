# 1. 编写一个闹钟程序，启动时设置定时时间（小时和分钟)

#     到时间后打印"时间到....." 然后退出程序

import time

def alarm():
    h = int(input("请输入小时: "))
    m = int(input("请输入分钟: "))
    while True:
        ct = time.localtime()  # 当前时间的元组
        if (h, m) == ct[3:5]:
            print("\n时间到...")
            return
        print("\r%02d:%02d:%02d" % ct[3:6], end='')
        time.sleep(1)

# 启动闹钟
alarm()


