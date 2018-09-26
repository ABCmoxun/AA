import os 
from time import sleep 

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    #父进程已经退出，打印的将是新的父进程的ＰＩＤ
    # sleep(1)
    # print("My parent PID:",os.getppid())
    print("child PID",os.getpid())
else:
    #子进程退出，父进程不退出
    sleep(1)
    while True:
        pass

    # print("Parent PID:",os.getpid())
    