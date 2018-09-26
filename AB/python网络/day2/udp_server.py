from socket import * 
import sys 
from time import ctime 

#从命令行传入ＩＰ和端口
#python3 udp_server.py 172.60.50.42 8888
if len(sys.argv) < 3:
    print('''
           argv is error!!!
           input as 
           python3 udp_server.py 172.60.50.42 8888
           ''')

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
BUFFERSIZE = 1024

#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)
#绑定地址
sockfd.bind(ADDR)

#收发消息
while True:
    data,addr = sockfd.recvfrom(BUFFERSIZE)
    print('recv from %s:%s'%(addr,data.decode()))
    sockfd.sendto\
    (("[%s] 接收到消息"%ctime()).encode(),addr)

sockfd.close()