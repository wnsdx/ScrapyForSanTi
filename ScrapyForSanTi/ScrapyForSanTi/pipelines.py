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
