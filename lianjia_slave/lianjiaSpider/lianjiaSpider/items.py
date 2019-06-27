# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    targeturl = scrapy.Field()
    unit_price = scrapy.Field()
    total_price = scrapy.Field()
    # 下面属于同一结构，共13个
    huxing = scrapy.Field()
    floor = scrapy.Field()
    area = scrapy.Field()
    huxing_struct = scrapy.Field()
    inarea = scrapy.Field()
    build_type = scrapy.Field()
    direction = scrapy.Field()
    build_struct = scrapy.Field()
    decoration = scrapy.Field()
    tihu = scrapy.Field()
    warm_type = scrapy.Field()
    elevator = scrapy.Field()
    property_years = scrapy.Field()

    #     地区
    #
    region = scrapy.Field()
    #     小区名称
    community = scrapy.Field()
