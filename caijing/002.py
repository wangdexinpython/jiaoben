# coding = utf-8
import time,requests
import json
url = 'https://www.mbcaijing.com/channel/Q1HeTCBsEW0%253d'
url2 = 'https://api.mbcaijing.com/api/web/Articles/GetArticles'

headers1 = {
    ':authority':'api.mbcaijing.com',
    ':method':'OPTIONS',
    ':path':'/api/web/Articles/GetArticles',
    ':scheme':'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'origin': 'https://www.mbcaijing.com',
    'access-control-request-headers':'content-type',
    'access-control-request-method': 'post',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}


session = requests.session()
session.get(url)

html = session.options(url2,data =headers1)


# resp = session.post(url2, data=json.dumps(params2), headers=headers2)
# resp = requests.post(url2, data=params2, headers=headers2)

print(html.status_code)

print(html.text)

