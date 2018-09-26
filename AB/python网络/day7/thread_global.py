from threading import Thread 
from time import sleep

#通过全局变量进行线程通信
a = 1 

def foo():
    global a 
    a = 1000 

def bar():
    sleep(1)
    print("a =",a) # a = 1000

t1 = Thread(target = foo)
t2 = Thread(target = bar)

t1.start()
t2.start()

t1.join()
t2.join()
