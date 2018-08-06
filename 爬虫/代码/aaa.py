import requests
import re
from bs4 import BeautifulSoup
l=[]
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/53"}
url="http://maoyan.com/board/4?offset=0"
def get_resp():
    r=requests.get(url,headers=headers)
    if r.status_code==200:
        r.encoding='utf-8'
        return r.text

def parser(demo):
    soup=BeautifulSoup(demo,'html.parser')
    elemt1=soup.find_all('p',class_='name')
    # i1=elemt1.children[1].string
    for i in range(len(elemt1)):
        d['i1']=soup.find_all('a',class_='image-link')[i].attrs['title'].strip()
        d['i2']=soup.find_all('p',class_='star')[i].string.strip()
        d['i3']=soup.find_all('p',class_='releasetime')[1].string.strip()
        t=(d['i1'],d['i2'],d['i3'])
        print(t)
        print(1)
        yield{
              "title":t[0],
              "actor":t[1],
              "time":t[2]
        }
        l.append(t)
    print(l)


def write():
    with open("maoyan.txt", 'wb') as f:
        # f.write(json.dumps(l, ensure_ascii=False)+'\n')
        f.write(str(l).encode('utf-8'))


if __name__=='__main__':
    demo=get_resp()
    parser(demo)
    write()