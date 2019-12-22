# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyforsantiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ChapterName = scrapy.Field()
    ChapterUrl = scrapy.Field()
    ChapterFileName = scrapy.Field()
    ChapterContent = scrapy.Field()
    ChapterNum = scrapy.Field()
    pass
