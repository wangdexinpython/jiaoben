# -*- coding: utf-8 -*-
# import urllib
# import urllib2
# import request

# with urllib2.request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

# -* - coding: UTF-8 -* -
import urllib2

request = urllib2.Request("http://www.baidu.com/")
# request.add_header('content-TYPE', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
# print response.getcode()
# print response.geturl()
# print response.read()
print response.headers