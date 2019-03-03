import pandas as pd
import numpy as np
# 创建一组Series数据
# 1.创建Series
# s1=pd.Series([90,86,70],
#              index=['leo','kate','john'])
dict={'leo':90,'kate':86,'john':70}
s1=pd.Series(dict)
print(s1)
# print(s1[0])
# print(s1['kate'])
# print(s1[['kate','john']])
# print(s1[s1>80])

# 2.numpy中的ndarray：
s2=pd.Series(np.random.randn(5),
             index=['A','B','C','D','E'])
# print(s2)
# 3.数字创建
s3=pd.Series(6)
# print(s3)
# 4.创建一组DataFrame数据-date_range创建时间
date=pd.date_range('20100101',periods=6)
df=pd.DataFrame(np.random.randn(6,4),
                index=date,columns=list('abcd'))
# 访问a列
print(df.a)
print(df['a'])
# 访问a,b两列
print(df[['a','b']])
# 访问前四行
print(df[0:4])
print(df.head(4))

# 选取红色框中的数据
print(df.loc['2010-01-01':'2010-01-04',['a','b']])
print(df.iloc[:4,[0,1]])
print(df.ix[:4,['a','b']])