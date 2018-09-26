from socket import * 

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#发起连接
sockfd.connect(('172.60.50.42',9999))

for i in range(5):
    sockfd.send(str(i).encode())

#接收消息
data = sockfd.recv(1024)
print(data.decode())

#关闭
sockfd.close()
