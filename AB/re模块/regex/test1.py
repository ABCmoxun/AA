import re 
import sys 

def getAddress(port):
    pattern = r'^\S+'
    f = open('1.txt','r')
    while True:
        data = ''
        for line in f:
            if line != '\n':
                data += line
            else:
                break
        if not data:
            break
        PORT =  re.match(pattern,data).group()
        if port == PORT:
            pattern = r'address is (\S+)'
            addr = re.search(pattern,data).group(1)
            return addr 
        else:
            continue

if __name__=='__main__':
    port = sys.argv[1]
    print(getAddress(port))