# -*- coding:utf-8 -*-
import time
from bases.my_base import random_name,random_id
from bases.wang_logging import Log

log = Log()

class signPage():
    def __init__(self,driver,driver_i):
        self.driver = driver
        self.driver_i = driver_i

    def signContract(self):
        log.info('跳转个人中心')
        self.driver_i.find_element(('xpath','//*[@content-desc=" 我的"]')).click()

        log.info('点击【签约机构】，进入签约页面')
        self.driver_i.find_element(('id',"myContract")).click()

        log.info('点击【确定并签约】')
        self.driver_i.find_element(('id',"mb_btn_ok")).click()

        # log.info('输入真实姓名')
        # self.driver_i.send_keys(('id',"vname"),random_name())
        #
        # log.info('选择证件类型')
        # self.driver_i.find_element(('id', "idTypeVal")).click()
        # self.driver_i.find_element(('xpath','//*[@text="护照"]')).click()
        #
        # log.info("请输入您的证件号")
        # self.driver_i.send_keys(('xpath','//*[@text="请输入您的证件号"]'),random_id())
        #
        # log.info("选择民族")
        # self.driver_i.find_elements(('xpath', "//*[@content-desc='请选择']"))[0].click()
        # self.driver_i.find_element(('xpath', "//*[@text='汉族']")).click()
        #
        # log.info("选择性别")
        # self.driver_i.find_elements(('xpath', "//*[@content-desc='请选择']"))[0].click()
        # self.driver_i.find_element(('xpath', "//*[@text='男']")).click()

        # log.info("输入出生年月")
        # time.sleep(2)
        # js = 'document.getElementById("birthDate").removeAttribute("readonly");'
        # self.driver.execute_script(js)
        self.driver_i.send_keys(('id','birthDate'),"1978-08-21")

        time.sleep(2)
        self.driver_i.find_element(('id','android:id/date_picker_header_year')).click()
        time.sleep(2)
        for i in range(8):
            self.driver.swipe(500, 900, 500, 1200, 1000)


        log.info("选择文化程度")
        self.driver_i.find_elements(('xpath', "//*[@content-desc='请选择']"))[0].click()
        self.driver_i.find_element(('xpath', "//*[@text='博士']")).click()

        log.info("选择政治面貌")
        self.driver_i.find_elements(('xpath', "//*[@content-desc='请选择']"))[0].click()
        self.driver_i.find_element(('xpath', "//*[@text='群众']")).click()

        log.info("点击下一步")
        self.driver_i.find_element(('id',"next")).click()


if __name__ == "__main__":
    from pages.login_page import loginPage
    from BaseDriver.baseDriver import basedriver
    from bases.my_appium import my_app

    driver = basedriver()
    driver_i = my_app(basedriver())
    loginPage(driver,driver_i).wechat()

    signPage(driver,driver_i).signContract()







