import pandas as pd

#读取电影详情表 movies
movies=pd.read_table('movies.dat',header=None,
                     names=['MovieID', 'Title', 'Genres']
                     ,sep='::',engine='python')
print(movies.head())
#读取评分表 Ratings
Ratings=pd.read_table('ratings.dat',sep='::'
                      ,engine='python',header=None,
                      names=['UserID', 'MovieID',
                             'Rating', 'Timestamp'])
print(Ratings.head())
# 读取test.csv表格
test=pd.read_csv('test.csv')
print(test.head())
print(test.info())
print(test.describe())
# PassengerId => 乘客ID
# Pclass => 乘客等级(1/2/3等舱位)
# Name => 乘客姓名
# Sex => 性别
# Age => 年龄
# SibSp => 堂兄弟/妹个数
# Parch => 父母与小孩个数
# Ticket => 船票信息
# Fare => 票价
# Cabin => 客舱
# Embarked => 登船港口

