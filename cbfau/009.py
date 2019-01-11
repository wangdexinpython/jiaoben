#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangdexin
# ee1f0fUH8bVqrAYY6B%2F1HhWvNgnKsA9w7OU0ZCxh9NYuLeS4mjTN
# print(con)
# print(resp)
import requests,re
from lxml import etree
class Ailab(object):
    def __init__(self):
        self.url = 'http://cloud.ailab.cn/?page={}'
        self.li = []

    def header_s(self,cook):

        cookie = "nRhl_ba1e_saltkey=BO55QH99; nRhl_ba1e_lastvisit=1545296577; UM_distinctid=167cb7c6e6eb86-080f21b1784a4-18261202-100200-167cb7c6e6f319; CNZZDATA3202821=cnzz_eid%3D982886494-1545299754-http%253A%252F%252Fcloud.ailab.cn%252F%26ntime%3D1545299754; nRhl_ba1e_lastrequest={}; nRhl_ba1e_lastact=1545300515%09index.php%09".format(cook)
        headers = {
        "Host":"cloud.ailab.cn",
        "Connection":"keep-alive",
        "Upgrade-Insecure-Requests":"1",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding":"gzip,deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'Cookie':cookie,
            # 'Cookie':'nRhl_ba1e_saltkey=BO55QH99; nRhl_ba1e_lastvisit=1545296577; UM_distinctid=167cb7c6e6eb86-080f21b1784a4-18261202-100200-167cb7c6e6f319; CNZZDATA3202821=cnzz_eid%3D982886494-1545299754-http%253A%252F%252Fcloud.ailab.cn%252F%26ntime%3D1545299754; nRhl_ba1e_lastrequest=f6d0W9XCTZirk4YYSG2YaSW4UblHy3C7WyVIHH8gQOKrvqlPGoH%2F; nRhl_ba1e_lastact=1545300515%09index.php%09'
        }
        return headers
    def parse(self,url,headers):
        resp = requests.get(url, headers=headers)
        con = resp.text
        # print(con)
        selector = etree.HTML(con)
        cons = selector.xpath("//ul[@class='list_jc']/li/a[1]/@href")
        if len(cons)==0:
            print("数据为空，失败")
        else:
            print("抓取成功")
            set_s = resp.headers
            lastrequest = re.findall('nRhl_ba1e_lastrequest=(.*?);', set_s.get('Set-Cookie'))[0]
            return [1,lastrequest]
        self.li.append(cons)
        set_s = resp.headers
        lastrequest = re.findall('nRhl_ba1e_lastrequest=(.*?);',set_s.get('Set-Cookie'))[0]

        # print(set_cookie)
        return [lastrequest]
    def url_(self):
        for i in range(1,9):
            url = self.url.format(i)
            return url

    def run(self):
        parm = 'ed5exV5M%2BTa8qGLkSdGBEI7MWyxhM%2FPDlPKvcYkc%2FGd8b1DTzeOR'
        print("参数测试阶段")
        for i in range(1,50):
            print(i)
            url = self.url.format(i)
            headers = self.header_s(parm)
            data = self.parse(url,headers)
            if len(data)==1:
                parm = data[0]
            else:
                self.li = []
                parm = data[1]
                print("===============================")
                print("正式请求阶段")
                for j in range(1, 10):
                    print(j)
                    url = self.url.format(j)
                    headers = self.header_s(parm)
                    data = self.parse(url, headers)
                    parm = data[1]
                return
        # print(self.li)

if __name__ == '__main__':
    ailab = Ailab()
    ailab.run()