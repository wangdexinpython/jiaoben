# -*- coding: utf-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
import requests,re
import time
from pyquery import PyQuery as pq

class Ai(object):
    def __init__(self):
        self.url = 'http://www.rgznworld.com/jiashi'  # 智能驾驶

    def pase_index(self):

        resp = requests.get(self.url).text
        pq_resp = pq(resp)
        # for each in pq_resp(' div.list_block  > div.list_right > h3 > a').items():
        #     self.pase_datail(each.attr.href)

        page2 = 'http://www.rgznworld.com/ajax/index/lists?callback=jQuery191034534395701151865_1542781471027&categoryid=10&lasttime=%s'
        for t in pq_resp('div.list_block ').items():
            pub_time = t('p.biaozhu_time').text()
        pub_time = str(int(time.mktime(time.strptime(pub_time, '%Y-%m-%d %H:%M'))))
        page2url = page2 % str(pub_time)

        resp_page = requests.get(page2url).text
        print resp_page
        a_list = re.findall(r'html\\\/(\d+)\\\/(\d+)\\\/a0(\d+)\.html"',resp_page)
        self.parse_pages(a_list)

    def list_page(self,pub_time): # 列表也
        page2 = 'http://www.rgznworld.com/ajax/index/lists?callback=jQuery191034534395701151865_1542781471027&categoryid=10&lasttime=%s'

        pub_time = str(int(time.mktime(time.strptime(pub_time, '%Y-%m-%d %H:%M'))))
        page2url = page2 % str(pub_time)

        resp_page = requests.get(page2url).text
        print resp_page
        a_list = re.findall(r'html\\\/(\d+)\\\/(\d+)\\\/a0(\d+)\.html"', resp_page)
        self.parse_pages(a_list)

    def parse_pages(self,a_list): # 解析详情页
        detailurl = 'http://www.rgznworld.com/html/%s/%s/a0%s.html'
        for nums in a_list:
            print detailurl % (str(nums[0]), str(nums[1]), str(nums[2]))
            self.pase_datail(detailurl % (str(nums[0]), str(nums[1]), str(nums[2])))
        self.parse_m_pages(a_list)

    def parse_m_pages(self,a_list):  # 多页
        detailurl = 'http://www.rgznworld.com/html/%s/%s/a0%s.html'
        print detailurl % (str(a_list[-1][0]), str(a_list[-1][1]), str(a_list[-1][2]))
        resp = requests.get(detailurl % (str(a_list[-1][0]), str(a_list[-1][1]), str(a_list[-1][2]))).text
        pq_resp = pq(resp)
        pub_time = '20'+ pq_resp('div.text_nr_pl > p').text()
        pub_time = str(int(time.mktime(time.strptime(pub_time, '%Y-%m-%d %H:%M'))))
        self.list_page(pub_time)

    def pase_datail(self,url):
        data = {}
        response = requests.get(url).text
        data["title"] = pq(response)('div.text_nr>h2').text()
        print data

    def run(self):
        # pass
        self.pase_index()
#
if __name__ == '__main__':
    ai = Ai()
    ai.run()

# for t in doc('div.list_block ').items():
#     pub_time = t('p.biaozhu_time').text()
#     print pub_time
# print pub_time,'*'*10

# page2 = 'http://www.rgznworld.com/ajax/index/lists?callback=jQuery191034534395701151865_1542781471027&categoryid=10&lasttime=1542641400'
# # page3 = 'http://www.rgznworld.com/ajax/index/lists?callback=jQuery191034534395701151865_1542781471027&categoryid=10&lasttime=1542450612'
# #
# resp2 = requests.get(page2).text
# print resp2
# print re.findall(r'html(.*?)\.html"',resp2)
#
# print requests.get(page3).text


# http://www.rgznworld.com/ajax/index/lists?callback=jQuery191019423247184320358_1542800860594&categoryid=10&lasttime=1542688213&_=1542800860596
# http://www.rgznworld.com/ajax/index/lists?callback=jQuery191019423247184320358_1542800860594&categoryid=10&lasttime=1542468608&_=1542800860597
# http://www.rgznworld.com/ajax/index/lists?callback=jQuery191019423247184320358_1542800860594&categoryid=10&lasttime=1542277819&_=1542800860598
# http://www.rgznworld.com/ajax/index/lists?callback=jQuery191019423247184320358_1542800860594&categoryid=10&lasttime=1542184212&_=1542800860599








