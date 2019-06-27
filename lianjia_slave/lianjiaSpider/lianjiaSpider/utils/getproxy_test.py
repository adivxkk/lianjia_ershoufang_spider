path_txt = './proxy_list.txt'
path_json = './verified_proxies.json'

# def get_proxy():
#     li = []
#     with open(path_txt, 'r') as f:
#         ips = f.readlines()
#         for ip in ips:
#             ip = ip.replace('\n', '')
#             print(ip.replace('\n', ''))
#             li.append(ip)
#     print(li)
#     return li
import json


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

