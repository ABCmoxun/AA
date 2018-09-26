from threading import Thread 
from time import ctime,sleep 

#编写自己的线程类 
class MyThread(Thread):
    def __init__(self,func,args,name = "Tedu"):
        super().__init__()
        self.func = func 
        self.args = args
        self.name = name 

    # 调用start会自动运行
    def run(self):
        self.func(*self.args)

def player(file,sec):
    for i in range(2):
        print("playing %s : %s"%(file,ctime()))
        sleep(sec)


t = MyThread(player,('baby.mp3',3))
t.start()
t.join()
