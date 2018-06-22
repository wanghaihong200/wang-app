# -*- coding:utf-8 -*-
import unittest
from pages.login_page import loginPage
from pages.shopping_page import shoppingPage
from BaseDriver.baseDriver import basedriver
from bases.my_appium import my_app
from bases.wang_logging import Log
from BeautifulReport import BeautifulReport
import os
import time
from ddt import ddt,data,unpack

log = Log()
phoneNum2 = "13391387853"

@ddt
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

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        log.info("测试结束")

    @data('13391387841', '13391387840', '13391387842', '13391387843')
    # @BeautifulReport.add_test_img()
    def test00_login(self,phoneNum):
        # 登录微信公众号【随身易】
        loginPage(self.driver,self.driver_i).wechat()
        # 登录随身易
        loginPage(self.driver,self.driver_i).login(phoneNum)

        #记录初始佣金与积分
        time.sleep(2)
        commission = self.driver_i.find_elements(('class name','android.view.View'))[5].get_attribute('name')
        log.info("手机号：%s，初始佣金：%s"%(phoneNum,commission))
        points = self.driver_i.find_elements(('class name','android.view.View'))[6].get_attribute('name')
        log.info("手机号：%s，初始积分：%s" % (phoneNum, points))
        time.sleep(2)

        # 购买e生宝2017
        shoppingPage(self.driver,self.driver_i).shopping()
        shoppingPage(self.driver,self.driver_i).e_2017(phoneNum2)

        # 点击个人中心
        log.info("进入个人中心")
        self.driver_i.find_elements(('id', "com.tencent.mm:id/acn"))[2].click()

        # 解绑随身易
        loginPage(self.driver,self.driver_i).unbind()



