# -*- coding: utf-8 -*-
import scrapy
import os
from fake_useragent import UserAgent
from scrapy.selector import Selector
from ..items import ScrapyforsantiItem

class SantiSpider(scrapy.Spider):
    name = 'santi'
    # allowed_domains = ['www.luoxia.com/santi/']
    # start_urls = ['https://www.luoxia.com/santi//']
    ChapterNum = 1
    def start_requests(self):
        url='https://www.luoxia.com/santi/'
        headers={
            'User-Agent': UserAgent().random
        }
        yield scrapy.Request(url, headers=headers)

    def parse(self, response):
        items = []
        # msg = response.body.decode()
        # with open("index.html",mode="w",encoding="utf-8") as file:
        #     file.write(msg)
        # self.log(msg)
        # bookNames = response.css('div>h3>a::attr(title)').extract()
        # bookNames = response.css('.title.clearfix').extract()
        bookChapters = response.css('div>ul>li')

        # for bookName in bookNames:
            # print("[bookname]=",bookName)
            # item=ScrapyforsantiItem()
        for bookChapter in bookChapters:
            item = ScrapyforsantiItem()
            # print("[ChapterName]=", bookChapter.css('[target=_blank]::attr(title)').extract_first())
            item['ChapterName'] = bookChapter.css('[target=_blank]::attr(title)').extract_first()
            if item['ChapterName']== None:
                item['ChapterName'] = bookChapter.css('li>b::attr(title)').extract_first()
            # print("[ChapterName]=", item['ChapterName'])

            # print("[ChapterUrl]=", bookChapter.css('[target=_blank]::attr(href)').extract_first())
            item['ChapterUrl'] = bookChapter.css('[target=_blank]::attr(href)').extract_first()
            if item['ChapterUrl']== None:
                item['ChapterUrl'] = bookChapter.css('li>b::attr(onclick)').extract_first()
                item['ChapterUrl'] = item['ChapterUrl'][item['ChapterUrl'].find(r'window.open("')+len(r'window.open("'):item['ChapterUrl'].find(r'")')]
            # print("[ChapterUrl]=", item['ChapterUrl'])

            item['ChapterNum'] = self.ChapterNum
            self.ChapterNum += 1
            items.append(item)

        for item in items:
            yield scrapy.Request(url=item['ChapterUrl'], meta={'item': item}, dont_filter=True, callback=self.parse2)
        pass

    def parse2(self,response):
        # msg = response.body.decode()
        # print("[ChapterHtmlContent]=",msg)
        # with open("content.html",mode="w",encoding="utf-8") as file:
        #     file.write(msg)
        msg = response.meta['item']
        chpcon = ''
        # print('[ChapterName]=', msg)

        ChaptersContent_lv1 = response.css('#nr1>p::text').extract()
        # ChaptersContent_lv2 = ChaptersContent_lv1.css('')
        for content in ChaptersContent_lv1:
            chpcon = chpcon + '\n' + content
        item = ScrapyforsantiItem()

        item['ChapterContent'] = chpcon
        # print('[ChapterContent]=',content)
        item['ChapterName'] = msg['ChapterName']
        item['ChapterNum'] = msg['ChapterNum']
        yield item