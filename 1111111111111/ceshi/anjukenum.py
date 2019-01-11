# -*- coding=utf-8 -*-



import requests,json
from lxml import etree
list1 = []

for i in range(1,71):
    url1 = 'http://bj.58.com/chuzu/1/pn{}?PGTID=0d3090a7-0000-15f7-6996-d0b1deada02f&ClickID=2'.format(i)

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }

    response = requests.get(url1,headers=headers)
    data = response.content
    html = etree.HTML(data)
    link_list = html.xpath("//a[contains(text(),'下一页')]/@href")
    for link in link_list:
        response1 = requests.get(url=link,headers=headers)
        data2 = response1.content
        html2 = etree.HTML(data2)
        a = html2.xpath("//*[@id='bigCustomer']/p[1]/a/text()")
        # print(a)
        list1.extend(a)
result = len(set(list1))
print(result)
