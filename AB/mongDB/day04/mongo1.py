#索引和聚合操作演示
from pymongo import MongoClient,IndexModel 

conn = MongoClient('localhost',27017)
db = conn.stu 
my_set = db.class3 

#创建索引

# index = my_set.ensure_index('name')
# #返回索引名称
# print(index)

# 复合索引
# index = my_set.ensure_index\
# ([('name',1),('King',-1)])
# print(index)

cls = db.class0
# 唯一索引和稀疏索引
# index = cls.ensure_index('name',unique=True)
# print(index)
# index = my_set.ensure_index\
# ('king_name',sparse = True)
# print(index)

#　删除一个索引
# my_set.drop_index('name_1')
#　删除全部索引
# my_set.drop_indexes()

#同时创建多个索引
# index1 = IndexModel([('name',1),('King',-1)])
# index2 = IndexModel([('king_name',1)])
# indexes = my_set.create_indexes([index1,index2])

#查看一个集合中的索引
# for i in my_set.list_indexes():
#     print(i)

#聚合管道

l =[{'$group':{'_id':'$King','count':{'$sum':1}}},
    {'$match':{'count':{'$gt':1}}}
   ]
cursor = my_set.aggregate(l)
for i in cursor:
    print(i)
