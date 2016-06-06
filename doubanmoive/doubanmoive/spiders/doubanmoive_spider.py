#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
#scrapy crawl doubanmoive -o items.json -t json
__author__ = 'zhen'

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
#from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors  import LinkExtractor
from doubanmoive.items import DoubanmoiveItem

class MoiveSpider(CrawlSpider):
    name="doubanmoive"
    allowed_domains=["movie.douban.com"]
    start_urls=["http://movie.douban.com/top250"]
    rules=[
        Rule(LinkExtractor(allow=(r'http://movie.douban.com/top250\?start=\d+.*'))),
        Rule(LinkExtractor(allow=(r'http://movie.douban.com/subject/\d+')),callback="parse_item"),
    ]

    def parse_item(self,response):
        sel=Selector(response)
        name = sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        director = sel.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        classification = sel.xpath('//*[@id="info"]/span[6]/text()').extract() #//*[@id="info"]/span[6]//*[@id="info"]/span[4]
        actor = sel.xpath('//*[@id="info"]/span[3]/span[2]/a/text()').extract()

        item=DoubanmoiveItem()
        item['name']=[n.encode('utf-8') for n in name]
        item['year']=sel.xpath('//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)') #//*[@id="content"]/h1/span[2]
        item['score']=sel.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()
        item['director']= [n.encode('utf-8') for n in director]
        item['classification']= [n.encode('utf-8') for n in classification]
        item['actor']= [n.encode('utf-8') for n in actor]

        yield item

