import urllib
import urllib2

import re



class yinongjihua():


    def __init__(self):
        self.url = "https://licai.eloancn.com/pcgway/gateway/v1/01"
        # self.get_url = 'https://licai.eloancn.com/pcgway/gateway/v1/01?requesturl=IjE9HTj42YWoZVeH5M3LwlnldpmC7Qbc&pageNo={}&pid='


    def parse_list(self):
        self.details_list = []
        self.lilv_list = []
        for i in range(1, 7):
            print(i)
            value = {}
            value['requesturl'] = '/appwmps/app002/v2/03'
            value['pageNo'] = i
            value['platform'] = '5'
            data = urllib.urlencode(value)

            req = urllib2.Request(self.url, data)
            response = urllib2.urlopen(req)
            html = response.read()
            print(html)
            qi_list = re.findall(r'"id":"(.*?)"', html)
            nianhua = re.findall(r'"strInterestrate":"(.*?)",', html)
            self.details_list.append(qi_list)
            self.lilv_list.extend(nianhua)
        print(self.details_list)


        print(self.lilv_list)


    def parse_det(self):
        get_url = 'https://licai.eloancn.com/pcgway/gateway/v1/01?requesturl=IjE9HTj42YWoZVeH5M3LwlnldpmC7Qbc&pageNo={}&pid='
        self.id_list = []
        for i in self.details_list:
            for j in i:
                self.id_list1 = []
                for p in range(1, 3):

                    url = get_url
                    url_1 = url.format(p)
                    # print(url)
                    url = url_1 + j
                    print(url)
                    request = urllib2.Request(url)
                    response = urllib2.urlopen(request)
                    html = response.read()
                    # print(html)
                    id = re.findall(r'"id":"(.*?)"',html)
                    # print(id)

                    if len(id):
                        self.id_list1.extend(id)


                    # print(self.id_list)
                # print(self.id_list1)
                self.id_list.append(self.id_list1)

    def parse_data(self):
        self.data = []
        m = 0
        for i in self.id_list:
            m += 1
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
                data_2.append(re.findall(r'"title":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"realName":"(.*?)\*.*",', html)[0])
                print(re.findall(r'"realName":"(.*?)\*.*",', html)[0])
                data_2.append(re.findall(r'"cityName":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"gender":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"age":"(.*?)",', html)[0])
                data_2.append(re.findall(r'"amount":"(.*?)"', html)[0])

                data_2.append(re.findall(r'"applyDate":"(.*?)",', html)[0])

                data_2.append(self.lilv_list[m - 1])

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
        # print(self.data)
    def data_re(self):
        f1 = open('data2.txt','a')

        for i in self.data:
            for j in i:
                f1.write(j)
                f1.write('\t')
            f1.write('\n')
    def run(self):
        self.parse_list()
        self.parse_det()
        self.parse_data()
        self.data_re()



beg = yinongjihua()
beg.run()