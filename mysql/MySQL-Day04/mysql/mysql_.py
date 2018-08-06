import pymysql

#1.创建数据库连接
db = pymysql.connect("localhost","root","123456",
                     "db2",charset="utf8")
#2.创建游标对象
cursor = db.cursor()

#3.利用游标对象cursor的方法来操作数据库
cursor.execute("insert into sheng values(3,200000,\
                '四川省');")

cursor.execute("insert into sheng\
 values(4,200001,'日本省');")
#4.提交到数据库commit
db.commit()
#5.关闭游标对象
cursor.close()
#6.关闭数据库连接
db.close()

















