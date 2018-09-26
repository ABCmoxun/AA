#多进程tcp　

from socketserver import *

#创建服务器类
# class Server(ForkingTCPServer)
class Server(ForkingMixIn,TCPServer):
    pass 

#处理具体请求
class Handler(StreamRequestHandler):
    def handle(self):
        #self.request 相当于　accept创建的新的套接字
        addr = self.request.getpeername()
        print("Connect from",addr)
        while True:
            data = self.request.recv(1024).decode()
            if not data:
                break
            self.request.send(b"receive your message")

server = Server(('0.0.0.0',9999),Handler)
server.serve_forever()