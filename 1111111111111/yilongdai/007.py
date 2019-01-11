import urllib
import urllib2
import requests
import json
# https://licai.eloancn.com/sesame/
import re

class yilongdai():

    def __init__(self):
        self.url = "https://licai.eloancn.com/pcgway/gateway/v1/01"

    def parse_list(self):
        self.details_list = []
        self.lilv_list = []
        for i in range(1,8):
            print (i)
            value = {}
            value['requesturl'] = 'dtAouQWbsDjKac4I44if40Ujayw38KOk?v=123'
            value['pageNo'] = i
            value['platform'] = '5'
            data = urllib.urlencode(value)

            req = urllib2.Request(self.url, data)
            response = urllib2.urlopen(req)

            html = response.read()
            qi_list = re.findall(r'"prodDetail":"(.*?)",',html)
            nianhua = re.findall(r'"maxRate":"(.*?)",',html)
            self.details_list.append(qi_list)
            self.lilv_list.extend(nianhua)
        # print(self.details_list)
        # print(self.lilv_list)

    def parse_details(self):
        self.data_list = []
        # self.det_list = []
        for i in self.details_list:
            for j in i:
                pid = j
                self.det_list = []
                for n in range(1,5):
                    value = {}
                    value['requesturl'] = 'dtAouQWbsDjA1WICWhCBIEUjayw38KOk'
                    value['pageNo'] = n
                    value['prodDetail'] = pid
                    value['platform'] = '5'
                    data = urllib.urlencode(value)

                    req = urllib2.Request(self.url, data)
                    response = urllib2.urlopen(req)

                    html = response.read()
                    list = re.findall(r'"enTenderId":"(.*?)"}', html)
                    if len(list):
                        self.det_list.extend(list)

                # print(self.det_list)
                self.data_list.append(self.det_list)
        # print(self.data_list)
    def parse_data(self):
        self.data= []
        m=0
        for i in self.data_list:
            m+=1
            print(m)
            for j in i:
                data_2 = []
                value = {}
                value['requesturl'] = 'AqeXfFgEApnttSuMj1r7BaBklHUjMROZ'
                value['id'] = j
                value['mark'] = 2
                value['platform'] = '5'
                data = urllib.urlencode(value)
                req = urllib2.Request(self.url, data)
                response = urllib2.urlopen(req)
                html = response.read()
                # print(html)
                data_2.append(re.findall(r'"title":"(.*?)",',html)[0])
                data_2.append(re.findall(r'"realName":"(.*?)\*.*",', html)[0])
                print(re.findall(r'"realName":"(.*?)\*.*",', html)[0])
                data_2.append(re.findall(r'"cityName":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"gender":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"age":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"amount":"(.*?)"', html)[0])

                data_2.append(re.findall(r'"applyDate":"(.*?)",', html)[0])

                data_2.append(self.lilv_list[m-1])

                data_2.append(re.findall(r'"progress":"(.*?)"', html)[0])
                data_2.append(re.findall(r'"finalLevel":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"description":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"fullTenderDate":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"repaymenting":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"nsr":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"peopleGuarantee":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"hyzk":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"jycd":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"nativePlace":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"cqjzd":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"fc":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"gznx":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"industryName":(.*?),', html)[0])

                data_2.append(re.findall(r'"sbnx":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"sybx":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"liability":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"creditReportOverdue":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"overdueStatus":"(.*?)",', html)[0])
                # print(type(html))
                # self.data.append(html)
                # details_list = re.findall(r'', html)

                # if len(details_list):
                #     self.data_list.append(details_list)
                # # print(self.data_list)
                self.data.append(data_2)
    def data_re(self):
        f1 = open('data3.txt','a')

        for i in self.data:
            for j in i:
                f1.write(j)
                f1.write('\t')
            f1.write('\n')

        #     title = re.findall(r'"title":"(.*?)",',i)
        # print(self.data)

    def run(self):
        self.parse_list()
        self.parse_details()
        self.parse_data()
        self.data_re()

str = yilongdai()

str.run()