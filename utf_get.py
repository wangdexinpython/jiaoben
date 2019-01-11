#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangdexin
from lxml import etree
import json
import requests,re
from requests import utils
url = 'http://www.innomd.org/appliance/web/innovatenews/detail?id=389489066499840'
html = requests.get(url)
selector = etree.HTML(html.text)
content = selector.xpath('//p[@id="remark"]/script/text()')
str1 = content[0].replace('%u', '\\u')
str1 = utils.unquote(str1)
cont = str1.encode('utf-8').decode('unicode_escape')
print(cont)







