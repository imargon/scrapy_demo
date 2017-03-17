#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest
from zhihu.items import ZhihuPeopleItem, ZhihuRelationItem
from zhihu.constants import Gender, People, HEADER, Cookie
from zhihu.settings import DEFAULT_REQUEST_HEADERS


class ZhihuSipder(CrawlSpider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_url = "https://www.zhihu.com/people/linan"

    def __init__(self, *args, **kwargs):
        super(ZhihuSipder, self).__init__(*args, **kwargs)
        self.xsrf = ''
        self.headers = HEADER
        self.cookies = Cookie

    def start_requests(self):
        return [Request("https://www.zhihu.com/#signin", meta={'cookiejar': 1}, callback=self.post_login, headers=HEADER, cookies=self.cookies )]

    def post_login(self, response):
        self.xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
        # session = requests.session()
        # response_page = session.get(url='https://www.zhihu.com', headers=DEFAULT_REQUEST_HEADERS)
        return [FormRequest('https://www.zhihu.com/login/email', method='POST',
                            meta={'cookiejar': response.meta['cookiejar']},
                            formdata={'_xsrf': self.xsrf,
                            'email': '00000@mail.com',
                            'password': '00000',
                            'remember_me': 'true'},
                            headers=self.headers,
                            callback=self.after_login,
                            dont_filter=True)]

    def after_login(self, response):
        self.headers['X-Xsrftoken'] = self.xsrf
        self.headers['X-Requested-With'] = 'XMLHttpRequest'
        return [Request(self.start_url, meta={'cookiejar': response.meta['cookiejar']}, callback=self.parse_people, headers=HEADER)]

    def parse_people(self, response):
        zhihu_url = "https://www.zhihu.com/people/"
        sel = Selector(response)
        nickname = sel.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[1]/h1/span[1]/text()').extract()[0]
        zhihu_id = response.url.split('/')[-1]
        following_urls = zhihu_url+zhihu_id+'/'
        following_num = sel.xpath('//*[@id="root"]/div/main/div/div/div[2]/div[2]/div[2]/div[1]/a[1]/div[2]/text()').extract()[0]
        follower_num = sel.xpath('//*[@id="root"]/div/main/div/div/div[2]/div[2]/div[2]/div[1]/a[2]/div[2]/text()').extract()[0]
        image_url = sel.xpath('//img/@src')[1].extract()

# 生成页码
        following_num = int(following_num) if following_num else 0
        page_num = following_num/20
        page_num += 2 if following_num % 20 else 0
        page_url = ['following?page=%d' % i for i in xrange(1, page_num)]
        following_urls = map(lambda url: following_urls+url,  page_url)
        for following_url in following_urls:
            yield Request(following_url, method='next', meta={'cookiejar': response.meta['cookiejar']}, callback=self.parse_following, headers=HEADER)

        item = ZhihuPeopleItem()
        item['nickname'] = nickname,
        item['zhihu_id'] = zhihu_id,
        item['following_num'] = following_num,
        item['follower_num'] = follower_num,
        item['image_url'] = image_url
        yield item

    def parse_following(self, response):
        following_ids = []
        zhihu_url = "https://www.zhihu.com/people/"
        sel = Selector(response)
        # 将followering 和follower 的ID生成列表
        following_ids = sel.xpath('//span[@class="UserLink UserItem-name"]//a[@class="UserLink-link"]/@href').extract()
        following_ids.append(following_ids)
        following_id = [following_id.split('/')[-1] for following_id in following_ids]
        following_urls1 = map(lambda id: zhihu_url+id, following_id)
        for urls in following_urls1:
            yield Request(urls, meta={'cookiejar': response.meta['cookiejar']}, callback=self.parse_people, headers=HEADER)
        item = ZhihuRelationItem()
        item['following_id'] = following_id
        yield item

    # def parse_err(self, response):
    #     log.ERROR('crawl {} failed'.format(response.url))