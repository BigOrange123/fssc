# -*- coding: UTF-8 -*-
'''
=================================================
@Project -> File   ：fssc -> GUI练习
@IDE    ：PyCharm
@Author ：Mr. Jiang
@Date   ：2020/7/22 15:57
@Desc   ：GUI练习
==================================================
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pprint
chormeOption = webdriver.ChromeOptions()
chormeOption.add_argument("--referer=https://www.zhipin.com/chongqing/")
# 加载chrome浏览器驱动
driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe", options=chormeOption) # 切记Chorme 是大写
driver.maximize_window() # 浏览器最大化
driver.get("https://www.zhipin.com/")
driver.implicitly_wait(5) # 隐式等待5S
action = ActionChains(driver)
action.key_down(Keys.F12).perform()
# 定位元素--点击登录链接
loginLink = driver.find_element_by_link_text("登录")
loginLink.click() # 点击元素

# 为元素赋值--账号密码
driver.find_element_by_name("account").send_keys("19923895692")
driver.find_element_by_name("password").send_keys("woniu01")
# 推拽验证码
# verificationCode0 = driver.find_element_by_id("nc_1_n1z") # 定位验证码
# verificationCode1 = driver.find_element_by_id("nc_2_n1z") # 定位验证码
# verificationCode2 = driver.find_element_by_id("nc_3_n1z") # 定位验证码
list = driver.find_elements_by_css_selector("div[class=nc_wrapper]")
for li in list:
    if li.size['width'] == 324:
        verificationCode = li.find_element_by_css_selector(".nc_iconfont.btn_slide")

        action.drag_and_drop_by_offset(verificationCode, 276, 0).perform()
        action.reset_actions()

# driver.quit()
# pprint.pprint(verificationCode0, verificationCode1, verificationCode2)
# actionChains = ActionChains(driver) # 创建一个新的ActionChains，将webdriver实例对driver作为参数值传入，然后通过WenDriver实例执行用户动作
# try:
# actionChains.drag_and_drop_by_offset(verificationCode, 276, 0) # 将验证码推拽至最右边
# actionChains.click_and_hold(verificationCode)
# actionChains.move_by_offset(565, 0)
# actionChains.release()
# actionChains.perform() # 执行操作
# except Exception as e:
#     print(e)
#     driver.quit()
driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[1]/div[2]/div[1]/form/div[6]/button').click()

# driver.quit() # 推出浏览器