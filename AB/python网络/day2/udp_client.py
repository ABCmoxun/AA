from socket import * 
import sys 

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

while True:
    data = input("消息>>")
    #直接回车退出
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    data,addr = sockfd.recvfrom(BUFFERSIZE)
    print('从服务器收到：',data.decode())
sockfd.close()