#os为系统相关模块，不同操作系统使用情况不同

import os
from test import * 
from time import sleep

print("准备创建进程")
a = 1 

pid = os.fork()

if pid < 0:
    print("创建进程失败")
elif pid == 0:
    
    print("创建了一个新的进程 a = ",a)
    a = 10000
else:
    # sleep(0.1)
    print("这是原有的进程")
    # fun2()
    print("a = ",a)

print("进程执行完毕")

