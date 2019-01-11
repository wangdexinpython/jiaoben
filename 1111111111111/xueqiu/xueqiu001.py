#!usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import re
import pymysql

import csv
from lxml import etree

"""
author:wangdexin
time:2018,8.2
"""

class Xueqiu(object):
    def __init__(self):
        self.url = 'https://xueqiu.com/'
        self.url1 = "https://xueqiu.com/v4/statuses/user_timeline.json?page={}&user_id=8801386347"
        # self.url2 = "https://xueqiu.com/statuses/comments.json?id=111555885&count=20&page=1&reply=true&asc=false&type=status&split=true"
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

        self.session = requests.session()

        self.session.get(self.url, headers=self.headers)
    def parse(self):
        list = []
        # xiang = session.get(self.url1, headers=self.headers).text
        # print(xiang)
        for i in range(1, 2):
            url = self.url1.format(i)
            res = self.session.get(url,headers = self.headers).text
            html = json.loads(res)
            statuses = html.get('statuses')
            for j in range(0, 20):
                url = statuses[j].get('id')
                list.append(url)
        # print(list)
        return list
    def details(self):
        list = self.parse()
        print(list)
        list_dec = []

        url = "https://xueqiu.com/statuses/comments.json?id={}&count=20&page={}&reply=true&asc=false&type=status&split=true"
        for i in range(0,len(list)):
            for j in range(1,100):
                ur = url.format(list[i],j)
                print(ur)
                res = self.session.get(ur,headers = self.headers)
                results = res.text
                html = json.loads(results)

                # print(len(comments))
                maxpage = html.get("maxPage")
                if j > maxpage:
                    break
                else:
                    comments = html.get("comments")
                    if len(comments) is not 0:
                        for k in range(0,len(comments)):
                            temp = {}
                            temp['dec'] = comments[k].get('text')
                            # temp['dec'] = re.findall(r'(.*).*<.*>|.*',comments[k].get('text'))
                            temp['com_id'] = comments[k].get('id')
                            temp['user_id'] = comments[k].get('user_id')
                            list_dec.append(temp)
        # print(temp)
        print(len(list_dec))
        print(list_dec)

    def ex_mysql(self):
        pass
        # url = statuses.get(0)
        # print(url)
        # print(statuses)

    def run(self):
        self.parse()
        self.data_()
        self.details()
if __name__ == '__main__':
    xueqiu = Xueqiu()
    xueqiu.run()
