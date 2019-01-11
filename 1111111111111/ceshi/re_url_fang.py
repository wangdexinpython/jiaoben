

import re
# url1 = "http://soufunappesf.3g.fang.com/http/sfservice.jsp?city=%E5%8C%97%E4%BA%AC&houseids=413070236&messagename=esf_searchListByIds&wirelesscode=0AED215ACA8A9FCA91AFD629C9A19E6C"
url = 'data-phone="18324503219"'
res = re.findall(r'data-phone=\"(\d{11})\"',url)
# https://m.fang.com/my/?c=mycenter&a=ajaxAddMySelectOfFangYuan&city=bj&houseid=412827828&housetype=FAGT&channel=esf
# https://m.fang.com/my/?c=mycenter&a=ajaxAddMySelectOfFangYuan&city=bj&houseid=411681300&housetype=FAGT&channel=esf
# https://m.fang.com/my/?c=mycenter&a=ajaxAddMySelectOfFangYuan&city=bj&houseid=60992693&housetype=JX&LeaseStyle=%BA%CF%D7%E2&channel=rent&groupid=undefined&agentid=
print(res)

# import requests
# import json
# def apps_():
#     # url1 = "https://mtsapi.house365.com/secure/?method=newhouse.getLoanRateNew&city=nj&client=tf&version=7.2.31&v=7.2.31&commitId=33a9025&api_key=android"
#     url = 'https://mtsapi.house365.com/secure/?method=secondhouse.getHouseDetail&city=nj&client=tf&version=7.2.31&v=7.2.31&commitId=33a9025&api_key=android&name=HouseSell&id=206336748&app=sell'
#     res = requests.get(url).text
#     text = json.loads(res)
#     print(text)
#
#
# apps_()