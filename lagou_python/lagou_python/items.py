# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouPythonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    salary = scrapy.Field()
    experience = scrapy.Field()
    education = scrapy.Field()
    occupation_temptation = scrapy.Field()
    job_fields = scrapy.Field()
    stage = scrapy.Field()
    scale = scrapy.Field()
    company = scrapy.Field()
    url = scrapy.Field()
    founder = scrapy.Field()
    index = scrapy.Field()