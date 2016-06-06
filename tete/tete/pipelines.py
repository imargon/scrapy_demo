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
from tete.items import TeteItem

import os
reload(sys)
sys.setdefaultencoding('utf-8')

# scrapy.contrib.pipeline.images.ImagesPipeline类的get_media_requests(item, info)会下载图片，
# 并把结果喂给item_completed()方法，结果是一个tuple，(success, image_info_or_failure)，
# 其中success是下载是否成功的bool，image_info_or_failure包括url、path和checksum三项。其中，path就是相对于IMAGES_STORE的路径（含文件名）。


class TetePipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         for image_url in item['image_urls']:
#             yield Request(image_url, meta={'item': item})
#
#     def file_path(self, request, response=None, info=None):
#         item = request.meta['item']
#         image_guid = request.url.split('/')[-1]
#         image_name = item['image_titles']+image_guid[-8:]
# #        image_name = item['image_titles']+str(item['image_prices'])+image_guid[-8:]
#
#         return image_name
#
#     def item_completed(self, results, item, info):
#
#         image_paths = [x['path'] for ok, x in results if ok]
#         if not image_paths:
#             raise DropItem('Items contains no images')
#         item['image_paths'] = image_paths
#         return item
          pass


        # item['image'] = []
        # for i in item['image_paths']:
        #     item['image'].append(item['image_titles']+i[-8:]) #截取倒数第8位到结尾
        # item['image_paths'] = item['image']

        # item['image'] = item['image_titles']+i
        # item['image'].append(item['image_titles']+i)
        # item['image_paths'].append(item['image_paths'])
        # os.rename("/test/"+str(i for i in item['image_paths']), "/test/" + str(n for n in range(1, len(item['image_paths'])))+item['image_titles'])

        # if item['image_id']:
        #     item['image_id'] = item['image_titles']+'.jpg'
        # os.rename("/test/"+image_paths[0], "/test/"+item['image_id'])


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
