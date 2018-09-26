import time
#处理特定请求的模块
def app(environ,start_response):
    status = '200 OK'
    response_headers =\
     [('Content-Type','text/plain;charset=UTF-8')]

    start_response(status,response_headers)

    return "\n====简单的app程序===\n%s"%time.ctime()
