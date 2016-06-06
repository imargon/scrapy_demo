# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

class DoubanmoiveItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class DoubanmoiveItem(Item):
    name=Field()#电影名
    year=Field()#上映年份
    score=Field()#豆瓣分数
    director=Field()#导演
    classification=Field()#分类
    actor=Field()#演员