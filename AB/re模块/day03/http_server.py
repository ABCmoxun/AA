
try:
    from BaseHTTPServer import \
    BaseHTTPRequestHandler,HTTPServer
except ImportError:
    from http.server import \
    BaseHTTPRequestHandler,HTTPServer

#请求处理类
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        #获取请求头
        print(self.headers)
        print("Do method get")
        fd = open('test.html','rb')
        content = fd.read()
        #组织响应行
        self.send_response(200)
        #组织响应头
        self.send_header('Content-Type','text/html')
        #响应头结束
        self.end_headers()
        #发送响应体
        self.wfile.write(content)
        return

    def do_POST(self):
        pass

#指定地址
address = ('0.0.0.0',8080)
#生产服务器对象
server = HTTPServer(address,RequestHandler)
#运行
server.serve_forever()