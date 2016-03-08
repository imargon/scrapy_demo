#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
from scrapy import Spider
from bs4 import BeautifulSoup
from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider,Rule
from scrapy.http import Request
from weather.items import WeatherItem

reload(sys)
sys.setdefaultencoding('utf-8')


class WeatherSpider(CrawlSpider):
    name = "weather"
    allowed_domains =["sina.com.cn"]
    start_urls = ['http://weather.sina.com.cn']

    def parse(self, response):
        item = WeatherItem()
        html_doc = response.body
        soup = BeautifulSoup(html_doc)
        itemTemp = {}
        itemTemp['city'] = soup.find(id='silder_ct_name')
        tenDay =soup.find(id='blk_fc_c0_scroll')
        itemTemp['date']=tenDay.findAll("P",{"class":'wt_fc_c0_i_date'})
        itemTemp['dayDesc']=tenDay.findAll("img",{"class":'icons_wt'})
        itemTemp['dayTemp']=tenDay.findAll("p",{"class":'wt_fc_c0_i_temp'})

        for att in itemTemp:
            item[att] = []
            if att == 'city':
                item[att] = itemTemp.get(att).text
                continue
            for obj in itemTemp.get(att):
                if att == 'dayDesc':
                    item[att].append(obj['title'])
                else:
                    item[att].append(obj.text)
        return item
