from multiprocessing import Array,Process 
import time 

def fun(shm):
    for i in shm:
        print(i)
    shm[2] = 1000

#开辟共享内存空间,可容纳6个整数
#初始值是[1,2,3,4,5,6]
# shm = Array('i',[1,2,3,4,5,6])
#表示在共享内存中开辟一个包含6个整形的空间
shm = Array('i',6)

p = Process(target = fun,args = (shm,))
p.start()
p.join()
for i in shm:
    print(i)