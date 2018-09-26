from pymysql import *

class mysqlpython:
    def __init__(self,host,port,db,user,passwd,
                 charset="utf8"):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def open(self):
        self.conn = connect(host=self.host,port=
               self.port,db=self.db,user=self.user,
               passwd=self.passwd,
               charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def zhixing(self,sql):
        self.open()
        self.cursor.execute(sql)
        self.conn.commit()
        self.close()
        print("ok")














