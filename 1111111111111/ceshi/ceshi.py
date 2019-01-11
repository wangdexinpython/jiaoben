# -*- coding: utf-8 -*-
# import re
# import json
# import datetime
# import time
# class fun():
#
#
#     # ba = {'regex' : '\d+'}
#     # val = {'data':'747477'}
#     def extract(self, *args, **kwargs):
#         print ("sssssssssssssssssss")
#         # data_list = re.findall(kwargs.get("regex"), str(kwargs.get("data")))
#         # data_list = re.search(kwargs.get("regex"), str(kwargs.get("data")))
#         pat = re.compile(kwargs.get("regex").encode("utf-8"))
#         data_list = pat.findall(kwargs.get("data").encode("utf-8"))
#         mo = data_list
#         print mo
#         print (type(mo))
#         # value = len(data_list) > 0 and data_list.pop() or ""
#         value =data_list.pop() or ""
#         print (type(value))
#         print(value)
# a= fun()
# a.extract(data='483483743874', regex='(\d+)')

#
#
# today_time = datetime.datetime.now()
# time1 = time.time()
# print (time1)
# time2 = time.mktime(time1.timetuple())
# # time3 = datetime.timedelta(today_time)
#
# print (time2)
#
# print (today_time)





# !/usr/bin/env python
# coding=utf-8


# class MyList1(object):  # 定义可迭代对象类
#
#     def __init__(self, num):
#         self.data = num  # 上边界
#
#     def __iter__(self):
#         return MyListIterator1(self.data)  # 返回该可迭代对象的迭代器类的实例
#
#
# class MyListIterator1(object):  # 定义迭代器类，其是MyList可迭代对象的迭代器类
#
#     def __init__(self, data):
#         self.data = data  # 上边界
#         self.now = 0  # 当前迭代值，初始为0
#
#     def __iter__(self):
#         return self  # 返回该对象的迭代器类的实例；因为自己就是迭代器，所以返回self
#
#     def next(self):  # 迭代器类必须实现的方法
#         while self.now < self.data:
#             self.now += 1
#             return self.now - 1  # 返回当前迭代值
#         raise StopIteration  # 超出上边界，抛出异常
#
#
# my_list = MyList1(5)  # 得到一个可迭代对象
# print(type(my_list))  # 返回该对象的类型
#
# my_list_iter1 = iter(my_list)  # 得到该对象的迭代器实例，iter函数在下面会详细解释
# print(type(my_list_iter1))
# for i in my_list:  # 迭代
#     print(i)


# !/usr/bin/env python
# coding=utf-8


def myList(num):  # 定义生成器
    now = 0  # 当前迭代值，初始为0
    while now < num:
        val = (yield now)  # 返回当前迭代值，并接受可能的send发送值；yield在下面会解释
        now = now + 1 if val is None else val  # val为None，迭代值自增1，否则重新设定当前迭代值为val


my_list = myList(5)  # 得到一个生成器对象

print(my_list.next())  # 返回当前迭代值
print(my_list.next())

my_list.send(3)  # 重新设定当前的迭代值
print(my_list.next())

print(dir(my_list))  # 返回该对象所拥有的方法名，可以看到__iter__与next在其中
