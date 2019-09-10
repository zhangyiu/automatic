from selenium import webdriver
from time import sleep
import unittest
import os
import HTMLTestRunner
import datetime
import xlrd
import login
import test
import platform
import ssl
import json
from http.client import HTTPConnection, HTTPSConnection
ssl._create_default_https_context = ssl._create_unverified_context




class foxconn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
        self.parameter=xlrd.open_workbook(r'foxconn.xlsx').sheet_by_name('Sheet1')
        
        
    def test_foxconn_case1_login(self):

        login.case1(self)

    def test_foxconn_case2_login(self):
    
        login.case2(self)

    def test_foxconn_case3_index(self):

        login.case3(self)
        
        
    def tearDown(self):
        self.driver.quit()


class interface(unittest.TestCase):
    def setUp(self):
        self.https = HTTPSConnection("center.foxconn.honeywell.com")
        
        
    def test_interface_case1_login(self):

        test.case1(self)

    def test_interface_case2_login(self):
        
        test.case2(self)

    def test_interface_case3_index(self):

        test.case3(self)
        
        
    def tearDown(self):
        self.https.close()

def run():
    testunit = unittest.TestSuite()
    if(platform.system()=='Windows'):
        testunit.addTest(unittest.makeSuite(foxconn))
    else:
        testunit.addTest(unittest.makeSuite(interface))
    filepath = os.getcwd()
    time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    time = str(time)
    time += "_result.html"
    if(platform.system()=='Windows'):
        filename = filepath + '\\' + time
    else:
        filename = filepath + '//' + time
    
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="用例执行情况")
    runner.run(testunit)
    fp.close()

if __name__ == "__main__":

    run()
