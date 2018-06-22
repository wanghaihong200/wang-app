# -*- coding:utf-8 -*-
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 对appium定位方法进行二次封装
class my_app():
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,loc):
         # 重写查找元素的方法, 暂时不成功，与selenium有区别
         '''
                 定位元素，参数locator是元祖类型
                 Usage:
                     locator = ("id","xxx")
                     BaseDriver.find_element(locator)

                    by_id= "id"
                    by_xpath = "xpath"
                    by_link_text = "link text"
                    by_class_name = "class name"
                    accessibility_id 用 xpath， //*[@content-desc='']
        '''
         try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
         except:
            print("%s 页面中未找到%s 元素"%(self,loc))

    def find_elements(self,loc):
         # 重写查找元素的方法
         '''
                 定位元素，参数locator是元祖类型
                 Usage:
                     locator = ("id","xxx")
                     BaseDriver.find_element(locator)

                    by_id= "id"
                    by_xpath = "xpath"
                    by_link_text = "link text"
                    accessibility_id 用 xpath， //*[@content-desc='']
                    by_class_name = "class name"
        '''
         try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(loc))
            return self.driver.find_elements(*loc)
         except:
            print("%s 页面中未找到%s 元素"%(self,loc))

    def send_keys(self, loc, value):
        # 重写在文本框中输入内容的方法
        self.find_element(loc).send_keys(value)

    def find_toast(self, message):
        # 判断toast消息
        try:
            toast_loc = ("XPATH", ".//*[contains(@text,'%s')]" % message)
            WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(toast_loc))
            return True
        except:
            return False

if __name__ == "__main__":
    from bases.my_base import random_name, random_id
    from BaseDriver.baseDriver import basedriver
    import os

    PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

    phone_num = '13391387821'

    driver = basedriver()
    driver_i = my_app(driver)
    # 点击公众号
    driver_i.find_element(('id','com.tencent.mm:id/as6')).click()
    # 点击产品中心
    driver_i.find_elements(('id', "com.tencent.mm:id/acn"))[1].click()
    #登录
    driver_i.send_keys(('id', 'phone'),phone_num)
    driver_i.send_keys(('id', 'verifyCode'), '123456')
    driver_i.find_element(('id', 'submit')).click()
    #点击产品
    driver_i.find_element(('xpath',"//*[@content-desc=' 产品']")).click()
    # 点击医疗
    driver_i.find_element(('xpath',"//*[@content-desc='医疗']")).click()

    # 点击E生宝2017
    driver_i.find_element(('id','productDetails0')).click()

    # 点击立即投保
    driver_i.find_element(('id','立即投保')).click()

    # 滑动屏幕到底
    time.sleep(1)
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    for i in range(0,4):
        driver.swipe(0.5 * x, 0.9 * y, 0.5 * x, 0.05 * y, 1000)

    # 点击【以上全否】
    driver_i.find_element(('id','notAll')).click()
    # 输入投保人姓名
    driver_i.send_keys(('id','holderName'), random_name())
    # 选择证件类型为护照
    driver_i.find_element(('id','holderIdType')).click()
    driver_i.find_elements(('class name','android.widget.ImageView'))[1].click()
    # 输入随机护照号
    driver_i.send_keys(('id','holderIdNo'),random_id())
    # 输入生日
    driver_i.find_element(('id','holderBirthday')).click()
    for i in range(8):
        driver.swipe(300, 900, 300, 1200, 1000)

    driver_i.find_element(('xpath', "//*[@content-desc='确定']")).click()
    # 输入手机号
    driver_i.send_keys(('id','holderMobile'), phone_num)
    # 滑动屏幕到底
    driver.swipe(0.5 * x, 0.9 * y, 0.5 * x, 0.05 * y, 1000)
    time.sleep(1)
    # 点击立即付款
    driver_i.find_element(('xpath', "//*[@content-desc='立即付款']")).click()
    # 点击确定
    driver_i.find_element(('id','mb_btn_ok')).click()

    # 微信确认支付
    driver_i.find_element(('id','lyj_confirmMethod')).click()

