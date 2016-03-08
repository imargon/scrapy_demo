#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import scrapy
import json
from spixiv.items import SpixivItem
reload(sys)
sys.setdefaultencoding('utf-8')

class PixivSpider(scrapy.Spider):
    """Spider for daily top illustrations on Pixiv
    """
    name = 'spixiv'
    allowed_domains = ['pixiv.net']
    start_urls = ["http://www.pixiv.net/ranking.php?mode=daily&amp%3Bcontent=illust&amp%3Bformat=json"]

    def parse(self, response):
        jsondata = json.loads(response.body)

        date = jsondata['date']
        for one in jsondata['contents']:
            item = SpixivItem()
            item['title'] = one['title']
            item['url'] = one['url']
            yield item