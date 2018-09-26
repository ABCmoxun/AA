from socket import *

HOST = ''
PORT = 9999

#创建套接字
s = socket(AF_INET,SOCK_DGRAM)
#设置套接字可以接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

#固定接收端的端口号
s.bind((HOST,PORT))

while True:
    try:
        message,addr = s.recvfrom(4096)
        print("从{}获取信息{}:".\
            format(addr,message.decode()))
        s.sendto(b"I am here",addr)
    except (KeyboardInterrupt,SyntaxError):
        raise
    except Exception as e:
        print(e)

s.close()

