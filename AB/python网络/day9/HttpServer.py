'''
１．实现了多线程并发
２．讲server的创建部分封装为类
３．后端可以处理不同的请求　
'''
from socket import *
from threading import Thread
import sys 

ADDR = ('0.0.0.0',8000)
static_root = './static'
handler_root = './handler'

#httpserver 类
class HTTPServer(object):
    def __init__(self,addr):
        self.sockfd = socket()
        self.sockfd.setsockopt\
        (SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(addr)
        self.sockfd.listen(5)
        self.serveName = '127.0.0.1'
        self.servePort = 8000

    #服务器启动函数　: 接受客户端请求，创建新的线程
    def serveForever(self):
        while True:
            self.connfd,self.clientAddr =\
             self.sockfd.accept()
            clientThread = Thread\
            (target = self.handleRequest)
            clientThread.start()

    def setApp(self,application):
        self.application = application

    def handleRequest(self):
        #接收request请求
        self.recvData = self.connfd.recv(2048)
        requestHeaders = self.recvData.splitlines()
        for line in requestHeaders:
            print(line)

        #获取到从浏览器输入的具体请求
        getRequest = \
        str(requestHeaders[0]).split(' ')[1]

        if getRequest[-3:] != '.py':
            if getRequest == '/':
                getFilename = static_root + "/index.html"
            else:
                getFilename = static_root + getRequest

            try: 
                f = open(getFilename)
            except:
                responseHeaders = "HTTP/1.1 404 not found\r\n"
                responseHeaders += "\r\n"
                responseBody = "====sorry,file not find====="
            else:
                responseHeaders = "HTTP/1.1 200 OK\r\n"
                responseHeaders += "\r\n"
                responseBody = f.read()
            finally:
                response = responseHeaders + responseBody
                self.connfd.send(response.encode())
        else:
            #需要的环境变量
            env = {}
            bodyContent = self.application\
            (env,self.startResponse)

            response = "HTTP/1.1 {}\r\n".format(self.header_set[0])
            for header in self.header_set[1:]:
                response += "{0}:{1}\r\n".format(*header)
            response += '\r\n'
            response += bodyContent
            self.connfd.send(response.encode())

        self.connfd.close()

    def startResponse(self,status,response_headers):
        serverHeaders = [
            ('Date','2018-5-21'),
            ('Server',"HTTPServer 1.0"),
        ]
        self.header_set = \
        [status,response_headers + serverHeaders]


#控制服务器启动
def main():
    # 启动时直接告知使用哪个模块哪个函数处理请求
    # python3 HttpServer.py module app
    if len(sys.argv) < 3:
        sys.exit("请选择一个模块和应用")
    #将handler文件夹加入搜索路径
    sys.path.insert(0,handler_root)
    #导入module模块
    m = __import__(sys.argv[1])
    #获取module 下的app 付给一个变量
    application = getattr(m,sys.argv[2])

    httpd = HTTPServer(ADDR)
    httpd.setApp(application)
    print("Serving HTTP on port 8000")
    httpd.serveForever()

if __name__ == "__main__":
    main()