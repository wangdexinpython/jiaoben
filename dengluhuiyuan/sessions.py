#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangdexin

import requests,re




# http://www.metalnews.cn/member/dl1.php

def parse():
    url = 'http://www.metalnews.cn/member/dl1.php'
    url1 = 'http://www.metalnews.cn/ys/show-1288595-1.html'


    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        "Referer":"http://www.metalnews.cn/ys/list-75-1.html",
        "Upgrade-Insecure-Requests": "1",
        "Host":"www.metalnews.cn",
        "Connection":"keep-alive",
        "Cache-Control":"max-age=0",
        "Accept-Language":"zh-CN,zh;q = 0.9",
        "Accept-Encoding":"gzip,deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    }
    parm = {
        'cookietime':2592000,
        "forward":"http://www.metalnews.cn/ys/list-75-1.html",
        'option':'username',
        'password':'e5ae90cfd9d7ab9ebf27e87a897dbda4',
        'submit':'+%B5%C7+%C2%BC+',
        'username':'wangdexin1'

    }
    session = requests.session()
    session.post(url,headers = headers,data=parm)
    print(session.cookies)
    html = session.get(url1)
    print(html.text)


parse()