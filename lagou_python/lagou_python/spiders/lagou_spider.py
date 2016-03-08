#coding:utf-8
__author__ = 'sniper.geek'

import re
import json
from scrapy.selector import Selector
from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from lagou_python.items import LagouPythonItem
from scrapy import log
from scrapy.http import Request

class LagouSpider(CrawlSpider):
    name = "lagou"

    download_delay = 2
    allowed_domains = ["lagou.com"]
    start_urls = [
        "http://www.lagou.com/jobs/list_Python?kd=Python&spc=1&pl=&gj=&xl=&yx=&gx=&st=&labelWords=&lc=&workAddress=&city=%E4%B8%8A%E6%B5%B7&requestId=&pn=1"
    ]
    #rules = [
    #    Rule(sle(allow=("/jobs/list_Python?kd=Python&spc=1&pl=&gj=&xl=&yx=&gx=&st=&labelWords=&lc=&workAddress=&city=%E4%B8%8A%E6%B5%B7&requestId=&pn=\d{1}")),follow=True,callback='parse_item')
    #    Rule(sle(),follow=True,callback='parse_item')
    #
    #]

    def parse(self,response):
        log.msg("Fetch page: %s"%response.url)
        #items = []
        sel = Selector(response)
        sites = sel.xpath('//div[@class="content"]/ul[@class="hot_pos reset"]/li')
        total_page_value = sel.xpath('//div[@class="Pagination myself"]/a[@href="#"][last()]/@title').extract()
        log.msg("total_page_value: %s"%total_page_value)
        total_page = int(total_page_value[0])
        log.msg("page_number: %s"%total_page)
        for site in sites:
            item = LagouPythonItem()
            item['salary'] =site.xpath('div[@class="hot_pos_l"]/span[1]/text()').extract()
            item['experience'] =site.xpath('div[@class="hot_pos_l"]/span[2]/text()').extract()
            item['education'] =site.xpath('div[@class="hot_pos_l"]/span[3]/text()').extract()
            item['occupation_temptation'] =site.xpath('div[@class="hot_pos_l"]/span[4]/text()').extract()
            if len(site.xpath('div[@class="hot_pos_r"]/span')) ==3:
                item['job_fields'] = site.xpath('div[@class="hot_pos_r"]/span[1]/text()').extract()
                item['stage'] = site.xpath('div[@class="hot_pos_r"]/span[2]/text()').extract()
                item['scale'] = site.xpath('div[@class="hot_pos_r"]/span[3]/text()').extract()
                item['company'] =site.xpath('div[@class="hot_pos_r"]/div[@class="mb10"]/a/text()').extract()
                item['url'] = site.xpath('div[@class="hot_pos_r"]/div[@class="mb10"]/a/@href').extract()
                item['founder']=[]
            else:
                item['job_fields'] = site.xpath('div[@class="hot_pos_r"]/span[1]/text()').extract()
                item['founder'] = site.xpath('div[@class="hot_pos_r"]/span[2]/text()').extract()
                item['stage'] = site.xpath('div[@class="hot_pos_r"]/span[3]/text()').extract()
                item['scale'] = site.xpath('div[@class="hot_pos_r"]/span[4]/text()').extract()
                item['company'] =site.xpath('div[@class="hot_pos_r"]/div[@class="mb10"]/a/text()').extract()
                item['url'] = site.xpath('div[@class="hot_pos_r"]/div[@class="mb10"]/a/@href').extract()
            yield item
        next_urls=[]
        for k in xrange(2,total_page+1):
            base_url = "http://www.lagou.com/jobs/list_Python?kd=Python&spc=1&pl=&gj=&xl=&yx=&gx=&st=&labelWords=&lc=&workAddress=&city=%E4%B8%8A%E6%B5%B7&requestId=&pn="+str(k)
            next_urls.append(base_url)
        for next_url in next_urls:
            #log.msg("Next page:%s"%next_url, level=log.INFO)
            yield Request(next_url,callback=self.parse)