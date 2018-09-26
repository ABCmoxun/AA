import signal 
from time import sleep 

signal.alarm(5)

#采用默认的方法处理SIGALRM信号
# signal.signal(signal.SIGALRM,signal.SIG_DFL)

#忽略信号
signal.signal(signal.SIGALRM,signal.SIG_IGN)
signal.signal(signal.SIGINT,signal.SIG_IGN)

while True:
    sleep(2)
    print("让你摁ctrl + c")
    print("等待时钟....") 
