#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:dexin


import re
import requests,json,time,base64

class  Silver(object):

    def __init__(self):
        self.url1 = 'http://www.silver.org.cn/kuaixun/'
        self.url = 'http://www.silver.org.cn/live/more.html?id={}'
    def parse(self):
        html = requests.get(self.url1).text
        self.lastkxid = re.findall('kxLastId=(.*?);',html)[0]
        # print(self.lastkxid)
    def parse2(self):
        lastkxid = self.lastkxid
        print(lastkxid)
        url = self.url.format(lastkxid)
        print(url)
        res = requests.get(url).text

        lastkxid = re.findall('"lastkxid":"(\\d+)"',res)
        print(lastkxid)
        print(res)
    def run(self):
        self.parse()
        self.parse2()




if __name__ == '__main__':
    sivler = Silver()
    sivler.run()
