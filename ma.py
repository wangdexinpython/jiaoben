#!usr/bin/env python
# # -*- coding: utf-8 -*-
# import requests
# import json
# import re
# class Datapay(object):
#     def __init__(self):
#
#         content = {
#             'encrypt': 1,
#             'cdpDate': 'DY6dEs7g1huVNAQb/KsDdg==',
#             'token':'NWuPw+1kpuAOLk5ufIwB3A==',
#             'sign': 'qp3DG8OD/hhxO1jCe7K1DFkrCwuK9ZigN6j8Wk/affA=',
#             'page': 'gjGIigAEqLMxUHJsQsDIww==',
#             'pageSize': 'ORYL5P5EIJpP6rXsw8AG7Q=='
#         }
#         self.url = 'https://www.chinadatapay.com/viewJsp/newsList.jsp?v=3.1'
#         self.url1 = "https://www.chinadatapay.com/dynamics/archives"
#         self.headers = {
#             "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
#         html = requests.post(self.url1,headers = self.headers,data=content)
#         res = html.text
#         print(res)
#     def parse(self):
#         pass
#     def run(self):
#         pass
# if __name__ == '__main__':
#     pa = Datapay()
#     pa.run()
import requests
import flask
from flask import request

fname = request.files.get()

print(fname)
























