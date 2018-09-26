from socket import *
from time import sleep 

#发送广播的地址
#<broadcast>
dest = ('172.60.50.255',9999)

s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    sleep(1)
    s.sendto("坚决拥护习大大".encode(),dest)
    data,addr = s.recvfrom(1024)
    print("Received from %s:%s"%(addr,data.decode()))