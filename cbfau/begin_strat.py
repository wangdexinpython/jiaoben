#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:wangdexin

from selenium import webdriver
# import selenium

browser = webdriver.Chrome()



class Cbfau(object):




    def __init__(self):
        browser.get("http://www.baidu.com")
        print(browser.page_source)
        browser.close()

    def parse(self):

        pass

    def run(self):
        pass

# 69.0.3497.81


if __name__ == '__main__':
    cbfau = Cbfau()
    cbfau.run()