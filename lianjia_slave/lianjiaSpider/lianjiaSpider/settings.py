# -*- coding: utf-8 -*-

# Scrapy settings for lianjiaSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lianjiaSpider'

SPIDER_MODULES = ['lianjiaSpider.spiders']
NEWSPIDER_MODULE = 'lianjiaSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'lianjiaSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 下载等待时间10s
# DOWNLOAD_TIMEOUT = 2
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16
# 这个是设置请求并发数的，先不用它的
# CONCURRENT_REQUESTS=8
# CONCURRENT_REQUESTS= 10
# 避免爬虫被禁的策略1，禁用cookie
# Disable cookies (enabled by default)
# COOKIES_ENABLED = False
COOKIES_ENABLED = False
# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False
# 设置下载延时，防止爬虫被禁
DOWNLOAD_DELAY = 2
# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'lianjiaSpider.middlewares.LianjiaspiderSpiderMiddleware': 543,
# }

SPIDER_MIDDLEWARES = {
    # 'lianjiaSpider.middlewares.MyUserAgentMiddleware': 400,
}
# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# 添加User—Agent用户代理
DOWNLOADER_MIDDLEWARES = {
    # 'lianjiaSpider.middlewares.LianjiaspiderDownloaderMiddleware': 543,
    'lianjiaSpider.middlewares.MyUserAgentMiddleware': 400,
    'lianjiaSpider.middlewares.MyHttpProxyMiddleware': 100,
    'lianjiaSpider.middlewares.Redirect_Middleware': 500,
    'lianjiaSpider.middlewares.Timeout_Middleware': 610,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': None,
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': None,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 设置数据入库pipline
ITEM_PIPELINES = {
    # 'lianjiaSpider.pipelines.LianjiaspiderPipeline': 300,
    'lianjiaSpider.mongodb_pipeline.SingleMongodbPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# mongod数据写入
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'esfang'
MONGODB_DOCNAME = 'esfang_detail'

# scrapy-redis设置，改造scrapy
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# redis数据库操作请求
REDIS_URL = None
# 寝室下master_ip
# REDIS_HOST = '192.168.1.102'
REDIS_HOST = '192.168.1.104'
# 手机下master_ip
# REDIS_HOST = '192.168.43.194'
REDIS_PORT = '6379'

