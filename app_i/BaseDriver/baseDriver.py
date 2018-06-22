# -*- coding:utf-8 -*-
from appium import webdriver



def basedriver():
    desired_caps = {
            'platformName': 'Android',
            'platformVersion': '8.0',
            'deviceName': 'GWY0217823000028',
            'appPackage': 'com.tencent.mm',
            "appActivity": "com.tencent.mm.ui.LauncherUI",
            "noReset": "True",
            'unicodeKeyboard': 'True',
            'resetKeyboard': 'True',
            'chromeOptions': {
            'androidProcess': 'com.tencent.mm:tools'
            }
        }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    return driver

