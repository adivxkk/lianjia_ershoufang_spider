# -*- coding: utf-8 -*-
import scrapy


class LianjiatestSpider(scrapy.Spider):
    name = 'lianjiatest'
    allowed_domains = [''zz.lianjia.com'']
    start_urls = ['http://'zz.lianjia.com'/']

    def parse(self, response):
        pass
