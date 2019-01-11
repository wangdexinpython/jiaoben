# # coding=utf-8
#
# """
# @author:wangdexin
# @time:2018/8/2
# @desc:
# """
#
# # import random
# import requests
# # import redis
# import csv
# # redis_config = {
# #     "host":"127.0.0.1",
# #     "port":6379,
# #     "db" : 0
# # }
# # redis_conn = redis.Redis(host='localhost',port=6379,db=4,decode_responses=True)
#
# from lxml import etree
# class User_Agent(object):
#     def __init__(self):
#         self.url = 'https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/{}'
#     def user_agent(self):
#         self.tr_list = []
#         for i in range(1,2):
#             res = requests.get(self.url.format(i),headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
#             html = res.content
#             Html = etree.HTML(html)
#             list = Html.xpath('//div[@class="corset"]/table/tbody/tr')
#             self.tr_list.extend(list)
#             # print(tr_list)
#     def parse(self):
#         length = len(self.tr_list)
#         self.temp = []
#         dic_1 = {}
#         for i in range(1,length):
#             dic_1['user_age'] = self.tr_list[i].xpath('./td[@class="useragent"]/a/text()')[0]
#             dic_1['version'] = self.tr_list[i].xpath('./td[2]/text()')[0]
#             dic_1['os1'] = self.tr_list[i].xpath('./td[3]/text()')[0]
#             dic_1['type_hardware'] = self.tr_list[i].xpath('./td[4]/text()')[0]
#             self.temp.append(dic_1)
#         # print(len(temp))
#     def data_(self):
#         with open("file.csv","w") as f:
#             writer = csv.writer(f)
#             writer.writerow(["useragent","version","type"])
#             writer.writerow([1,2,3],[4,4,4])
#     def run(self):
#         self.user_agent()
#         self.parse()
#         self.data_()
# if __name__ == '__main__':
#     USA = User_Agent()
#     USA.run()



import csv
with open("file.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(["useragent","version","type"])
    writer.writerow([1,2,3])