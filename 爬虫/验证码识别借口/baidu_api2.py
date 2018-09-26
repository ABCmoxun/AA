
#百度的文字识别
#安装：pip install baidu-aip
#


from aip import AipOcr
import requests

url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1534911861248&di=7d7f97f2d1e3a23926bdc46611d9fd44&imgtype=0&src=http%3A%2F%2Fwww.zhengma.com%2FPublic%2Fstatics%2Fjs%2Fkindeditor%2Fattached%2Fimage%2F20140403%2F20140403163420_33708.jpg"
url='https://passport.lagou.com/vcode/create?from=register&refresh=1451121012510'
resp=requests.get(url)
print(resp.status_code)
resp=resp.content

""" 你的 APPID AK SK """
APP_ID = '11709692'
API_KEY = 'gwLwKiqi8yNA5thAPuZCIqhG'
SECRET_KEY = 'W9g0kX4xEW1onboW6TDx0vKu2TZI5mT0'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

#res=client.accurate(resp)
#print(res)


""" 如果有可选参数 """
options = {}
options["detect_direction"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别（高精度版） """


res=client.accurate(resp,options)
print(res)


#谷歌的文字识别
#谷歌ai安装
#sudo apt-get install tesseract-ocr
#pip3 install pytesseract

from PIL import Image

from pytesseract import *

imag=Image_to_string(image)

print(image)





























