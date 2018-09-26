#coding=utf-8

'''
name: Levi
time: 2018-5-31
功能： 完成httpserver部分
'''

from socket import *
import sys 
import re 
from threading import Thread 

#处理http请求
class HTTPServer(object):
    def __init__(self,app):
        self.sockfd = socket()
        self.sockfd.setsockopt\
        (SOL_SOCKET,SO_REUSEADDR,1)
        self.app = app

    def bind(self,addr):
        self.sockfd.bind(addr)

    def start(self):
        self.sockfd.listen(10)
        while True:
            c,addr = self.sockfd.accept()
            print(addr,"用户连接")
            handle_thread = \
            Thread(target = self.handle_client,args = (c,))
            handle_thread.start()

    #客户端处理函数
    def handle_client(self,c):
        #接受浏览器request
        request_data = c.recv(2048)
        request_lines = request_data.splitlines()
        #请求行  'GET / HTTP/1.1'
        request_line = request_lines[0].decode('utf-8')
        print(request_line)
        #GET or POST
        method = re.match(r'(\w+)\s+/\S*',request_line).group(1)
        filename = re.match(r'\w+\s+(/\S*)',request_line).group(1)
        # print(method,filename)

        #要传递的内容写入一个字典中，传递给应用程序
        env = {'METHOD':method,'PATH_INFO':filename}

        response_body = self.app(env,self.set_headers)
        response = self.response_headers +'\r\n' \
        + response_body
        #像客户端发送response
        c.send(response.encode())
        c.close()

    def set_headers(self,status,headers):
        '''
        在app调用该函数 希望得到
        status = "200 OK"
        headers = [
            ("Content-Type","text/plain")
        ]
        '''
        response_headers = "HTTP/1.1 " + status + '\r\n'
        for header in headers:
            response_headers += "%s: %s\r\n"%header
        self.response_headers = response_headers

# 完成httpserver对象属性的添加 和创建
def main():
    # 要选择一个要使用的网站 的某个 app
    if len(sys.argv) < 2:
        sys.exit('''
            Run the server as:
            python3 HttpServer.py FrameworkName:app
            ''')
    #获取到这个网站下则这个应用到本地
    module_name,app_name = sys.argv[1].split(':') 
    sys.path.insert(1,'.')
    m = __import__(module_name)
    app = getattr(m,app_name)
    #将该应用变为server对象的属性
    http_server = HTTPServer(app)
    http_server.bind(('0.0.0.0',8000))
    print("Listen on port 8000....")
    http_server.start()
    

if __name__ == "__main__":
    main()