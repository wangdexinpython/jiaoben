#!usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import re
import csv
from lxml import etree

"""
author:wangdexin
time:2018,8.2
"""

class Xueqiu(object):
    def __init__(self):
        self.url = "https://xueqiu.com/v4/statuses/user_timeline.json?page=1&user_id=8801386347"
        # self.url = 'https://xueqiu.com/'
        #首页cookie
        cookie = "_ga=GA1.2.1890675989.1528085065; device_id=f67d6a789eb88d9fc5c92389708e61bf; _gid=GA1.2.1455210456.1533126179; s=ef11evot6s; __utmz=1.1533126255.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); aliyungf_tc=AQAAAADUSkaKLA4AMYdFec3KcErxReDS; xq_a_token=aef774c17d4993658170397fcd0faedde488bd20; xq_a_token.sig=F7BSXzJfXY0HFj9lqXif9IuyZhw; xq_r_token=d694856665e58d9a55450ab404f5a0144c4c978e; xq_r_token.sig=Ozg4Sbvgl2PbngzIgexouOmvqt0; u=691533272441309; __utma=1.1890675989.1528085065.1533207822.1533272455.3; __utmc=1; __utmb=1.1.10.1533272455; Hm_lvt_1db88642e346389874251b5a1eded6e3=1533207798,1533214278,1533272441,1533273762; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1533273762; _gat_gtag_UA_16079156_4=1"
        #详情cookie
        # cookie = "_ga=GA1.2.1890675989.1528085065; device_id=f67d6a789eb88d9fc5c92389708e61bf; _gid=GA1.2.1455210456.1533126179; s=ef11evot6s; __utmz=1.1533126255.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); aliyungf_tc=AQAAAADUSkaKLA4AMYdFec3KcErxReDS; xq_a_token=aef774c17d4993658170397fcd0faedde488bd20; xq_a_token.sig=F7BSXzJfXY0HFj9lqXif9IuyZhw; xq_r_token=d694856665e58d9a55450ab404f5a0144c4c978e; xq_r_token.sig=Ozg4Sbvgl2PbngzIgexouOmvqt0; Hm_lvt_1db88642e346389874251b5a1eded6e3=1533126179,1533207798,1533214278,1533272441; _gat_gtag_UA_16079156_4=1; u=691533272441309; __utma=1.1890675989.1528085065.1533207822.1533272455.3; __utmc=1; __utmt=1; __utmb=1.1.10.1533272455; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1533272458"
        self.cookies = {i.split("=")[0]: i.split("=")[-1] for i in cookie.split("; ")}
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

    def parse(self):
        # res = requests.get(self.url,headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"})
        # res = requests.get(self.url)
        # ss = requests.session()
        # requests.utils.add_dict_to_cookiejar(ss.cookies,self.dic)
        res = requests.get(self.url,headers = self.headers,cookies = self.cookies)
        # ss = requests.session()
        # print(ss)
        html = res.content
        # html = etree.HTML(res.content)
        print(html)
    def run(self):
        self.parse()

if __name__ == '__main__':
    xueqiu = Xueqiu()
    xueqiu.run()


# cookies = {i.split("=")[0]:i.split("=")[-1] for i in cookies.split("; ")}
# print(cookies)
# # 请求个人主页
# r = requests.get("http://www.renren.com/327550029/profile", headers=headers,cookies=cookies)