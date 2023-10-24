# searchPage.py 代码如下
# _*_ coding:utf-8 _*_

__author__ = 'David'

import sys
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import time
import os
import pyperclip
from webdriver_helper import get_webdriver
import pytest
# reload(sys)
# sys.setdefaultencoding("utf-8")
from Tripo.Tripo_Web.pages.BasePage import *


# 百度搜索page
class LoginPage(BasePage):
    # 元素集
    webaccount = ".ant-row:nth-child(1) .ant-input"
    webpassword = ".ant-input-affix-wrapper > .ant-input"
    webcompanycode = ".ant-row:nth-child(3) .ant-input"
    weblogin = ".login-button"

    # 搜索输入框
    search_input = (By.ID, u'kw')
    # 百度一下 按钮
    search_button = (By.ID, u'su')


    def login(self, textaccount, textpassword, textcompanycode):

        # self.driver.get(web)
        # self.driver.set_window_size(1950, 939)
        self.driver.maximize_window()
        # input()
        # 3 | click | css=.ant-row:nth-child(1) .ant-input |
        self.driver.find_element(By.CSS_SELECTOR, self.webaccount).click()
        # 4 | type | css=.ant-row:nth-child(1) .ant-input | david
        self.driver.find_element(By.CSS_SELECTOR, self.webaccount).send_keys(textaccount)
        # 5 | pause | 1000 | 1000
        time.sleep(0.5)
        # 6 | click | css=.ant-input-affix-wrapper > .ant-input |
        self.driver.find_element(By.CSS_SELECTOR, self.webpassword).click()
        # 7 | type | css=.ant-input-affix-wrapper > .ant-input | Travel2021
        self.driver.find_element(By.CSS_SELECTOR, self.webpassword).send_keys(textpassword)
        # 8 | pause | 1000 | 1000
        time.sleep(0.5)
        # 9 | click | css=.ant-row:nth-child(3) .ant-input |
        self.lazyelement(By.CSS_SELECTOR, self.webcompanycode).click()
        # self.driver.find_element(By.CSS_SELECTOR, self.webcompanycode).click()
        # 10 | type | css=.ant-row:nth-child(3) .ant-input | TC0139
        self.driver.find_element(By.CSS_SELECTOR, self.webcompanycode).send_keys(textcompanycode)

        # 11 | click | css=.login-button |
        print("1")
        self.cssclick(self.weblogin)
        print("2")


        # self.driver.find_element(By.CSS_SELECTOR, self.weblogin).click()
        self.homepage_handle = self.driver.window_handles
        # input("测试")
        print("已点击登录")



    #
    # def gotoBaiduHomePage(self):
    #     print
    #     u"打开首页: ", self.base_url
    #     self.driver.get(self.base_url)
    #
    # def input_search_text(self, text=u"开源优测"):
    #     print
    #     u"输入搜索关键字： 开源优测 "
    #     self.input_text(self.search_input, text)
    #
    # def click_search_btn(self):
    #     print
    #     u"点击 百度一下  按钮"
    #     self.click(self.search_button)