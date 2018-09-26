from socket import * 

s = socket()

#设置端口立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

#获取选项值
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))

#套接字描述符
print(s.fileno())
#套接字类型
print(s.type)

s.bind(('172.60.50.42',9999))
#获取绑定的地址
print(s.getsockname())

s.listen(5)
conn,addr = s.accept()
print(conn.getpeername())

while True:
    conn.recv(1024)