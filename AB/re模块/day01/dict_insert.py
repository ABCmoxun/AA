import pymysql 
import re 

f = open('dict.txt')
db = pymysql.connect\
('localhost','root','123456','dict')
cursor = db.cursor()

for line in f:
    l = re.split('[ ]+',line)
    sql = "insert into words (word,interpret) values ('%s','%s')"\
    %(l[0],' '.join(l[1:]))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
f.close()