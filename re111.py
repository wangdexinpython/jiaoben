#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangdexin
import requests,re
from lxml import etree

# ss = '"【钢谷网动力煤快报】20日动力煤市场，上游”'

# cont = re.findall('【(.*?)】',ss).
# cont = re.search('【.*?】',ss).group()
# print(cont)
# //div[@class='texttit_m1']

def parse():

    # url = 'http://stock.jrj.com.cn/2018/12/26002126802260.shtml'
    url = 'http://stock.jrj.com.cn/2018/12/26025226802546.shtml'
    url2='https://baijiahao.baidu.com/s?id=1620900522377058975&wfr=spider&for=pc'
    html = requests.get(url)

    cont = html.text
    # cont_re = re.findall('document.*爱投顾',cont)
    # print(cont_re)
    # print(cont)
    selector = etree.HTML(cont)

    div = selector.xpath("//div[@class='article-content']")
    div = etree.tostring(div[0],encoding='utf8')
    # print(div)


    # content = etree.tostring(div[0  ], method='html')
    # content = etree.tostring(div[0],)
    # # print())
    # cont = type(str(content).encode('utf-8').decode('unicode_escape'))
    # # print(content.decode('unicode-escape'))
    # print content
parse()


