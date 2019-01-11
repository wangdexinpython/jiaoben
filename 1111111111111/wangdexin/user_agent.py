# coding=utf-8

"""
@author:wangdexin
@time:2018/8/2
@desc:
"""

# import random
import requests
import redis
# redis_config = {
#     "host":"127.0.0.1",
#     "port":6379,
#     "db" : 0
# }
redis_conn = redis.Redis(host='localhost',port=6379,db=4,decode_responses=True)

from lxml import etree
class User_Agent(object):
    def __init__(self):
        self.url = 'https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/{}'
    def user_agent(self):
        self.tr_list = []
        for i in range(1,2):
            res = requests.get(self.url.format(i),headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
            html = res.content
            Html = etree.HTML(html)
            list = Html.xpath('//div[@class="corset"]/table/tbody/tr')
            self.tr_list.extend(list)
            # print(tr_list)
    def parse(self):
        length = len(self.tr_list)
        self.temp = []
        dic_1 = {}
        for i in range(1,length):
            dic_1['user_age'] = self.tr_list[i].xpath('./td[@class="useragent"]/a/text()')[0]
            dic_1['version'] = self.tr_list[i].xpath('./td[2]/text()')[0]
            dic_1['os1'] = self.tr_list[i].xpath('./td[3]/text()')[0]
            dic_1['type_hardware'] = self.tr_list[i].xpath('./td[4]/text()')[0]
            self.temp.append(dic_1)
        # print(len(temp))
    def data_(self):
        # print(self.temp)
        # field = 'user_age'
        value = self.temp
        #hash类型
        # redis_conn.set('useragent',field,value)
        #string类型
        redis_conn.append('useragent',value)
        #list类型
        # redis_conn.lpush('useragent',value)
    def run(self):
        self.user_agent()
        self.parse()
        self.data_()
if __name__ == '__main__':
    USA = User_Agent()
    USA.run()




# def user_agent():
#     a = random.randint(1, 10)
#     url = 'https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/{}'.format(str(a))
#     res = requests.get(url, headers={
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
#     print (res)
#
#     tree = etree.HTML(res.content)
#     tr_list = tree.xpath('//div[@class="corset"]//tr')
#     user_agent_list = []
#     for tr in tr_list:
#         user_agent = tr.xpath('./td[@class="useragent"]/a/text()')
#         version = tr.xpath('./td[2]/text()')
#         system_os = tr.xpath('./td[3]/text()')
#         common = tr.xpath('./td[5]/text()')
#         if user_agent:
#             user_agent_list.append((user_agent[0], version, system_os, common))
#     print (user_agent_list)
#     return random.choice(user_agent_list)
#
#
# if __name__ == '__main__':
#     uas = user_agent()
#     print (uas)
