#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangdexin


# coding = utf-8
import time,requests
import json
url2 = 'http://www.cbfau.com/hwsj.html'
params2 = {
    "__EVENTTARGET":"lnkBtnNext",
    "__EVENTARGUMENT":"",
    "__VIEWSTATE":"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",
    "__EVENTVALIDATION":"fr65kxdSpX58lxXeKn539GO9+ANQKGHQ5x8auW9MV2+cl+ZC2LFxnKmZ5hDYHg8Jvp2Br9ZoesyM1pfIUUB4lNK2WJ4WgXmmAPYxOIh4nOxvFqOI+fGddnhtWhv/uyFg5d8Xs0PNHIdASHIRCoKsUR9lKuReopbHJjJOarmklXMOxieImoYm9Tbsl3Y/aV+WGC6m71Iv9YL1HL40bT6MpSuDHKCOcYKU2m90lA1KsiRFL3dNrn7XBZbYQXPhHsdb",
    "wucsearch$searchtd":""
}
headers2 = {
# POST /hwsj.html HTTP/1.1
'Host': 'www.cbfau.com',
'Connecition': 'keep-alive',
'Content-Length': '5795',
'Cache-Control': 'max-age=0',
'Origin': 'http://www.cbfau.com',
'Upgrade-Insecure-Requests': '1',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'http://www.cbfau.com/hwsj.html',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': 'Hm_lvt_3210d5a96eea563944a603c7b0ff64d5=1544084469; Hm_lpvt_3210d5a96eea563944a603c7b0ff64d5=1544090842'

    # "Host":"www.cbfau.com",
    # "Origin":"http://www.cbfau.com",
    # "Referer":"http://www.cbfau.com/hwsj.html",
    # "Upgrade-Insecure-Requests":"1",
    # "Cookie":"Hm_lvt_3210d5a96eea563944a603c7b0ff64d5=1544084469; Hm_lpvt_3210d5a96eea563944a603c7b0ff64d5=1544088729",
    # 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
resp = requests.post(url2, data=json.dumps(params2), headers=headers2)
print(resp.status_code)
print(resp.text)

