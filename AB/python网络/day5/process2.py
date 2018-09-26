from multiprocessing import * 
from time import sleep

a = 1

def worker(sec,msg):
    print("a = ",a)
    for i in range(3):
        sleep(sec)
        print("worker message:",msg)

# 位置传参
# p = Process(target = worker,args = (2,"hello")
# 字典传参
p = Process(name="worker",target = worker,\
    args = (2,),kwargs = {'msg':"hello"})
p.start()

print("p.name :",p.name)
#p所代表的子进程的ＰＩＤ号
print("p.pid:",p.pid)
print("p.alive",p.is_alive())

p.join()  