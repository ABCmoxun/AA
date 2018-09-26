# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 16:36:42 2018

@author: Python
"""
from PIL import Image
import hashlib
import time
import os
import math

# 计算向量的余弦相似度
class VectorCompare:
    def magnitude(self,concordance):
        total = 0
        for word,count in concordance.items():
            total += count ** 2
        return math.sqrt(total)
    
    def relation(self,concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            #if concordance2.has_key(word):
            if word in concordance2:
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))
    
    
def buildvector(im):
	d1 = {}
    count = 0
    for i in im.getdata():
		d1[count] = i
        count += 1
	return d1


V = VectorCompare()
iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
imageset = []
for letter in iconset:
    for img in os.listdir('.\\iconset\\%s\\'%(letter)):
        temp = []
        if img != "Thumbs.db" and img != ".DS_Store": # windows check...
            temp.append(buildvector(Image.open(".\\iconset\\%s\\%s"%(letter,img))))
        imageset.append({letter:temp})
#print(imageset)

# 这是需要识别的验证码
im = Image.open("captcha.gif")
im2 = Image.new("P",im.size,255)
#im.size是个元组
#把图片转换成8位像素模式
im.convert("P")
#print(im.convert("P"))
#im2.show()
#变成直方图,每个数字都代表了图片中含有对应颜色的像素的数量(256个点)
#print(im.histogram())
#得到图片中最多的10中颜色
#list1=im.histogram()
#values={}
#for i in range(256):
#	value[i]=list1[1]
#for j,k in sort(values.items(),key=lambda x:x[1],reverse=True)[:10]:
#	print(j,k)




temp = {}
# 把图片的背景色和前景区分出来
for y in range(im.size[1]):
    for x in range(im.size[0]):
        pix = im.getpixel((x,y))
        temp[pix] = pix
        if pix == 220 or pix == 227: # these are the numbers to get
#重新对像素点赋值
            im2.putpixel((x,y),0)
#im2.show()
#im.getpixel()--value or tuple
#含义：给定位置像素值，元组
#load()
#r,g,b=img.split()



# 提取图片的单个字符
inletter = False
foundletter=False
start = 0
end = 0

letters = []
for x in range(im2.size[0]): # slice across
    for y in range(im2.size[1]): # slice down
        pix = im2.getpixel((x,y))
        if pix != 255:
            inletter = True

    if foundletter == False and inletter == True:
        foundletter = True
        start = x
    
    if foundletter == True and inletter == False:
        foundletter = False
        end = x
        letters.append((start,end))    
    inletter=False
#print(letters)


#crop(box)-->imag()
count = 0
for letter in letters:
    m = hashlib.md5()
    im3 = im2.crop((letter[0] , 0, letter[1],im2.size[1]))
    guess = []

    for image in imageset:
        #for x,y in image.iteritems():
        for x,y in image.items():
            if len(y) != 0: # 通过余弦相似度来计算最大可能的值
                guess.append( ( V.relation(y[0],buildvector(im3)),x) )
    # 取出和当前字符最大概率匹配的样本集中的字符
    guess.sort(reverse=True)
    print(guess[0])
    count += 1

#box=[0,0,100,100]
#im_crop=im01.crop(box)
#print(im_crop.mode)
#print(im_crop.size)

















