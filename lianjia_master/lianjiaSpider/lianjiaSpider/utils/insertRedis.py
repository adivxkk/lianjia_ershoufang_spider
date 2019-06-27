import redis
from scrapy.conf import settings


def inserintotc(str, type):
    try:
        # r = redis.Redis(host='127.0.0.1', port=6379, db=0)
        r = redis.Redis(host=settings['REDIS_HOST'], port=settings['REDIS_PORT'], db=settings['REDIS_DB'])
    except:
        print('连接redis失败')
    else:
        if type == 1:
            r.lpush('kk_esfang:start_urls', str)


def inserintota(str, type):
    try:
        # r = redis.Redis(host='127.0.0.1', port=6379, db=0)
        r = redis.Redis(host=settings['REDIS_HOST'], port=settings['REDIS_PORT'], db=settings['REDIS_DB'])

    except:
        print('连接redis失败')
    else:
        if type == 2:
            r.lpush('kk_esfang:requests', str)
