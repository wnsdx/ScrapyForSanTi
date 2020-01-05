# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class ScrapyforsantiPipeline(object):
    def process_item(self, item, spider):
        curPath = os.getcwd()
        loadPath=curPath+os.path.sep+r'download'
        if not os.path.exists(loadPath):
            os.makedirs(loadPath)

        filename_path = loadPath+os.path.sep+str(item['ChapterNum'])+'-'+str(item['ChapterName'])+'.txt'
        with open(filename_path, 'w', encoding='utf-8') as f:
            f.write(item['ChapterContent'] + "\n")
        # print("[pipeline]=",curPath,item)
        return item

import pymysql.cursors
class MySQLPipeline(object):
    def __init__(self):
        # connect to datebase
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='novel',
            user='root',
            passwd='root',
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()

    def process_item(self,item,spider):
        self.cursor.execute(
            """insert into santi(chapter,content)
            value(%s,%s)""",(str(item['ChapterNum'])+'-'+str(item['ChapterName']),(item['ChapterContent'] + "\n"))
        )
        self.connect.commit()
        return item
        pass

