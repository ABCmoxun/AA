import os 
from time import sleep

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:   
    print("Child process")
    print("getpid() :",os.getpid()) #子进程自己获取自己的PID
    print("getppid() :",os.getppid()) #子进程获取它父进程的PID
    print("========================")
else:
    sleep(1)
    print("Parent process")
    print("pid =",pid)　#父进程fork返回值就是子进程PID
    print("getpid():",os.getpid())#父进程获取自己的PID
