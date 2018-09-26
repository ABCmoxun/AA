#静态网页处理器
#采用循环的模式，无法满足客户端长连接

from socket import *

#处理客户端请求
def handleClient(connfd):
    request = connfd.recv(2048) 
    requestHeadlers = request.splitlines()
    for line in requestHeadlers:
        print(line)

    try:
        f = open("知乎.html",'r')
    except IOError:
        response = "HTTP/1.1 404 not found\r\n"
        response += '\r\n'
        response += "====sorry ,file not find"
    else:
        response = "HTTP/1.1 200 OK\r\n"
        response += '\r\n'
        for i in f:
            response += i
    finally:
        connfd.send(response.encode())
        connfd.close()

#流程控制
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8000))
    sockfd.listen(10)
    while True:
        connfd,addr = sockfd.accept()
        handleClient(connfd)
     

if __name__ == "__main__":
    main()