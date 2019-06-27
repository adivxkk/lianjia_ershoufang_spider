import json
import re

from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider

from lianjiaSpider.utils.insertRedis import inserintotc, inserintota

'''
58同城的爬虫
'''


# 继承自RedisSpider，则start_urls可以从redis读取
# 继承自BaseSpider，则start_urls需要写出来
class LianjiaSpider(RedisSpider):
    name = 'lianjia_master'
    # 因为https://zz.lianjia.com/ershoufang/guanchenghuizuqu/就是该地区第一页，所以直接加上pg1，对应下面正则表达式提取head_url
    # start_urls=(
    #
    #     'https://zz.lianjia.com/ershoufang/guanchenghuizuqu/pg1',
    #     'https://zz.lianjia.com/ershoufang/zhongyuan/pg1',
    #     'https://zz.lianjia.com/ershoufang/jinshui/pg1',
    # )
    # redis_key = 'kk_esfang:start_urls'
    # 解析从start_urls下载返回的页面
    # 页面页面有两个目的：
    # 第一个：解析获取下一页的地址，将下一页的地址传递给爬虫调度器，以便作为爬虫的下一次请求
    # 第二个：获取详情页地址，再对详情页进行下一步的解析
    # redis_key = 'start_urls'
    redis_key = 'kk_esfang:start_urls'

    def parse(self, response):
        # 获取所访问的地址,获得第一个分组
        head_url = re.findall(r'^https://.*?/pg', response.url)[0]
        response_selector = Selector(response)
        # 下一页链接，有一个大坑，页面加载之后，没有“下一页”这个字符串了，所有都是单纯的a标签，
        # next_link = response_selector.xpath('//div[contains(@class,"page-box house-lst-page-box")]/a[text()="下一页"]/@href').extract()[0]
        # 所以需要使用totalPage和curpage构造下一页链接，json加载从str变成dict
        totalpage_curpage = response_selector.xpath('//div[contains(@class,"page-box fr")]/div/@page-data').extract()[0]
        page_dict = json.loads(totalpage_curpage)
        totalpage = page_dict['totalPage']
        curpage = page_dict['curPage']
        if curpage < totalpage:
            next_link = head_url + str(curpage + 1)
            # print('the next_page link : ' + next_link)
            inserintotc(next_link, 1)
            print('#########[success] the next link :-> ' + next_link + ' is insert into the redis queue#########')
        elif curpage == totalpage:
            print('已经爬完该地区的详情页url，共有{}页'.format(totalpage))
        # 详情页链接列表
        # 有些地区最后一页新上的房源会加上ul.class=sellListContent LOGCLICKDATA，多加了一个LOGCLICKDATA，所以要使用contains
        detail_links = response_selector.xpath(
            '//ul[contains(@class,"sellListContent")]/li[contains(@class,"clear LOGCLICKDATA")]/a[contains(@class,"noresultRecommend img")]/@href').extract()
        for detail_link in detail_links:
            # 对详情页进行解析detail_url
            if detail_link:
                inserintota(detail_link, 2)
                print('########[success] the detail link:-> ' + detail_link + ' is insert into the redis queue########')
