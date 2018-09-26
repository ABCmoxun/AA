from socket import * 

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#发起连接
sockfd.connect(('127.0.0.1',8888))

while True:
    msg = input("发消息>>")
    #发送消息
    sockfd.send(msg.encode())
    if not msg:
        break

    #接收消息
    data = sockfd.recv(1024)
    print(data.decode())

#关闭
sockfd.close()
