import base64
# import requests,re
# def parse():
#     url = 'http://cloud.ailab.cn/article-88594.html'
#     con = requests.get(url)
#     cons = con.text
#     print(cons)
# parse()
s='我是字符串'
ss = base64.b64encode(s)
print(ss)
