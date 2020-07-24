# -*- coding: UTF-8 -*-
'''
=================================================
@Project -> File   ：fssc -> common
@IDE    ：PyCharm
@Author ：Mr. Jiang
@Date   ：2020/7/24 16:18
@Desc   ：GUI公共方法
==================================================
'''

'''
    @Author:Mr. Jiang    
    @Date:2020/7/24 16:20
    @Desc:打开浏览器函数
'''
from selenium import webdriver


def openBrowser(driverPath, requestPath):
    driver = webdriver.Chrome(driverPath)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(requestPath)
    return driver

'''
    @Author:Mr. Jiang    
    @Date:2020/7/24 16:23
    @Desc:封装定位元素函数
'''


def findElement(driver, method, value):
    if method == "id":
        ele = driver.find_element_by_id(value)
        return ele
    if method == "name":
        ele = driver.find_element_by_name(value)
        return ele
    if method == "css":
        ele = driver.find_element_by_css_selector(value)
        return ele
    if method == "text":
        ele = driver.find_element_by_link_text(value)
        return ele
    if method == "class":
        ele = driver.find_element_by_class_name(value)
        return ele

'''
    @Author:Mr. Jiang    
    @Date:2020/7/24 16:33
    @Desc:封装对元素动作函数
'''