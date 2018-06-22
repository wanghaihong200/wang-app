# -*- coding:utf-8 -*-
import time
from bases.my_base import random_name,random_id
from bases.wang_logging import Log

log = Log()

class shoppingPage():
    def __init__(self,driver,driver_i):
        self.driver = driver
        self.driver_i = driver_i

    def shopping(self):
        # 点击产品
        self.driver_i.find_element(('xpath',"//*[@content-desc=' 产品']")).click()
        # 点击医疗
        self.driver_i.find_element(('xpath', "//*[@content-desc='医疗']")).click()

    def e_2017(self,phoneNum):
        # 点击E生宝2017
        self.driver_i.find_element(('id', 'productDetails0')).click()

        # 点击立即投保
        self.driver_i.find_element(('id', '立即投保')).click()

        # 滑动屏幕到底
        time.sleep(1)
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        for i in range(0, 4):
            self.driver.swipe(0.5 * x, 0.9 * y, 0.5 * x, 0.05 * y, 1000)

        # 点击【以上全否】
        self.driver_i.find_element(('id', 'notAll')).click()
        # 输入投保人姓名
        self.driver_i.send_keys(('id', 'holderName'), random_name())
        # 选择证件类型为护照
        self.driver_i.find_element(('id', 'holderIdType')).click()
        self.driver_i.find_elements(('class name', 'android.widget.ImageView'))[1].click()
        # BaseDriver.find_elements_by_class_name('android.widget.ImageView')[1].click()
        # 输入随机护照号
        self.driver_i.send_keys(('id', 'holderIdNo'), random_id())
        # 输入生日
        self.driver_i.find_element(('id', 'holderBirthday')).click()
        for i in range(10):
            self.driver.swipe(300, 900, 300, 1200, 1000)

        self.driver_i.find_element(('xpath', "//*[@content-desc='确定']")).click()
        # 输入手机号
        self.driver_i.send_keys(('id', 'holderMobile'), phoneNum)
        # 滑动屏幕到底
        self.driver.swipe(0.5 * x, 0.9 * y, 0.5 * x, 0.05 * y, 1000)
        time.sleep(1)
        # 点击立即付款
        self.driver_i.find_element(('xpath', "//*[@content-desc='立即付款']")).click()
        # 点击确定
        self.driver_i.find_element(('id', 'mb_btn_ok')).click()

        # 微信确认支付
        self.driver_i.find_element(('id', 'lyj_confirmMethod')).click()

        #返回公众号
        self.driver_i.find_element(('id', "com.tencent.mm:id/ht")).click()
        time.sleep(2)