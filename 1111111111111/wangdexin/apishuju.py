# -* - coding: UTF-8 -* -
import urllib
import urllib2
import json
import string

import re

class api():
    def __init__(self):
        self.url="http://data.zhugefang.com/Borough/Api/getCityareaList?city=bj"
    def parse(self):
        request = urllib2.Request(self.url)
        # request.add_header('content-TYPE', 'application/x-www-form-urlencoded')
        response = urllib2.urlopen(request)
        response.getcode()
        response.geturl()
        html = response.read()
        res_dict = json.loads(html)
        print(res_dict)
        self.data_list = res_dict['data']

    def parse_data(self):
        data_li = []
        for data in self.data_list:
            temp = {}
            temp[data['name']] = data['id']
            data_li.extend(temp)
        print(data_li)
    # res_dict = json.loads(res)
    # # print(res_dict['data'])
    # data_list = res_dict['data']

    # print(data_list)

    # dict = {}
    # list1=[]
    # list2=[]
    # for data in data_list:
    #     temp={}
    #     temp[data['name']]=data['id']
    #     list1.append(temp)
    #
    #     temp2={}
    #     dict2 = data['list_cityarea2']
    #     for k in dict2.keys():
    #         temp2[k]=dict2[k]['id']
    #         list2.append(temp2)

    # def data_re(self):
    #     f1 = open('api.txt','a',encoding='utf-8')
    #     # data = self.qi_list
    #     for i in self.qi_li:
    #         # for j in i:
    #
    #         f1.write(i)
    #         f1.write('\n')
    def run(self):
        self.parse()
        self.parse_data()


Api = api()

Api.run()
# Api.data_re()