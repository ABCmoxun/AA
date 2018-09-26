from socket import *  
import sys,os 

#确定用哪个文件进行通信
server_address = './test'

#判断文件存在性，如果已经存在需要处理
if os.path.exists(server_address):
    os.unlink(server_address)

#创建本地套接字
sockfd = socket(AF_UNIX,SOCK_STREAM)

#绑定本地套接字文件
sockfd.bind(server_address)
#监听
sockfd.listen(5)

#收发消息
while True:
    c,addr = sockfd.accept() 
    while True:
        data = c.recv(1024)
        if data:
            print(data.decode())
            c.sendall("收到消息".encode())
        else:
            break 
    c.close()
s.close()





