# -*- coding:utf-8 -*-
"""
# pan.baidu.com/s/1hs0mXDi--+--：xaag
"""
http://185.38.13.159//mp43/254044.
mp4?st=QL4suvr8wYLJHtlK7hqfxw&e=1519120247


from __future__ import unicode_literals
import sys
import json
import requests
reload(sys)
sys.setdefaultencoding('utf-8')

__url = 'http://www.lagou.com/jobs/positionAjax.json?px=default&first=true&kd=python&pn=1'


def get_positions():
    """"""
    r = requests.get(url=__url)
    if 200 != r.status_code:
        return
    try:
        content = json.loads(r.content,encoding='utf-8')
    except ValueError as e:
        return
#    print content
    results = content['content']['result']
    items = list()
    for result in results:
        item = dict()
        item['companyName'] = result['companyName']
        item['city'] = result['city']
        item['industry'] = result['industryField']
        item['salary'] = result['salary']
        items.append(item)
        print item
    return items

if __name__ == '__main__':
    get_positions()
