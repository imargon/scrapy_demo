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
from wukong.items import WukongItem
reload(sys)
sys.setdefaultencoding('utf-8')


class WukongSpider(CrawlSpider):
    name ='wukong'
    allowed_domains = ["swokon.com"]
    start_urls = ['http://www.swokon.com/']
    rules = [
        Rule(LinkExtractor(allow=('http://www.swokon.com/category*')), follow=True),
        Rule(LinkExtractor(deny=('cn357.com', 'taobao.com', '1688.com')), callback="parse_image")]

    def parse_image(self,response):
        sel = Selector(response)
        image_title = sel.xpath('//*[@id="cmFormbuy"]/h1/text()').extract()[0]
        image_price = sel.xpath('//*[@id="cmIDSHOPPRICE"]/text()').extract()
        image_url = sel.css('img').xpath('@src').extract()
        image_url = [a1 for a1 in image_url if a1[0:21] == '/images/upload/Image/']
        image_url = map(lambda url: 'http://www.swokon.com/'+url, image_url)
        
   #      sel.xpath('//img/@src').re(r'[^/]*.[jpg|png|gif]$') #正则过滤图片，不能加extract()
   #      sel.xpath('//a[contains(@src,"/images/upload/Image/DSC_6912(1).jpg")]/img/@src').extract()
   # response.xpath('//a[contains(@href, "image")]/img/@src').extract()
        
        
# sel.xpath('//img[contains(@src,'/images/upload/Image/DS*')]/@src').extract()        
# // *[@id="cmItemTab_v"]/div[1]/strong/div/font/img[1]
# // img[contains(@src,'/images/upload/Image/DSC*.JPG')]/@src
# // response.xpath('//img[contains(@src, "/images/upload/Image/DSC*.JPG")]').extract()
# src="/images/upload/Image/DSC_8765.JPG"
        item = WukongItem()
        item['image_titles'] = image_title
        item['image_prices'] = image_price
        item['image_urls'] = image_url
        yield item