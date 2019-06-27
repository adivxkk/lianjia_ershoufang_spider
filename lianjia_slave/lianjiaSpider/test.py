from lianjiaSpider.utils.getproxy import getjson_proxy
import random

def main():
    ip_list = getjson_proxy()
    print(ip_list)
    ip = random.choice(ip_list)
    print(ip)


main()
