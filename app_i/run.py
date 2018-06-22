# -*- coding:utf-8 -*-
from BeautifulReport import BeautifulReport
import os
import unittest
import time


cases_path = os.path.join(os.getcwd(), "cases")
report_path = os.path.join(os.getcwd(), "report")


if __name__ == "__main__":

    test_suite = unittest.defaultTestLoader.discover(cases_path, pattern='case_shopp*.py')
    result = BeautifulReport(test_suite)
    fileName = "result_" + "%s.html" % time.strftime("%Y_%m_%d_%H_%M_%S")
    result.report(filename=fileName, description='随身易一键多账号出单测试报告', log_path=report_path)
