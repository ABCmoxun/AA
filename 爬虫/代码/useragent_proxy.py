

# 在scrapy中的middleware中设置use_Agent和代理
import random
import base64

USER_AGENTS=[列表]
PROXIES=[{'ip_port':'127.0.0.1:0000'},
{'ip_port':'','user_passwd':user:passwd}
         {}]

class RandomUesrAgent(object):
    def process_request(self,request,sprider):
        useragent=random.choice(USER_AGENTS)
        request.headers.setdefault('User_Agent',useragent)


class RandomProxy(object):
    def process_request(self,request,sprider):
        proxy=random.choice(PROXIES)

        if proxy['user_passwd'] is None:
            request.meta['proxy']='http://'+proxy['ip_port']
            #request.meta['proxy']='https://'+proxy['ip_port']

        else:
            b64.user_psw=base64.b64encode(proxy['user_passwrd'].encode('utf-8'))
            request.meta['proxy']='http://'+proxy['ip_port']
            request.headers['proxy_Authorization']='basic '+b64.user_psw.decode('utf-8')
            #'basic '有一个空格




