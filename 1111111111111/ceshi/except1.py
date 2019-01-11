# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-


# a=10
# b=0
# try:
#     c = b/a
#     print c
# except (IOError ,ZeroDivisionError),x:
#     print x.message
# else:
#     print "no error"
# print "done"
# inputValue=input("please input a int data :")
# if type(inputValue)!=type(1):
#     raise ValueError
#
# else:
#     print inputValue
a=10
b=0
try:
    print a/b
finally:
    print "always excute"