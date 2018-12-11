#-*- coding:utf-8 -*-

百度识别文档
http://ai.baidu.com/docs#/OCR-Python-SDK/07883957
开发资源---文档中心---视觉技术下的文字识别---->API文档---SDK文档中的python语言


#谷歌借口
安装PIL:pip install Pillow
安装pytesseract: pip install pytesseract
安装esseract-ocr: pip insatll tesseract-ocr 
  
from PIL import Image
import pytesseract
#img = img.convert('L')灰度化
# 加载图片
image = Image.open('test3.jpg')
# 识别过程
text = pytesseract.image_to_string(image,lang='chi_sim') #使用简体中文解析图片
print(text)

