# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


#信息输出(不用设置pipeline)
# 保存json格式:scra py crawl 爬虫名 -o test.json
# 保存csv格式: scra py crawl 爬虫名 -o test.csv
# 提取信息保存在文件中(还要在settings里设置)
# ITEM_PIPELINES = {
#     'webCrawler_scrapy.pipelines.WebcrawlerScrapyPipeline': 301,#保存到mysql数据库
#     'webCrawler_scrapy.pipelines.JsonWithEncodingPipeline': 300,#保存到文件中
# }


from ABC.settings import mongo_host,mongo_port,mongo_db_name,mongo_db_collection
import pymongo
#import pymysql

class AbcPipeline(object):
    def process_item(self, item, spider):
        #相关信息
        #(1)保存到Json中
        """
        with open("tencent.json", "ab") as f:
            text = json.dumps(dict(item), ensure_ascii=False)+'\n'
            f.write(text.encode('utf-8'))"""
        return item

#-----------------------------------
#(1)mongodb数据库中
# class AbcPipeline(object):
#     def __init__(self):
#         host=mongo_host
#         port=mongo_port
#         dbname=mongo_db_name
#         sheetname=mongo_db_collection
#         client=pymongo.MongoClient(host=host,port=port)
#         mydb=client[dbname]
#         self.port=mydb[sheetname]

#     def process_item(self, item, spider):
#         data=dict(item)
#         self.port.insert(data)
#         return item


#(1)mysql数据库中
#from ABC.settings import mysql_host,mysql_port,
#import pymysql
# class AbcPipeline(object):
#     def __init__(self):
            # host=mysql_host,
            # port=mysql_port, 
            # db=mysql_dbname,
            # user=mysql_user,
            # passwd=mysql_passwrd,
            # charset='utf8'

#         conn=pymysql.connect(host=host,port=port,user=user,...)
#         cur = db.cursor()
          # sql=''
#         self.port=mydb[sheetname]

#     def process_item(self, item, spider):
#         data=dict(item)
#         self.port.insert(data)
#         return item