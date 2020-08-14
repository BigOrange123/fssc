# -*- coding: UTF-8 -*-
'''
=================================================
@Project -> File   ：fssc -> login
@IDE    ：PyCharm
@Author ：Mr. Jiang
@Date   ：2020/8/13 14:01
@Desc   ：
==================================================
'''
import os
import time
import pytest
from selenium import webdriver

def setup_module():
    global driver
    driver = webdriver.Chrome("../driver/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)

def teardown_module():
    global driver
    driver.quit()

def test_login_01():
    global driver
    driver.get("http://172.30.37.124/#/login")
    driver.find_element_by_name("userAccount").send_keys("yangxun")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector(".el-button.el-button--primary").click()

def test_login_02():
    time.sleep(2)
    global driver
    driver.get("http://172.30.37.124/#/login")
    driver.find_element_by_name("userAccount").send_keys("yangxun")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector(".el-button.el-button--primary").click()

# if __name__ == '__main__':
#     pytest.main(['test_01_login.py', '-s']) # , '--alluredir=../allureReport/myAllureReport'
#     # os.system('pytest serve ../allureReport/myAllureReport')
