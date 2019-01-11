#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
import json
import csv
from lxml import etree


class PretendUserAgent(object):
    def __init__(self):
        pass

    def process_request(self, i):
        url = 'https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/{}'.format(str(i))
        proxy = product_proxies()
        proxies = {
            'http': 'socks5://' + proxy,
            'https': 'socks5://' + proxy
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        }

        response = requests.get(url=url, proxies=proxies, headers=headers, timeout=10)
        return response.text

    def parse_response(self, response):
        tree = etree.HTML(response)
        tr_list = tree.xpath('//div[@class="corset"]//tr')
        user_agent_list = []
        for tr in tr_list:
            user_agent = tr.xpath('./td[@class="useragent"]/a/text()')
            version = tr.xpath('./td[2]/text()')
            # system_os = tr.xpath('./td[3]/text()')
            hardware_type = tr.xpath('./td[4]/text()')
            # common = tr.xpath('./td[5]/text()')
            if user_agent and version:
                user_agent_list.append((user_agent[0], version[0], hardware_type[0]))
        return user_agent_list

    def process_result(self, result):
        user_agent_list = []
        for ua in result:
            try:
                version = int(ua[1])
                if version > 60 and ua[2] == 'Computer':
                    user_agent_list.append(ua[0])
            except ValueError:
                pass

        self.save_user_agent(user_agent_list)

    def save_response(self, content):
        with open('chrom.html', 'wb')as myfile:
            myfile.write(content)

    def read_response(self):
        with open('chrom.html', 'r')as myfile:
            response = myfile.read()
        return response

    def save_user_agent(self, user_agent_list):
        with open('chrom.txt', 'a')as myfile:
            for user_agent in user_agent_list:
                user_agent = '"' + user_agent + '"' + ','
                myfile.write(user_agent)
                myfile.write('\n')

    def run(self):
        for i in range(1, 100):
            try:
                response = self.process_request(i)
                # self.save_response(response)
                # response = self.read_response()
                result = self.parse_response(response)
                self.process_result(result)
            except:
                pass


def product_proxies():
    proxy_info = requests.get("http://10.10.182.238:9091/?type=px001&qid=1529458890443&query={%22req%22:%20[{%22source%22:%20%22csairFlight%22,%20%22num%22:%201,%20%22type%22:%20%22verify%22,%20%22ip_type%22:%20%22test%22}]}&ptid=ptid&tid=tid&ccy=AUD").content
    proxy = json.loads(proxy_info)['resp'][0]['ips'][0]['inner_ip']
    print proxy
    return proxy


if __name__ == '__main__':
    ua = PretendUserAgent()
    ua.run()
