# -*- coding: UTF-8 -*-
'''
=================================================
@Project -> File   ：fssc -> common
@IDE    ：PyCharm
@Author ：Mr. Jiang
@Date   ：2020/7/24 16:18
@Desc   ：
==================================================
'''
import unittest
from fsscGUI.common import common
from ddt import ddt, data, unpack


@ddt
class loginTestCase(unittest.TestCase):
    driver = common.openBrowser(driverPath="../driver/chromedriver.exe",
                                requestPath="http://172.30.37.124/#/login")
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    @data(("yangxun", "admin"))
    @unpack
    def test_login(self, userAccount, password):
        self.driver.find_element_by_name("userAccount").send_keys(userAccount)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_css_selector(".el-button.el-button--primary").click()
        # userAccount = common.findElement(driver=self.driver, method="name", value="userAccount")
        # userAccount.send_keys("yangxun")
        # password = common.findElement(driver=self.driver, method="name", value="password")
        # password.send_keys("admin")
        # loginBtn = common.findElement(driver=self.driver, method="css", value=".el-button.el-button--primary")
        # loginBtn.click()



if __name__ == '__main__':
    unittest.main()
