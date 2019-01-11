#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangdexin

# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# 取前八页的数据
# 首页自己加上吧
# import re,requests,time,json
# def parse():
#     url = 'http://column.jrj.com.cn/expertsFirst.js'
#     html = requests.get(url)
#     res = html.text
#     data = re.findall('info={(.*}])};',res)[0]
#     infourl= re.findall('"infoUrl":"(.*?)",',data)
#     inputdate = re.findall('"inputDate":"(.*?)",',data)
#     infourl = infourl[0:140]
#     # print(data)
#     print(infourl)
#     # print(inputdate)
# parse()




# 一个月之内

import re,requests,time,json
from datetime import datetime
def parse():
    d_now = datetime.now()
    url = 'http://column.jrj.com.cn/expertsFirst.js?_=1543467572469'
    # time = time.time()
    html = requests.get(url)
    res = html.text
    data = re.findall('info={(.*}])};',res)[0]
    infourl= re.findall('"infoUrl":"(.*?)",',data)
    inputdate = re.findall('"inputDate":"(.*?)",',data)
    j = 0
    infourl1 = []
    for i in inputdate:
        d1 = datetime.strptime(i, '%Y-%m-%d %H:%M:%S')
        day = (d_now - d1).days
        if day < 30:
            infourl1.append(infourl[j])
        j = j +1
    print(infourl1)
parse()