from multiprocessing import Process 
import time 

class ClockProcess(Process):
    def __init__(self,value):
        self.value = value
        Process.__init__(self)

    # 在自定义的进程类中　重写父类的这个方法
    def run(self):
        n = 5
        while n > 0:
            print("The time is {}".\
                format(time.ctime()))
            time.sleep(self.value)
            n -= 1

#用自己的进程类创建进程
p = ClockProcess(2)

# 自动执行run方法
p.start()
p.join()