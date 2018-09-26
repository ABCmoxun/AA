from socket import * 
import os,sys 
import signal 
import time 

#文件库位置
FILE_PATH = "/home/tarena/pythonweb/day3/"

class TftpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd

    def do_list(self):
        filelist = os.listdir(FILE_PATH)
        if not filelist:
            self.connfd.send(b'N')
            return
        else:
            self.connfd.send(b"Y")
        time.sleep(0.1)
        files = ""
        for filename in filelist:
            if filename[0] != '.' and os.path.isfile(FILE_PATH + filename):
                files = files + filename + '#'

        self.connfd.send(files.encode())

    def do_get(self):
        pass
    def do_put(self):
        pass

def main():
    if len(sys.argv) < 3:
        print("argv is error")
        sys.exit(1)
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    BUFFERSIZE = 1024

    sockfd  = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while True:
        try: 
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit(0)
        except Exception:
            continue 
        print("客户登录:",addr)
        pid = os.fork()
        if pid < 0:
            print("创建子进程失败")
            connfd.close()
            continue
        elif pid == 0:
            sockfd.close()
            #创建客户端通信对象
            tftp = TftpServer(connfd)
            while True:
                #接受客户端的请求类型
                data = connfd.recv(BUFFERSIZE).decode()
                if data[0] == 'L':
                    tftp.do_list()
                elif data[0] == 'G':
                    tftp.do_get()
                elif data[0] == "P":
                    tftp.do_put()
                elif data[0] == "Q":
                    print("客户端退出")
                    sys.exit(0) 
        else:
            connfd.close()
            continue 

if __name__ == "__main__":
    main()