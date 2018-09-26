import multiprocessing as mp 
import os 
import time

def th1():
    print(os.getppid(),"----",os.getpid())
    print("吃饭早饭")
    time.sleep(1)
    print("吃饭午饭")
    time.sleep(2)
    print("吃饭晚饭")
    time.sleep(3)

def th2():
    print(os.getppid(),"----",os.getpid())
    print("睡觉午觉")
    time.sleep(2)
    print("睡觉")
    time.sleep(3)

def th3():
    print(os.getppid(),"----",os.getpid())
    print("打豆豆")
    time.sleep(2)
    print("打豆豆")
    time.sleep(2)

things = [th1,th2,th3]
process = [] 

for th in things:
    p = mp.Process(target = th)
    p.daemon = True
    process.append(p)
    p.start()

print("+++++++父进程++++++++")

# for i in process:
#     i.join()
