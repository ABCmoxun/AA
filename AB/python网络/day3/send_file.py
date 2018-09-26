from socket import * 
from time import sleep

s = socket() 
s.bind(("127.0.0.1",8888))
s.listen(5)

c,addr = s.accept()
print("Connect from ",addr)

f = open('send_file','rb')

while True:
    data = f.read(128)
    if not data:
        sleep(0.5)
        c.send(b'##')
        break
    c.send(data)


f.close()    
c.close()
s.close()
