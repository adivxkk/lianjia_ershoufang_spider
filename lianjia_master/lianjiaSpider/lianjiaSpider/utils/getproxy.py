import json

path_json = 'lianjiaSpider/utils/verified_proxies.json'


def getjson_proxy():
    li = []
    with open(path_json, 'r') as f:
        ips = f.readlines()
        for ip in ips:
            # 字符串变为字典
            proxy_json = json.loads(ip)
            # ip = ip.replace('\n', '')
            type = proxy_json['type']
            host = proxy_json['host']
            port = str(proxy_json['port'])
            ip_proxy = type + '://' + host + ':' + port
            li.append(ip_proxy)
    return li
