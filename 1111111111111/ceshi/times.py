#
#
import time
import datetime

#日期转换为时间戳
# today_time = datetime.datetime.now()
# today_time2 = time.time()
# print(today_time)
# print(today_time2)
#
# data1 = datetime.timedelta(minutes=8)
# data2 = datetime.timedelta(hours=3)
#
# print(data1)
# print(data2)
#
# jian_value = today_time-data2
# print(jian_value)
# value = time.mktime(jian_value.timetuple())
# print(value)
#时间戳转换为日期
rr = time.gmtime(time.time())
rr = time.strftime("%Y-%m-%d %H:%M:%S",rr)
print(rr)
#
# tss1 = '2018-06-22 15:18:43'
# tm = time.strptime(tss1,'%Y-%m-%d %H:%M:%S')
# timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
# print(tm)
# print(timeArray)

timeStamp = 1381419600
timeArray = time.localtime(timeStamp)
print(timeArray)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print otherStyleTime