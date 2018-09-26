#通过pymongo 进行增删改查
from pymongo import MongoClient 

#创建连接对象
conn = MongoClient('localhost',27017)

#创建集合对象和数据库对象
# db = conn.stu 
# my_set = db.class3 
# __getitem__   __setitem__
db = conn['stu']
my_set = db['class3']

# print(my_set)
# print(dir(my_set))

#插入数据
# my_set.insert({'name':'张铁林','King':'乾隆'})
# my_set.insert([{'name':'陈道明','King':'康熙'},\
#     {'name':'张国立','King':'康熙'}])
# my_set.insert_many([{'name':'唐国强','King':'雍正'},\
#     {'name':'陈建斌','King':'雍正'}])
# my_set.insert_one({'name':'郑少秋','King':'乾隆'})
# my_set.save({'name':'吴奇隆','King':'四爷'})

#数据删除
# my_set.remove({'name':'吴奇隆'})

#只删除第一条符合条件文档
# my_set.remove({'name':'陈道明'},multi = False)
#删除所有文档
# my_set.remove()

#查找操作
# cursor = my_set.find({},{'_id':0})

# for i in cursor:
#     print(i['name'],'----',i['King'])

cls = db.class0 

#使用到修改器用字符串表示
# cursor = cls.find({'gender':{'$exists':True}},\
#     {'_id':0})

# for i in cursor:
#     print(i)
# print(cursor)
# print(cursor.next())
# print(cursor.count())
# for i in cursor.skip(2).limit(3):
#     print(i)

# for i in cursor.sort([('name',1)]):
#     print(i)

# dic = {'$or':[{'name':{'$gt':'Tom'}},\
# {'gender':'w'}]}

# data = cls.find_one(dic)
# print(data)

# 修改操作
# my_set.update({'name':'张国立'},\
#     {'$set':{'name':'国立'}})

#如果文档不存在则插入
# my_set.update({'name':'冰冰'},\
#     {'$set':{'King':'武则天'}},upsert = True)

#修改多条文档
# my_set.update({'King':'康熙'},\
#     {'$set':{'king_name':'玄烨'}},multi = True)

# my_set.update_many({'King':'雍正'},\
#     {'$set':{'king_name':'胤禛'}})

# my_set.update_one({'king_name':None},\
#     {'$set':{'king_name':'弘历'}})

#查找并删除，查找结果会返回
print(my_set.find_one_and_delete({'name':'冰冰'}))

conn.close()
