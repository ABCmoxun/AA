import signal 
import time 

#3秒后向自己发送个SIGALRM信号
signal.alarm(3)
time.sleep(2)

signal.alarm(8)

#阻塞等待接收一个信号
signal.pause()

while True:
    time.sleep(1)
    print("等待时钟.....")