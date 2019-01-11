#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangdexin

import requests,re
import json


# cookie = "_ga=GA1.2.1890675989.1528085065; device_id=f67d6a789eb88d9fc5c92389708e61bf; _gid=GA1.2.1455210456.1533126179; s=ef11evot6s; __utmz=1.1533126255.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); aliyungf_tc=AQAAAADUSkaKLA4AMYdFec3KcErxReDS; xq_a_token=aef774c17d4993658170397fcd0faedde488bd20; xq_a_token.sig=F7BSXzJfXY0HFj9lqXif9IuyZhw; xq_r_token=d694856665e58d9a55450ab404f5a0144c4c978e; xq_r_token.sig=Ozg4Sbvgl2PbngzIgexouOmvqt0; u=691533272441309; __utma=1.1890675989.1528085065.1533207822.1533272455.3; __utmc=1; __utmb=1.1.10.1533272455; Hm_lvt_1db88642e346389874251b5a1eded6e3=1533207798,1533214278,1533272441,1533273762; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1533273762; _gat_gtag_UA_16079156_4=1"
#         #详情cookie
#         # cookie = "_ga=GA1.2.1890675989.1528085065; device_id=f67d6a789eb88d9fc5c92389708e61bf; _gid=GA1.2.1455210456.1533126179; s=ef11evot6s; __utmz=1.1533126255.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); aliyungf_tc=AQAAAADUSkaKLA4AMYdFec3KcErxReDS; xq_a_token=aef774c17d4993658170397fcd0faedde488bd20; xq_a_token.sig=F7BSXzJfXY0HFj9lqXif9IuyZhw; xq_r_token=d694856665e58d9a55450ab404f5a0144c4c978e; xq_r_token.sig=Ozg4Sbvgl2PbngzIgexouOmvqt0; Hm_lvt_1db88642e346389874251b5a1eded6e3=1533126179,1533207798,1533214278,1533272441; _gat_gtag_UA_16079156_4=1; u=691533272441309; __utma=1.1890675989.1528085065.1533207822.1533272455.3; __utmc=1; __utmt=1; __utmb=1.1.10.1533272455; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1533272458"
#         self.cookies = {i.split("=")[0]: i.split("=")[-1] for i in cookie.split("; ")}
#         self.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}




def parse():
    url = 'http://www.metalnews.cn/ys/show-1288595-1.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        "Referer":"http://www.metalnews.cn/ys/list-75-1.html",
        "Upgrade-Insecure-Requests": "1",
        "Host":"www.metalnews.cn",
        "Connection":"keep-alive",
        "Cache-Control":"max-age=0",
        "Accept-Language":"zh-CN,zh;q = 0.9",
        "Accept-Encoding":"gzip,deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Cookie":"Hm_lvt_0f815ab47090e27bab5905a8c9fe18fb=1543567340; PHPSESSID=ntoqcj7gluu8kjkccqih1od2q4; c3j_forward_url=http%3A%2F%2Fwww.metalnews.cn%2Fys%2Fshow-1293129-1.html; c3j_auth=VWZZbFY8UTFQZQ1mBgtSJAtoBW9WZAVmBzcGeANpBWsDNlNdUTUCXVdqXjFWNAA4VDIAMgJkVWJSNlJnB2FSZlVkWWpWNVExUDMNYgYzUjILbwU4VmcFMgc3BjIDYQU3AzBTY1FlAmVXW14y; c3j_username=wangdexin1; Hm_lpvt_0f815ab47090e27bab5905a8c9fe18fb=1543570146"
    }
    cookie = 'Hm_lvt_0f815ab47090e27bab5905a8c9fe18fb=1543567340; PHPSESSID=ntoqcj7gluu8kjkccqih1od2q4; c3j_forward_url=http%3A%2F%2Fwww.metalnews.cn%2Fys%2Fshow-1293129-1.html; c3j_auth=VWZZbFY8UTFQZQ1mBgtSJAtoBW9WZAVmBzcGeANpBWsDNlNdUTUCXVdqXjFWNAA4VDIAMgJkVWJSNlJnB2FSZlVkWWpWNVExUDMNYgYzUjILbwU4VmcFMgc3BjIDYQU3AzBTY1FlAmVXW14y; c3j_username=wangdexin1; Hm_lpvt_0f815ab47090e27bab5905a8c9fe18fb=1543570146'
    cookies = {i.split("=")[0]: i.split("=")[-1] for i in cookie.split("; ")}
    print(type(cookies))
    html = requests.get(url,headers = headers,cookies = cookies)
    # print(html.text)

parse()



