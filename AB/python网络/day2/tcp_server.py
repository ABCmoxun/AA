from socket import * 

#创建流式套接字
sockfd = socket(AF_INET,SOCK_STREAM,0)

#绑定ＩＰ端口
sockfd.bind(('127.0.0.1',8888))

#设置监听套接字，创建监听队列
sockfd.listen(5)

while True:
    print("waiting for connect....")
    #等待客户端链接
    connfd,addr = sockfd.accept()
    print("connect from",addr)

    while True:
        #收发消息
    
        data = connfd.recv(1024)

        if not data:
            break   
        
        print(data.decode())

        #发消息
        connfd.send('来,确认下眼神'.encode())
    #关闭套接字
    connfd.close()

sockfd.close()

