from multiprocessing import Value,Process 
import time 
import random 

#向共享内存存钱
def deposite(money):
    for i in range(100):
        time.sleep(0.03)
        money.value += random.randint(1,200)
#从共享内存取钱
def withdraw(money):
    for i in range(100):
        time.sleep(0.02)
        money.value -= random.randint(1,150)

#创建共享内存对象
money = Value('i',2000)

d = Process(target = deposite,args = (money,))
w = Process(target = withdraw,args = (money,))
d.start()
w.start()
d.join()
w.join()

print(money.value)