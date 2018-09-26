from multiprocessing import Pool 
from time import sleep 
import os 

def worker(msg):
    sleep(2)
    print(msg)
    return msg + " over"

#　创建进程池
pool = Pool(processes = 4)

result = []
# 放入事件
for i in range(10):
    msg = "hello %d"%i 
    #加入事件后进程就会立即操作事件
    #apply_async 的返回值对象，该对象可以获取worker返回结果
    r = pool.apply_async(worker,(msg,))
    # pool.apply(worker,(msg,))
    result.append(r)

# sleep(3)
# print("++++++++")
#关闭进程池 不能再加入事件
pool.close() 
# sleep(3)
# print("*********") 
#阻塞等待回收
pool.join()

print("===========")
#通过apply_async()返回对象get()方法获取返回值
for res in result:
    print(res.get())