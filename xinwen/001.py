import re
import os
import requests

class Datapay(object):
    def __init__(self):
        content = {
            'pageNum': 1,
            'pageSize': 20,
            'jsonStr':{"typeid":"220"}

        }


        self.url1 = "http://news.cqcoal.com/manage/newsaction.do?method:webListPageNewsArchivesByTypeid"
        self.headers = {
            "Congtent-Type":"application/x-www-form-urlencoded; charset=UTF-8",
"Host":"news.cqcoal.com",
            "Origin":"http://news.cqcoal.com",
            "Cookie":"JSESSIONID=bSDGBKl8tW1DbvqujBid+ZiH.undefined; __51cke__=; __tins__19092507=%7B%22sid%22%3A%201542115269095%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201542117140573%7D; __51laig__=2",
            "Referer":"http://news.cqcoal.com/blank/nl.jsp?tid=220",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"




        }
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

