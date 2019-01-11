# -*- coding: UTF-8 -*-
import urllib
import urllib2
import requests
# from selenium import webdriver
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# driver = webdriver.PhantomJS('1.js')

class yilongdai():

    def __init__(self):
        self.temp_url = 'https://licai.eloancn.com/sesame/'
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

    def parse(self):
        html = requests.get(self.temp_url)
        # print(html.status_code)
        response = requests.get("")
    def run(self):
        self.parse()







obj=yilongdai()
obj.run()

