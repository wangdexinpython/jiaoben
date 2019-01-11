


import requests
def requ():
    url = 'http://ygw.xz.gov.cn/ygw/zwgk/20181115/001001_c8c72c91-fdca-4fff-92c5-658ff45d85a9.htm'
    res = requests.get(url)
    res.encoding='gbk'
    print(res.text)
requ()