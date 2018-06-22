# -*- coding:utf-8 -*-
import unittest
from pages.login_page import loginPage
from BaseDriver.baseDriver import basedriver
from bases.wang_logging import Log
from bases.my_appium import my_app
from BeautifulReport import BeautifulReport
import os
from ddt import ddt,data,unpack

log = Log()

@ddt
class wx_login(unittest.TestCase):
    driver = None
    img_path = 'img'

    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))

    def setUp(self):
        self.driver = basedriver()
        self.driver_i = my_app(self.driver)
        log.info("测试开始")

    def tearDown(self):
        self.driver.quit()
        log.info("测试结束")

    @data('13391387841','13391387840','13391387842','13391387843')
    @BeautifulReport.add_test_img('登录微信','微信商城')
    def test01_login(self,phoneNum):
        loginPage(self.driver,self.driver_i).wechat()
        self.save_img('登录微信')
        loginPage(self.driver,self.driver_i).login(phoneNum)
        self.save_img('微信商城')
        log.info("登录成功")
        loginPage(self.driver,self.driver_i).unbind()




if __name__ == "__main__":
    # unittest.main()是为了在cmd中也可以执行该py文件
    unittest.main()


