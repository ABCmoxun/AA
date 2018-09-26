'''
import requests
url1='http://i.baidu.com/'
url='https://passport.baidu.com/v2/api/?login'
#proxy={'http':'127.0.0.1:27017'}
#res=requests.get(url,headers=headers,proxies=proxy)
url='http://httpbin.org/ip'
res=requests.get(url,headers=headers)

print(res.status_code)
res.encoding=res.apparent_encoding

with open ('a1.html','w') as f:
    f.write(res.text)





import urllib, urllib2, sys
host = 'http://txyzmsb.market.alicloudapi.com'
path = '/yzm'
method = 'POST'
appcode = '你自己的AppCode'
querys = ''
bodys = {}
url = host + path

bodys['v_pic'] = '''v_pic'''
bodys['v_type'] = '''v_type'''
post_data = urllib.urlencode(bodys)
request = urllib2.Request(url, post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)
//根据API的要求，定义相对应的Content-Type
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
response = urllib2.urlopen(request)'''






import requests
import base64
url='http://passport.58.com/validcode/get?vcodekey=Koj5pbdUIV1OFqpsLy26rdja_avxWHMj&time=1537187757116'
#headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.23 Safari/537.36'}
#headers=headers
r=resquests.get(url，headers=headers)


with open ('a1.png','w') as f:
    f.write(r.content)


url1 ='http://txyzmsb.market.alicloudapi.com/yzm'
appcode = '099e20d757624b4ea0738e99f00a753d'

data={}
str1= base64.b64encode(r.content)
data['v_pic'] = str1
data['v_type'] = 'ne'

#图形验证码类型（n4：4位纯数字，n5：5位纯数字，n6:6位纯数字，
#e4：4位纯英文，e5：5位纯英文，e6：6位纯英文，ne4：4位英文数字，
#ne5：5位英文数字，ne6：6位英文数字），
#请准确填写，以免影响识别准确性
headers={'Content-Type': 'application/x-www-form-urlencoded',
          'charset':'utf-8'
         'Authorization': 'APPCODE '+ appcode }

resp=requests.post(url1,headers=headers,data=data)
content = resp.read()
if content:
    print(content)



















    
