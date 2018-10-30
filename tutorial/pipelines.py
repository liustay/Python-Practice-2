# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

str = ''

class TutorialPipeline(object):
    def __init__(self):
        self.client = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='123',
            db='test',
            charset='utf8'   
        )
        self.cur = self.client.cursor()
    def process_item(self, item, spider):
        sql = 'insert into testdb(number,title,`desc`,star,intro,link) VALUES (%s,%s,%s,%s,%s,%s)'
        lis = (item['number'],item['title'],item['desc'],item['star'],item['intro'],item['link'])
        self.cur.execute(sql,lis)
        self.client.commit()
        str+item['intro']
        print(str)
        return str
    