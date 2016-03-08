# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

class LagouItem(scrapy.Item):
    companyName=scrapy.Field()
    companyShortName = scrapy.Field()
    city=scrapy.Field()
    industry=scrapy.Field()
    salary= scrapy.Field()
    workYear=scrapy.Field()
    education = scrapy.Field()


