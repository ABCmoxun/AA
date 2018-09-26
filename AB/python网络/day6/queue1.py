from  multiprocessing import Queue 
from time import sleep
#创建队列
q = Queue(3) 

q.put(1)
print(q.full())
q.put(2)
q.put(3)
print(q.full())

# 设置超时事件为3sec
# q.put(4,True,3)

print(q.get())
print("队列中还有%d条消息"%q.qsize())
print(q.empty())
q.close() #关闭队列