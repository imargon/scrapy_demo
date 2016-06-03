# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from __future__ import unicode_literals
import sys
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
from wukong.items import WukongItem

reload(sys)
sys.setdefaultencoding('utf-8')


class WukongPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url, meta={'item': item})
        
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Items contains no images')
        item['image_paths'] = image_paths
        return item
        
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_guid = request.url.split('/')[-1]
        image_name = item['image_titles']+image_guid[-8:]
        # image_name = item['image_titles']+str(item['image_prices'])+image_guid[-8:]
        return image_name

    # def process_item(self, item, spider):
    #     return item

# url去重


class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['image_titles'] in self.ids_seen:
            raise DropItem("Duplicates item found: %s" % item)
        else:
            self.ids_seen.add(item['image_titles'])
            return item