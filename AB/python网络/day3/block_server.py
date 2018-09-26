from socket import * 
from time import sleep,ctime

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(5)
#设置s是非阻塞状态
s.setblocking(False)
while True:
    print("waiting for connect....")
    try:
        connfd,addr = s.accept()
    except BlockingIOError:
        sleep(2)
        print(ctime())
        continue

    print("connect from",addr)
    # recv变为非阻塞
    # connfd.setblocking(False)
    while True:
        data = connfd.recv(1024)
        if not data:
            break   
        print(data.decode())
        connfd.send('来,确认下眼神'.encode())
    connfd.close()
s.close()
