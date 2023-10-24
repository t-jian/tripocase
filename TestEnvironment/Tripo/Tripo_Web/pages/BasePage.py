# basePage.py代码如下

# _*_ coding:utf-8 _*_

__author__ = 'David'

import pyperclip
import pytest
import time
import sys

# reload(sys)
# sys.setdefaultencoding("utf-8")
from selenium.webdriver import Keys

homepage_handle = "1"
from webdriver_helper import get_webdriver
from selenium.webdriver.common.by import By

# pages基类


class BasePage(object):
    """
        Page基类，所有page都应该继承该类
    """

    # def __init__(self, driver, base_url=u"http://www.baidu.com"):
    #     self.driver = driver
    #     self.base_url = base_url
    #     self.timeout = 30

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.homepage_handle = homepage_handle
        self.url = "http://tripo.hotfix.travelconnect.co/#/login"
        # self.url = "http://tripo.staging.travelconnect.co/#/login"


    def lazyelement(self, *loc):
         while True:
             try:
                 # print("1")
                 self.driver.find_element(*loc)
                 break
             except:
                 time.sleep(0.5)

                 continue
         return self.driver.find_element(*loc)

    # def login3(self, textaccount, textpassword, textcompanycode):
    #
    #     # self.driver.get(web)
    #     # self.driver.set_window_size(1950, 939)
    #     self.driver.maximize_window()
    #     # input()
    #     # 3 | click | css=.ant-row:nth-child(1) .ant-input |
    #     self.driver.find_element(By.CSS_SELECTOR, self.webaccount).click()
    #     # 4 | type | css=.ant-row:nth-child(1) .ant-input | david
    #     self.driver.find_element(By.CSS_SELECTOR, self.webaccount).send_keys(textaccount)
#用css方式單擊
    def cssclick(self, value):
        # print(value)
        # print(self.value)
        a = 0
        while True:
            try:

                self.driver.find_element(By.CSS_SELECTOR, value).click()

                break
            except:
                a = a+1
                if a > 60:
                    self.driver.find_element(By.CSS_SELECTOR, value).click()
                else:
                    time.sleep(1)
                    continue
                # print("2")

                # print("超时")

# 用xpath方式單擊
    def xpathclick(self, value):
        # print(value)
        # print(self.value)
        while True:
            try:
                self.driver.find_element(By.XPATH, value).click()
                break
            except:
                time.sleep(1)
                continue
                # print("超时")

    # 用css寫數據
    def csssend(self, value, text):
        # print(value)
        # print(self.value)
        while True:
            try:
                self.driver.find_element(By.CSS_SELECTOR, value).click()
                self.driver.find_element(By.CSS_SELECTOR, value).send_keys(Keys.CONTROL, "a")
                self.driver.find_element(By.CSS_SELECTOR, value).send_keys(Keys.DELETE)
                self.driver.find_element(By.CSS_SELECTOR, value).send_keys(text)
                break
            except:
                time.sleep(1)
                # print("2")
                continue
                # print("超时")

    # 用path寫數據
    def xpathsend(self, value, text):
        # print(value)
        # print(self.value)
        while True:
            try:
                self.driver.find_element(By.XPATH, value).click()
                self.driver.find_element(By.XPATH, value).send_keys(Keys.CONTROL, "a")
                self.driver.find_element(By.XPATH, value).send_keys(Keys.DELETE)
                self.driver.find_element(By.XPATH, value).send_keys(text)
                break
            except:
                time.sleep(1)
                # print("2")
                continue
                # print("超时")

    # 用拷貝數據進去
    def cssperclip(self, value, text):
        # print(value)
        # print(self.value)
        while True:
            try:
                # self.driver.find_element(By.CSS_SELECTOR, value).click()
                # time.sleep(0.1)
                self.driver.find_element(By.CSS_SELECTOR, value).send_keys(Keys.CONTROL, "a")
                self.driver.find_element(By.CSS_SELECTOR, value).send_keys(Keys.DELETE)
                pyperclip.copy(text)  # 将长文本复制到剪切板
                self.driver.find_element(By.CSS_SELECTOR, value).send_keys(Keys.CONTROL,
                                                                                                'v')
                break
            except:
                time.sleep(1)
                # print("2")
                continue
                # print("超时")

    # 用拷貝數據進去
    def xpathperclip(self, value, text):
        # print(value)
        # print(self.value)
        while True:
            try:
                # self.driver.find_element(By.XPATH, value).click()
                # time.sleep(0.1)
                self.driver.find_element(By.XPATH, value).send_keys(Keys.CONTROL, "a")
                self.driver.find_element(By.XPATH, value).send_keys(Keys.DELETE)
                pyperclip.copy(text)  # 将长文本复制到剪切板
                self.driver.find_element(By.XPATH, value).send_keys(Keys.CONTROL,
                                                                                                'v')
                break
            except:
                time.sleep(1)
                # print("2")
                continue
                # print("超时")
#獲取元素文案
    def cssreturntext(self, value):
        # print(value)
        # print(self.value)
        b=0
        while True:
            try:
                b = self.driver.find_element(By.CSS_SELECTOR, value).text
                return b
            except:
                time.sleep(1)
                # print("2")
                continue
                # print("超时")

#獲取最新窗口
    def newHandle(self):
        handles = self.driver.window_handles
        # 循环handles找出新窗口的handle
        for handle in handles:
            for oldhandle in self.homepage_handle:
                if handle != oldhandle:
                    # 激活新窗口
                    self.driver.switch_to.window(handle)
                    self.homepage_handle = self.driver.window_handles
                    break




    # def find_element(self, *loc):
    #     return self.driver.find_element(*loc)
    #
    # def input_text(self, loc, text):
    #     self.find_element(*loc).send_keys(text)
    #
    # def click(self, loc):
    #     self.find_element(*loc).click()
    #
    # def get_title(self):
    #     return self.driver.title
