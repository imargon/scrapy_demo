#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import requests
from lxml import html

reload(sys)
sys.setdefaultencoding('utf-8')
headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "www.zhihu.com",
        "Referer": "www.zhihu.com/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2723.2 Safari/537.36"
 }

session = requests.session()
#@id_url = 'https://www.zhihu.com/people/weizhi-xiazhi/answers'
id_url = 'https://www.zhihu.com/people/zheng-wei-yang-01/'
host_url = 'https://www.zhihu.com'
login_url = host_url+'/login/email'
response = session.get(url=host_url, headers=headers)


def zhihu_login(email, passwd):
    login_data = {
            '_xsrf': response.cookies['_xsrf'],
            'email': '000@gmail.com',
            'password': '0000',
            'remember_me': 'true'
    }

    login_post = session.post(login_url, data=login_data, headers=headers)

    # print login_post.json()['msg'], login_post.status_code, login_post.raise_for_status(),
    # login_post.url, login_post.history

    print login_post.json()
    if login_post.json()['r'] == 1:
        print 'Login Failed:'+login_post.json()['msg']
    else:
        print login_post.json()['msg']

    # print login_post.text

    # print id_html.text.encode('utf-8')
    # zhihu_file = open('D:/py/py_learn/zhihu1.html', 'w')
    # zhihu_file.write(id_html.text.encode('utf-8'))


def parse_page():
    id_html = session.get(url=id_url, headers=headers, verify=False)
    id_html = html.fromstring(id_html.text.encode('utf-8'))
    print id_html.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[1]/h1/span[1]/text()')
    print id_html.xpath('//*[@id="root"]/div/main/div/div/div[2]/div[2]/div[1]/div/a[1]/div[2]/text()')
    print id_html.xpath('//*[@id="root"]/div/main/div/div/div[2]/div[2]/div[1]/div/a[2]/div[2]/text()')
    print id_html.xpath('//*[@id="root"]/div/main/div/div/div[2]/div[2]/div[1]/div/text()')
    print id_html.xpath('//div[@class="zm-profile-side-following zg-clear"]/a[@class="item"]/strong/text()')
    print id_html.xpath('//*[@id="zh-profile-follows-list"]/div/div/a/@href')
    print id_html.xpath('//span[@class="location item"]/@title/text()')

if __name__ == "__main__":
    zhihu_login('xxxxx@gmail.com', '123123')
    parse_page()
