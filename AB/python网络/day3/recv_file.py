from socket import *

s = socket()

s.connect(("127.0.0.1",8888))

f = open('recv_file','w')

while True:
    data = s.recv(1024).decode()
    if data == '##':
        break
    f.write(data)

f.close()
s.close()
