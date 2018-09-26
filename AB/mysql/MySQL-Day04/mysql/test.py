from mysqlpython import mysqlpython

# 创建实例化对象
sqlh = mysqlpython("localhost",3306,"db2","root",
                   "123456")

sql_update = "update sheng set id=150 where id=1;"
sqlh.zhixing(sql_update)