

import re

url = "http://m.jingzhengu.com/ershouche/c/-j2-0-0-0-0-0-0-0-0-0-1-0-0-0-0t.html"

res = re.findall(r".*(?:m.jingzhengu.com)/ershouche/(\w+)/[\-j201]{1,}t.html",url)

print(res)


# .*m\.che168\.com/(\w+)/list/\?kw=.*&pvareaid=\d+&sw=.*_x0001_.*m\.che168\.com/\w+/list/\?kw=(.*)&pvareaid=\d+&sw=.*_x0001_.*m\.che168\.com/\w+/list/\?kw=.*&pvareaid=(\d)+&sw=.*_x0001_.*m\.che168\.com/\w+/list/\?kw=.*&pvareaid=\d+&sw=(.*)