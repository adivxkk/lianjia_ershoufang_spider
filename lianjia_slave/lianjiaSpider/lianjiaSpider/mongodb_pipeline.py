from pymongo import MongoClient
from scrapy.conf import settings
from scrapy.exceptions import DropItem


# import scrapy.crawler.settings

class SingleMongodbPipeline(object):

    # def __init__(self):
    #     #初始化mongodb连接
    #     try:
    #         client = MongoClient(self.MONGODB_SERVER, self.MONGODB_PORT)
    #         self.db = client[self.MONGODB_DB]
    #     except Exception as e:
    #         traceback.print_exc()
    #
    # @classmethod
    # def from_crawler(cls, crawler):
    #     cls.MONGODB_SERVER = crawler.settings.get('SingleMONGODB_SERVER', '127.0.01')
    #     cls.MONGODB_PORT = crawler.settings.getint('SingleMONGODB_PORT', 27017)
    #     cls.MONGODB_DB = crawler.settings.get('SingleMONGODB_DB', 'maitian')
    #     pipe = cls()
    #     pipe.crawler = crawler
    #     return pipe
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        client = MongoClient(host=host, port=port)
        db = client[db_name]
        self.collection = db[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        if item['unit_price'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        if item['total_price'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        if item['huxing'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        if item['floor'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        if item['area'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        if item['huxing_struct'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        if item['inarea'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        if item['build_type'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        if item['direction'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        if item['build_struct'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        if item['decoration'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        if item['tihu'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        if item['warm_type'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        if item['elevator'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        if item['property_years'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        if item['region'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        if item['community'] == 0:
            raise DropItem("Duplicate item found: %s" % item)
        esfang_detail = {
            'title': item.get('title'),
            'targeturl': item.get('targeturl'),
            'unit_price': item.get('unit_price', ''),
            'total_price': item.get('total_price', ''),
            'region': item.get('region', ''),
            'community': item.get('community', ''),
            'huxing': item.get('huxing', ''),
            'floor': item.get('floor', ''),
            'area': item.get('area', ''),
            'huxing_struct': item.get('huxing_struct', ''),
            'inarea': item.get('inarea', ''),
            'build_type': item.get('build_type', ''),
            'direction': item.get('direction', ''),
            'build_struct': item.get('build_struct', ''),
            'decoration': item.get('decoration', ''),
            'tihu': item.get('tihu', ''),
            'warm_type': item.get('warm_type', ''),
            'elevator': item.get('elevator', ''),
            'property_years': item.get('property_years', ''),
        }
        try:
            self.collection.insert(esfang_detail)
            print('[success] the ' + item['targeturl'] + 'wrote to MongoDB database')
        except:
            pass
        return item
