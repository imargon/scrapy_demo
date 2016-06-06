#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import os
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from tete.items import TeteItem

reload(sys)
sys.setdefaultencoding('utf-8')


class TeteSpider(CrawlSpider):
    name = "tete"
    allowed_domains = ["tete365.com"]
#    start_urls = ['http://www.tete365.com/product/getinsaleproducts/?category_id3=800200102']
#    start_urls = ['http://www.tete365.com/product/getinsaleproducts/?category_id3=800200102&currentPage=%d' % i for i in range(1,30)]
    start_urls = ['http://www.tete365.com/product/productdetail/1102464/1100386.html']
#    start_urls = ['http://www.tete365.com/']
    rules = [
         Rule(LinkExtractor(allow=('http://www.tete365.com/product/productdetail/\d+/\d+\.html')), callback="parse_image"),
         Rule(LinkExtractor(deny=('/1104251/1102559\.html', '/1104490/1102932\.html', '/1102917/1100836\.html',
                                  '/1102120/1100061\.html', '/1104256/1102570\.html', '/1102090/1100032\.html')))]

    def parse_image(self, response):

        sel = Selector(response)
#        image_url = sel.css('img').xpath('@src').extract()
        image_title = "".join(sel.xpath('//*[@id="product-intro"]/h1/text()').extract()[0].strip().split())
#        image_price = "".join(str(sel.xpath('//*[@id="member_real_lavel"]/p/i/span/text()').extract()[0]).strip().split())
        image_price = sel.xpath('//*[@id="member_real_lavel"]/p/i/text()').extract()
        if image_price:            
            image_price = sel.xpath('//*[@id="member_real_lavel"]/p/i/text()').extract()
        else:            
            image_price = sel.xpath('//*[@id="member_real_lavel"]/p/i/span/text()').extract()
            
#                                '//*[@id="member_real_lavel"]/p/i/span'
        # image_title = "".join(image_title.split()) /*去除空格与换行*/
#       log.msg("This is a warning", level=log.WARNING)
        item = TeteItem()
#       item['image_urls'] = image_url
        item['image_titles'] = image_title
        item['image_prices'] = image_price
        print item['image_prices']

        yield item

    # CTRL + /