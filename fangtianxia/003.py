
# -*- coding: utf-8 -*-
import os
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://passport.fang.com/?backurl=http://yt.fang.com/?s=BDPZ-BL")

ret1 = driver.title
#
# ret1 = driver.find_element_by_xpath("//span[test()='账号密码登录']").click()
print(ret1)
# # 输出为：<selenium.webdriver.remote.webelement.WebElement (session="ea6f94544ac3a56585b2638d352e97f3", element="0.5335773935305805-1")>
#
# ret2 = driver.find_element_by_id("username").send_keys("17600043315")
# print(ret2)
# # 输出为：[<selenium.webdriver.remote.webelement.WebElement (session="ea6f94544ac3a56585b2638d352e97f3", element="0.5335773935305805-1")>]
#
# ret3 = driver.find_element_by_id("password").send_keys("111111")
# print(len(ret3))
# # 输出为：1
#
# ret4 = driver.find_element_by_id("loginWithPswd").click()