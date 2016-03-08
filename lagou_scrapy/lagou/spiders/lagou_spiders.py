#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json
import sys
import re
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors  import LinkExtractor
from lagou.items import LagouItem
from scrapy.http import Request

#from scrapy import log


reload(sys)
sys.setdefaultencoding('utf-8')


class LagouSpider(CrawlSpider):
    name = "lagou"
    allowed_domains =["www.lagou.com/jobs/"]
    start_urls =["http://www.lagou.com/jobs/positionAjax.json?px=default&first=true&kd=python&pn=1"]
    # rules = [
    #      Rule(LinkExtractor(allow=(r'http://www.lagou.com/jobs/\d+')),callback='parse')
    # ]

    def parse(self,response):
        #log.msg("Fetch page: %s"%response.url,level=log.INFO)

#       json_data = json.loads(response.body.body_as_unicode().replace('\r\n','').replace('\n',''),encoding='UTF-8')
        json_data = json.loads(response.body,encoding='UTF-8') #json_datas是个字典
        #items= list()
        results = json_data['content']['result'] #results 已经是列表了
        for result in results:
            item = LagouItem()
            item["companyName"] = result["companyName"]
            item["city"] = result["city"]
            item["industry"] = result["industryField"]
            item["salary"] = result["salary"]
            #print result["companyName"]
#            print item
            yield item
        next_urls=[]
        for pn in xrange(2,79):
           base_url="http://www.lagou.com/jobs/positionAjax.json?px=default&first=false&kd=python&pn="+str(pn)
           next_urls.append(base_url)

        for next_url in next_urls:
           yield Request(next_url,callback=self.parse, dont_filter=True) #停用过滤功能
#         要request的地址和allow_domain里面的冲突，从而被过滤掉。可以停用过滤功能
#         print item["city"]
#       jsonresponse = json.dumps(jsonresponse,ensure_ascii=False,indent=1)

#       sel = Selector(json_data=response.body)
#       json_data = sel.xpath('//html/body/p/text()').extract()






