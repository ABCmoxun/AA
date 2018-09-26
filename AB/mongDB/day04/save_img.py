#将文件以二进制存储到数据库
from pymongo import MongoClient
import bson.binary 

conn = MongoClient('localhost',27017)
db = conn.file 
my_set = db.img  

# #存储　
# f = open('img.jpg','rb')
# #将读取的二进制流变为　bson格式二进制的字串
# content = bson.binary.Binary(f.read())

# my_set.insert({'filename':'img.jpg',\
#     'data':content})

#提取文件
data = my_set.find_one({'filename':'img.jpg'})

#直接通过字典的方式获取内容进行写入即可
with open(data['filename'],'wb') as f:
    f.write(data['data'])


conn.close()