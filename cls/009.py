#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangdexin
import requests,re
#https://www.cls.cn/v3/article/detail?id=305534&app=CailianpressWeb&os=web&sv=6.8.0&sign=44021c9e199dfd91b83dd66f5871e0c5
#
#
#
#


class Clss(object):
    def __init__(self):
        self.url = 'https://www.cls.cn/v3/article/detail?id=305534&app=CailianpressWeb&os=web&sv=6.8.0&sign=44021c9e199dfd91b83dd66f5871e0c5'
    def parse(self):
        con = requests.get(self.url)
        res = con.text
        print(res)

    def run(self):
        self.parse()


if __name__ == '__main__':
    clss = Clss()
    clss.run()














