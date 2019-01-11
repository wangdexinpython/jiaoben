


import re
import requests

s= requests.session()
s.proxies = {'http':"61.135.217.1:80"}
print(s.get('http://httpbin.org/ip').json())
