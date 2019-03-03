import numpy as np
import pandas as pd
# 获取电影数据表格
users = pd.read_table('users.dat',header=None,names=['UserID','Gender','Age','Occupation','Zip-code'], sep='::',engine= 'python')
print(users.head())
#获取csv文件,定义列名为width,height,category
csv=pd.read_csv('iris.csv',header=None,
                names=['width','height','category'])
print(csv.head())
csv.drop(labels=0,axis=0,inplace=True)
csv.to_csv('iris1.csv')
#获取表格文件
excel=pd.read_excel('data.xlsx')
print(excel)


