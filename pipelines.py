# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
from pymongo import MongoClient
from zhihu.settings import mongo_url, project_dir
from zhihu.items import ZhihuPeopleItem, ZhihuRelationItem
from zhihu.tools.async import download_pic


class ZhihuPipeline(object):

    def __init__(self, mongo_url, mongo_db, image_dir):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db
        self.image_dir = image_dir
        self.client = None
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url=mongo_url,
            mongo_db='zhihu',
            image_dir=os.path.join(project_dir, 'images')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]
        if not os.path.exists(self.image_dir):
            os.mkdir(self.image_dir)

    def close_spider(self, spider):
        self.client.close()

    def process_people(self, item):
        collection = self.db['zhihu']
        zhihu_id = item['zhihu_id']
        collection.update({'zhihu_id': zhihu_id}, dict(item), upsert=True)

    def process_relation(self, item):
        collection = self.db['relation']
        data = collection.find_one({'zhihu_id': item['zhihu_id']})
        if not data:
            self.db['relation'].insert(dict(item))

    def process_item(self, item, spider):

        if isinstance(item, ZhihuPeopleItem):
            self.process_people(item)
        elif isinstance(item, ZhihuRelationItem):
            self.process_relation(item)
        return item
