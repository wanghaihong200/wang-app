# -*- coding:utf-8 -*-
import unittest
from pages.login_page import loginPage
from pages.sign_page import signPage
from BaseDriver.baseDriver import basedriver
from bases.wang_logging import Log
from bases.my_appium import my_app
from BeautifulReport import BeautifulReport
import os

log = Log()
phoneNum = "13391387808"

class wx_order(unittest.TestCase):
    driver = None
    img_path = 'img'

    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))

    @classmethod
    def setUpClass(cls):
        cls.driver = basedriver()
        cls.driver_i = my_app(cls.driver)
        log.info("测试开始")



    @BeautifulReport.add_test_img('登录微信',"随身易登录")
    def test01_login(self):
        # self.save_img('登录微信')
        loginPage(self.driver_i).wechat()
        # loginPage(self.driver_i).login()
        # self.save_img('随身易登录')

    @BeautifulReport.add_test_img('随身易签约', "随身易登录")
    def test02_sign(self):
        signPage(self.driver, self.driver_i).signContract()
        # self.save_img('随身易签约')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        log.info("测试结束")
