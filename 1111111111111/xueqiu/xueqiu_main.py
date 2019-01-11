

import requests

def run():
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

    url = "https://xueqiu.com/u/8801386347"
    res = requests.get(url,headers = headers)

    result = res.text
    print(result)



run()