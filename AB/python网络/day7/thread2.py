#线程对象属性
from threading import Thread,currentThread
from time import sleep 

def fun(sec):
    print("线程属性测试")
    sleep(sec)
    print(" %s 线程结束"%currentThread().getName())

thread = []
for i in range(3):
    t = Thread(name = "tedu" + str(i),\
        target = fun,args = (3,))
    t.start()
    thread.append(t)

for i in thread:
    i.join()
    print("thread name:",i.name)
    print("alive:",i.is_alive())
    
