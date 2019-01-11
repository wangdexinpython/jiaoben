#!/usr/bin/python

from selenium import webdriver
driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()
driver.get("https://www.baidu.com")
# data = driver.title
print("++++++++++++++")
imgelement = driver.find_element_by_xpath("//*[@id='su']/text()")
print(imgelement)
# print data