import pymysql

db = pymysql.connect("localhost","root","123456",
                     "db2",charset="utf8")
cur = db.cursor()

try:
    cur.execute("update CCB set money=5000 where \
                 name='Zhuanqian';")
    cur.execute("update ICBC set money=9000 where \
                 name='Shouqian';")
    db.commit()
    print("ok")
except Exception as e:

    db.rollback()
    print("出现错误，已回滚")
    

cur.close()
db.close()



















