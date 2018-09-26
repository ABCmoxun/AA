from signal import * 
import time 

#固定格式要求
def handler(sig,frame):
    if sig == SIGALRM:
        print("收到时钟信号")
    elif sig == SIGINT:
        print("就不结束") 

alarm(7)

#通过自定义方法处理
signal(SIGALRM,handler)
signal(SIGINT,handler)

while True:
    print("waiting for a signal")
    time.sleep(2)