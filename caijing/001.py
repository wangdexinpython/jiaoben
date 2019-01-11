# coding = utf-8
import time,requests
import json
url2 = 'https://api.mbcaijing.com/api/web/Articles/GetArticles'
params2 = {
    "data": {"ChannelId":"Q1HeTCBsEW0%3d","Current": 9, "Psize": 9}
}
headers2 = {
'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'content-type': 'application/json',
'origin': 'https://www.mbcaijing.com',
'referer': 'https://www.mbcaijing.com/channel/Q1HeTCBsEW0%253d',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
resp = requests.post(url2, data=json.dumps(params2), headers=headers2)
print(resp.status_code)
print(resp.text)

