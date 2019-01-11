#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangdexin
import requests,re
import json
from lxml import etree

class Next(object):

    def __init__(self):
        self.url = 'http://www.cbfau.com/hwsj.html'


    def parse(self):
        html = requests.get(url=self.url).text
        selector = etree.HTML(html)
        VIEWSTATE = selector.xpath("//input[@name='__VIEWSTATE']/@value")
        EVENTVALIDATION = selector.xpath("//input[@name='__EVENTVALIDATION']/@value")
        params2 = {
            "__EVENTTARGET": "lnkBtnNext",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE":VIEWSTATE,
            "__EVENTVALIDATION":EVENTVALIDATION,
            "wucsearch$searchtd": ""
        }
        headers2 = {
            'Host': 'www.cbfau.com',
            'Connecition': 'keep-alive',
            'Content-Length': '5795',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://www.cbfau.com',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://www.cbfau.com/hwsj.html',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'Hm_lvt_3210d5a96eea563944a603c7b0ff64d5=1544084469; Hm_lpvt_3210d5a96eea563944a603c7b0ff64d5=1544090842'
}
    def parse_post(self):
        html = requests.post(url=self.url).text
        print(html)


    def run(self):
        self.parse()
        self.parse_post()


if __name__ == '__main__':
    next = Next()
    next.run()




















