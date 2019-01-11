#
# # -*- coding: utf-8 -*-
# # -*- coding: UTF-8 -*-
#
#
# import requests
# def fun():
#
#
    # headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
#
#     proxies = {
#         'https':'211.101.149.38:53281',
#         'https':'61.135.217.7:80',
#         'https':'42.55.253.135:1133'
#     }
#     url = 'https://shanghai.anjuke.com/v3/ajax/broker/phone/?broker_id=3709965&token=dcc834f2121dbf532f5168266acc0d76&prop_id=1352418197&prop_city_id=11&house_type=1&captcha='
#     r = requests.get(url,headers=headers,proxies = proxies)
#
#     data = r.text
#
#     print(data)
#
# fun()



# import requests
#
# headers = {
#     "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
#
# # 将代理的服务器放入这里，key为协议类型 value为代理的ip和端口
# # 发送https或者http请求会根据不同代理ip选择 为我们发送请求
proxies = {
    # 'http':'http://211.101.149.38:53281',
    # 'https':'https://42.55.253.135:1133',
    'https':'https://111.155.116.227:8123',
    'http':'http://183.167.217.152:63000'

}
#
# # 1 要爬取的页面地址
# url = 'https://shanghai.anjuke.com/v3/ajax/broker/phone/?broker_id=3709965&token=dcc834f2121dbf532f5168266acc0d76&prop_id=1352418197&prop_city_id=11&house_type=1&captcha='
# # 2 发送get请求 拿到响应
# response = requests.get(url=url,proxies=proxies,headers=headers)
# # 3 获取响应内容文本  两种方法
# html = response.content.decode() #response.content为bytes类型，decode() 将它转换为utf8
# print(html)

import requests

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    "referer": "https: // shanghai.anjuke.com / prop / view / A1365207046?from=filter & spread = commsearch_p & position = 3 & kwtype = filter & now_time = 1534236523"}
# 如果代理需要使用HTTP Basic Auth，可以使用下面这种格式：
proxy = {"https": "H3G17717921RP0VD:691B6CA2B56FA1E6@http://http-dyn.abuyun.com:9020"}
url = 'https://shanghai.anjuke.com/v3/ajax/broker/phone/?broker_id=3709965&token=dcc834f2121dbf532f5168266acc0d76&prop_id=1352418197&prop_city_id=11&house_type=1&captcha='
session =requests.session()
session.get('https://shanghai.anjuke.com/',proxies = proxies,headers = headers)

response = session.get(url, proxies = proxies,headers=headers)

print(response.content.decode())