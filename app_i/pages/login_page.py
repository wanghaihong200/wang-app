# -*- coding:utf-8 -*-
from BaseDriver.baseDriver import basedriver
from bases.my_appium import my_app
from bases.wang_logging import Log
import time

log = Log()

class loginPage():
    def __init__(self,driver,driver_i):
        self.driver = driver
        self.driver_i = driver_i

    # 微信登录
    def wechat(self):
        # 点击公众号
        self.driver_i.find_element(('xpath', '//*[@text="************"]')).click()
        log.info("微信登录")
        log.info("跳转随身易个人中心")
        # 点击个人中心，未登录，则自动跳转登录页面
        self.driver_i.find_elements(('id', "com.tencent.mm:id/acn"))[2].click()

    # 随身易登录
    def login(self,phoneNum="13391387808"):
        self.driver_i.send_keys(('id', 'phone'),phoneNum)
        self.driver_i.send_keys(('id', 'verifyCode'), '123456')
        self.driver_i.find_element(('id', 'submit')).click()
        log.info("随身易登录成功")

    # 随身易解绑
    def unbind(self):
        time.sleep(2)
        self.driver_i.find_elements(('class name', "android.widget.Image"))[0].click()
        time.sleep(1)
        for i in range(2):
            self.driver.swipe(300, 1200, 300, 500, 1000)
        self.driver_i.find_element(('id', 'unbind')).click()
        self.driver_i.find_element(('id', 'com.tencent.mm:id/an3')).click()
        log.info("随身易解绑成功")


if __name__ == "__main__":
    driver = basedriver()
    driver_i = my_app(driver)
    loginPage(driver,driver_i).wechat()

    # loginPage(driver,driver_i).login()
    phoneNum = "13391387808"
    time.sleep(2)
    commission = driver_i.find_elements(('class name','android.view.View'))[5].get_attribute('name')
    log.info("手机号：%s，初始佣金：%s"%(phoneNum,commission))
    points = driver_i.find_elements(('class name','android.view.View'))[6].get_attribute('name')
    log.info("手机号：%s，初始积分：%s" % (phoneNum, points))
    time.sleep(2)

    # time.sleep(2)
    # loginPage(driver,driver_i).unbind()
