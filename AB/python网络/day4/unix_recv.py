from socket import * 
import sys 

#文件已经被另一端创建
#　需要和另一端使用同一个ｓｏｃｋｅｔ文件
server_address = "./test"

try:
    sockfd = socket(AF_UNIX,SOCK_STREAM)
    sockfd.connect(server_address)
except error as e:
    print(e) 
    sys.exit(1)

while True:
    message = input("Your message>>")
    if message:
        sockfd.sendall(message.encode())
        print(sockfd.recv(1024).decode())
    else:
        break 

sockfd.close()


