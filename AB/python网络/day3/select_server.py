from socket import * 
from select import *
import sys

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("127.0.0.1",8888))
s.listen(10)

#将关注的ＩＯ放入rlist
rlist = [s]
wlist = []
xlist = [s]

while True:
    print("等待ＩＯ")
    #wlist中有内容select会立即返回
    rs,ws,xs = select(rlist,wlist,xlist,3)
    for r in rs:
        #表示套接字准备就绪
        if r is s:
            connfd,addr = r.accept()
            print("Connect from",addr)
            #将新的套接字加入到关注列表
            rlist.append(connfd)
        else:
            try:
                data = r.recv(1024)
                if not data:
                    rlist.remove(r)
                    r.close()
                else:
                    print("Received from",r.getpeername(),\
                        ":",data.decode())
                    #想发消息可以放到写关注列表
                    wlist.append(r)
            except Exception:
                pass

    for w in ws:
        w.send("天地悠悠，一壶浊酒".encode())
        wlist.remove(w)

    for x in xs:
        if x is s:
            s.close()
            sys.exit(1)
