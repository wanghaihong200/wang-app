# -*- coding:utf-8 -*-
import time

from appium import webdriver

from base.my_base import random_name, random_id

phone_num = '13391387821'
desired_caps = {
    'platformName' : 'Android',
    'platformVersion': '8.0',
    'deviceName': 'GWY0217823000028',
    'appPackage': 'com.tencent.mm',
    "appActivity": "com.tencent.mm.ui.LauncherUI",
    "noReset": "True",
    'unicodeKeyboard': 'True',
    'resetKeyboard': 'True',
    'chromeOptions':{
    'androidProcess': 'com.tencent.mm:tools'
    }
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.implicitly_wait(10)
# 点击公众号
driver.find_element_by_id('com.tencent.mm:id/as6').click()
time.sleep(1)
# 点击产品中心
driver.find_elements_by_id('')[1].click()
time.sleep(3)

#点击医疗
driver.find_element_by_accessibility_id('医疗').click()
time.sleep(1)

#点击E生宝2017
driver.find_element_by_id('productDetails0').click()
time.sleep(1)

#点击立即投保
driver.find_element_by_accessibility_id('立即投保').click()
time.sleep(2)

#滑动屏幕到底
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
driver.swipe(0.5*x,0.9*y,0.5*x,0.05*y,1000)
driver.swipe(0.5*x,0.9*y,0.5*x,0.05*y,1000)

time.sleep(1)
#点击【以上全否】
driver.find_element_by_id('notAll').click()
time.sleep(1)
#输入投保人姓名
driver.find_element_by_id('holderName').send_keys(random_name())
# 选择证件类型为护照
driver.find_element_by_id('holderIdType').click()
driver.find_elements_by_class_name('android.widget.ImageView')[1].click()
# 输入随机护照号
driver.find_element_by_id('holderIdNo').send_keys(random_id())
# 输入生日

driver.find_element_by_id('holderBirthday').click()
time.sleep(1)
for i in range(8):
    driver.swipe(300,900,300,1200,1000)
# BaseDriver.find_element_by_accessibility_id('2010').click()
# BaseDriver.find_element_by_accessibility_id('2006').click()
# BaseDriver.find_element_by_accessibility_id('2002').click()

driver.find_element_by_accessibility_id('确定').click()
time.sleep(1)
#输入手机号
driver.find_element_by_id('holderMobile').send_keys(phone_num)
#滑动屏幕到底
driver.swipe(0.5*x,0.9*y,0.5*x,0.05*y,1000)
time.sleep(1)
#点击立即付款
driver.find_element_by_accessibility_id('立即付款').click()
time.sleep(2)
# 点击确定
driver.find_element_by_id('mb_btn_ok').click()

# 微信确认支付
driver.find_element_by_id('lyj_confirmMethod').click()