#用来获取数据库中gridfs的存储文件
from pymongo import MongoClient 
#和pymongo 绑定的
import gridfs 

conn = MongoClient('localhost',27017)
db = conn.grid 

#获取gridfs对象
fs = gridfs.GridFS(db)

#所有文件的游标
files = fs.find()
# print(files)
# print(files.count())
# 代表每个文件的对象
# for file in files:
#     print(file.filename)
for file in files:
    if file.filename == 'abc.mp3':
        with open(file.filename,'wb') as f:
            while True:
                #file的read()函数可以获取文件内容
                data = file.read(64)
                if not data:
                    break
                f.write(data)
conn.close()