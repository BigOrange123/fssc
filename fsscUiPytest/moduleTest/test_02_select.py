# -*- coding: UTF-8 -*-
'''
=================================================
@Project -> File   ：fssc -> select
@IDE    ：PyCharm
@Author ：Mr. Jiang
@Date   ：2020/8/13 14:56
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

def test_select_01():
    print(1)

def test_select_02():
    print(2)