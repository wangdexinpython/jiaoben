import re
import os
import requests
pipeline = os.popen('node page.js')
pipeline = os.popen('node nodejs.js')
res = pipeline.read()
# print(type(res))
encrypt = re.findall("encrypt:\s'(\d)',",res)
cdpDate = re.findall("cdpDate:\s'(.*)',",res)
token = re.findall("token:\s'(.*)',",res)
sign = re.findall("sign:\s'(.*)',",res)
page = re.findall("page:\s'(.*)',",res)
pageSize = re.findall("pageSize:\s'(.*)'",res)
class Datapay(object):
    def __init__(self):
        content = {
            'encrypt': int(encrypt[0]),
            'cdpDate': cdpDate[0],
            'token':token[0],
            'sign': sign[0],
            'page': page[0],
            'pageSize': pageSize[0]
        }
        self.url = 'https://www.chinadatapay.com/viewJsp/newsList.jsp?v=3.1'
        self.url1 = "https://www.chinadatapay.com/dynamics/archives"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
        html = requests.post(self.url1,headers = self.headers,data=content)
        res = html.text
        print(res)
    def parse(self):
        pass
    def run(self):
        pass
if __name__ == '__main__':
    pa = Datapay()
    pa.run()

