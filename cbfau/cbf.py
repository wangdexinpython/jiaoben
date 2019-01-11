#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangdexin
import requests, re
from lxml import etree
class Cbfau(object):
    def __init__(self):
        self.url = 'http://www.cbfau.com/hwsj.html'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        }
    def data(self, viewstate, eventvalidation):
        params = {
            "__EVENTTARGET": "lnkBtnNext",
            "__VIEWSTATE": viewstate,
            "__EVENTVALIDATION": eventvalidation
        }
        return params
    def param(self, html):
        selector = etree.HTML(html.text)
        content = selector.xpath("//div[@class='box1']/div[@class='wz1']/div/a[1]/@href")
        viewstate = selector.xpath("//input[@id='__VIEWSTATE']/@value")
        eventvalidation = selector.xpath("//input[@id='__EVENTVALIDATION']/@value")
        return [content, viewstate[0], eventvalidation[0]]

    def parse(self, url):
        html1 = requests.get(url=self.url)
        return html1

    def parse_post(self, params):
        html = requests.post(url=self.url, headers=self.headers, data=params)
        return html

    def run(self):
        li = []
        html = self.parse(self.url)
        list1 = self.param(html)
        li.append(list1[0])
        data = self.data(list1[1], list1[2])
        # 循环页数自定义
        for i in range(0,9):
            html_post = self.parse_post(data)
            list2 = self.param(html_post)
            li.append(list2[0])
            data = self.data(list2[1],list2[2])
        print(li)


if __name__ == '__main__':
    cbfau = Cbfau()
    cbfau.run()
