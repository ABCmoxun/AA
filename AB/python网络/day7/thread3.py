#daemon属性
from threading import Thread
from time import sleep 

def fun():
    print("Daemon 属性测试")
    sleep(5)
    print("线程结束")

t = Thread(target = fun)

#为线程设置名字
t.setName("tedu")

#daemon属性设置为True
#t.daemon = True
t.setDaemon(True)
print(t.isDaemon())

t.start()
t.join(2)
print("=====主线程结束======")