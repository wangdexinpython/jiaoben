#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangdexin

# 2018-07-09 10:41:40
inputdate = '2018-07-09 10:41:40'
import time
from datetime import datetime
d_now = datetime.now()
d1 = datetime.strptime(inputdate, '%Y-%m-%d %H:%M:%S')
day = (d_now-d1).days
print(day)
