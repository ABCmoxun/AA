from socket import * 
from time import sleep,ctime
import traceback

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(5)
#设置s超时检测
s.settimeout(5)

while True:
    print("waiting for connect....")
    try:
        connfd,addr = s.accept()
    except Exception:
        traceback.print_exc()
        continue

    print("connect from",addr)
    # recv设置超时
    #　connfd.settimeout(3)
    while True:
        data = connfd.recv(1024)
        if not data:
            break   
        print(data.decode())
        connfd.send('来,确认下眼神'.encode())
    connfd.close()
s.close()
