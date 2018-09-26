import threading 
from time import sleep 

s = None 

#创建线程事件对象
e = threading.Event()

def bar():
    print("呼叫foo")
    global s 
    s = "天王盖地虎"

def foo():
    print("等待口令")
    sleep(2)
    if s == "天王盖地虎":
        print("foo收到:",s)
    else:
        print("打死他")
    e.set()

def fun():
    print("呵呵...")
    sleep(1)
    e.wait()
    global s 
    s = "小鸡炖蘑菇"


t1 = threading.Thread(name = 'bar',target = bar)
t2 = threading.Thread(name = 'foo',target = foo)
t3 = threading.Thread(name = 'fun',target = fun)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()