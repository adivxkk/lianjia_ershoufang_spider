# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo
class LianjiaspiderPipeline(object):
    # def __init__(self):
    #     host = settings['MONGODB_HOST']
    #     port = settings['MONGODB_PORT']
    #     db_name = settings['MONGODB_DBNAME']
    #     client = pymongo.MongoClient(host=host, port=port)
    #     db = client[db_name]
    #     self.collection = db[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        # ershoufang = dict(item)
        # self.collection.insert(ershoufang)
        return item
