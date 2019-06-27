from scrapy_redis.spiders import RedisSpider
from lianjiaSpider.items import LianjiaspiderItem

from scrapy.selector import Selector
import scrapy
import re


class LianjiaSpider(RedisSpider):
    name = 'lianjiaSpider'
    # start_urls = ["https://zz.lianjia.com/ershoufang/104102228217.html"]
    # start_urls = ["https://zz.lianjia.com/ershoufang/104102082370.html"]
    # start_urls请求改为从redis_key中获得requests
    redis_key = 'kk_esfang:requests'

    def parse(self, response):
        lianjiaItem = LianjiaspiderItem()
        # response_url = re.findall(r'^http://\w+..com', response.url)
        response_url = re.findall(r'https://zz.lianjia.com/ershoufang/\d+.html', response.url)[0]
        try:
            lianjiaItem['targeturl'] = response_url
        except:
            lianjiaItem['targeturl'] = '无'
        response_selector = Selector(response)
        # 字段提取
        # title = response_selector.xpath('//div[@class="title"]/h1[@class="main"]/text()').extract()
        # 因为生产的是一个列表，所以需要加[0]取第一个字符串
        title = response_selector.xpath('//div[@class="title"]/h1[@class="main"]/text()').extract()[0].replace(' ', '.')
        if title:
            lianjiaItem['title'] = title
        unitPrice_data = response_selector.xpath('//div[@class="text"]/div[@class="unitPrice"]/span')[0]
        unit_price = unitPrice_data.xpath('string(.)').extract()[0]
        try:
            lianjiaItem['unit_price'] = unit_price
        except:
            lianjiaItem['unit_price'] = 0
        total_price = \
            response_selector.xpath('//div[@class="content"]/div[contains(@class,"price")]/span/text()').extract()[
                0] + '万'
        try:
            lianjiaItem['total_price'] = total_price
        except:
            lianjiaItem['total_price'] = 0
        li_list = response_selector.xpath(
            '//div[@id="introduction"]//div[@class="base"]/div[contains(@class,"content")]/ul/li/text()').extract()

        huxing, floor, area, huxing_struct, inarea, build_type, direction, build_struct, decoration, tihu, warm_type, elevator, property_years = li_list
        region = response_selector.xpath(
            '//div[contains(@class,"areaName")]/span[contains(@class,"info")]/a[1]/text()').extract()[0]
        community = response_selector.xpath('//div[contains(@class,"communityName")]/a[1]/text()').extract()[0]
        try:
            lianjiaItem['community'] = community
        except:
            lianjiaItem['community'] = 0
        try:
            lianjiaItem['region'] = region
        except:
            lianjiaItem['region'] = 0
        try:
            lianjiaItem['huxing'] = huxing
        except:
            lianjiaItem['huxing'] = 0
        try:
            lianjiaItem['floor'] = floor
        except:
            lianjiaItem['floor'] = 0
        try:
            lianjiaItem['area'] = area
        except:
            lianjiaItem['area'] = 0
        try:
            lianjiaItem['huxing_struct'] = huxing_struct
        except:
            lianjiaItem['huxing_struct'] = 0
        try:
            lianjiaItem['inarea'] = inarea
        except:
            lianjiaItem['inarea'] = 0
        try:
            lianjiaItem['build_type'] = build_type
        except:
            lianjiaItem['build_type'] = 0
        try:
            lianjiaItem['direction'] = direction
        except:
            lianjiaItem['direction'] = 0
        try:
            lianjiaItem['build_struct'] = build_struct
        except:
            lianjiaItem['build_struct'] = 0
        try:
            lianjiaItem['decoration'] = decoration
        except:
            lianjiaItem['decoration'] = 0
        try:
            lianjiaItem['tihu'] = tihu
        except:
            lianjiaItem['tihu'] = 0
        try:
            lianjiaItem['warm_type'] = warm_type
        except:
            lianjiaItem['warm_type'] = 0
        try:
            lianjiaItem['elevator'] = elevator
        except:
            lianjiaItem['elevator'] = 0
        try:
            lianjiaItem['property_years'] = property_years
        except:
            lianjiaItem['property_years'] = 0

        # 下面所属于一类结构

        return lianjiaItem
