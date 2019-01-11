#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangdexin
import requests,re

def parse():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }
    cookie="nRhl_ba1e_saltkey=BO55QH99; nRhl_ba1e_lastvisit=1545296577; UM_distinctid=167cb7c6e6eb86-080f21b1784a4-18261202-100200-167cb7c6e6f319; nRhl_ba1e_lastact=1545818632%09index.php%09; CNZZDATA3202821=cnzz_eid%3D982886494-1545299754-http%253A%252F%252Fcloud.ailab.cn%252F%26ntime%3D1545818633; nRhl_ba1e_lastrequest=4c25NqPnAN%2F7GeMoH2qUOWgGQ1XTWDE9K23UDxCu97FtO1%2FfKeiv"
    url = 'http://cloud.ailab.cn/'
    cookies = dict(cookies_are=cookie)
    # print(type(cookies))
    # print(cookies)
    html = requests.get(url,cookies=cookies,headers=headers)
    cont = html.text
    print(cont)
parse()






