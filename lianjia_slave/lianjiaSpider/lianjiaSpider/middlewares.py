# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals


class LianjiaspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class LianjiaspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MyUserAgentMiddleware(object):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        print('this agent is ' + user_agent)
        request.headers['User-Agent'] = user_agent


USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    # 自己的
]
from lianjiaSpider.utils.getproxy import getjson_proxy


class MyHttpProxyMiddleware(object):
    def __init__(self):
        self.ip_list = getjson_proxy()

    def process_request(self, request, spider):
        ip = random.choice(self.ip_list)
        print('tihs ip is ' + ip)
        request.meta['proxy'] = ip


from scrapy.exceptions import IgnoreRequest


class Redirect_Middleware():
    '''这里重点讲解一下关于处理下载器刚下载下来的response。
	在spidermiddleware中，我禁掉了httperror中间件，其中的原因是，
	我禁止了scrapy自带下载中间件中重定向，重试以及metarefeash中间件。
	原因是这非常的影响爬虫的性能，只会增加爬虫的消耗，而不会带来任何好处。为什么这么说呢？
	每一次的重定向，都有可能增加dns解析，tcp/ip链接，然后才是发送http请求。
	我们为什么要浪费这么多的时间，没任何理由。所以我的做法是，接受任何响应，
	然后在下载中间件中处理这个响应，过滤出200状态码的相应交给engine.对于那么重定向的(301, 302,meta-refreash等)，
	我提取出响应头部中的’location’等，然后重新生成一个request对象，交给调度器重新调度。对于404响应，直接抛弃。
	对于500+响应，把初始request对象重新交给调度器。这样，既不会影响爬虫的正常抓取，也不会落下需要再次抓取的request对象。
	'''

    def process_response(self, request, response, spider):
        # 处理下载完成的response
        # 排除状态码不是304的所有以3为开头的响应

        http_code = response.status
        if http_code // 100 == 2:
            return response

        if http_code // 100 == 3 and http_code != 304:
            # 获取重定向的url
            # url = response.headers['location']
            # domain = urlparse.urlparse(url).netloc
            # 判断重定向的url的domain是否在allowed_domains中
            # if domain in spider.allowed_domains:
            #     return Request(url=url, meta=request.meta)
            # else:

            # 把request返回到下载器
            return request.replace(dont_filter=True)
        if http_code // 100 == 4:
            # 需要注意403不是响应错误，是无权访问
            raise IgnoreRequest(u'404')

        if http_code // 100 == 5:
            return request.replace(dont_filter=True)


from scrapy.downloadermiddlewares.downloadtimeout import DownloadTimeoutMiddleware


class Timeout_Middleware(DownloadTimeoutMiddleware):
    # def process_response(self, request, response, spider):
    #     http_code = response.status
    #     print "####timeout"
    #     print http_code
    #     print '######timeout'
    #     # return request
    def process_exception(self, request, exception, spider):
        # print "######the downloader return exception!"
        print(exception)
        return request.replace(dont_filter=True)
