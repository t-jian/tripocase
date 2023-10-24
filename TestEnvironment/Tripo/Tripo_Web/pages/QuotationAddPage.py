# searchPage.py 代码如下
# _*_ coding:utf-8 _*_

__author__ = 'David'

import sys
from selenium.webdriver.common.by import By
import time
import os
import pyperclip
from webdriver_helper import get_webdriver
import pytest
# reload(sys)
# sys.setdefaultencoding("utf-8")
from Tripo.Tripo_Web.pages.BasePage import *


# 百度搜索page
from Tripo.Tripo_Web.pages.QuotationPage import QuotationPage


class QuotationAddPage(BasePage):
    # 元素集
    # 抬头
    # 团
    fieldgroup = "//span[contains(.,'套票')]"
    fieldgroupadd = ".add-icon > svg"
    fieldgroupcontent1 = ".ant-select-selection--multiple > .ant-select-selection__rendered"
    fieldgroupdefault1 = ".ant-select-dropdown-menu-item-active"
    fieldgroupitem2 = ".ant-select-dropdown-menu-item:nth-child(2)"
    # fieldgroupitem2 = ".ant-select-dropdown ant-select-dropdown--multiple ant-select-dropdown-placement-bottomLeft > ul > li:nth-child(2)"
    # fieldgroupitem2 = ".ant-select-dropdown-menu-item-active"
    fieldgroupitem3 = ".ant-select-dropdown-menu-item:nth-child(3)"
    fieldgroupitem4 = ".ant-select-dropdown-menu-item:nth-child(4)"
    fieldgroupitem5 = ".ant-select-dropdown-menu-item:nth-child(5)"
    fieldgroupitem6 = ".ant-select-dropdown-menu-item:nth-child(6)"
    fieldgroupitem7 = ".ant-select-dropdown-menu-item:nth-child(7)"
    fieldgroupitem8 = ".ant-select-dropdown-menu-item:nth-child(8)"
    fieldgroupitem9 = ".ant-select-dropdown-menu-item:nth-child(9)"
    fieldgroupname1 = ".line-2 > .item-box:nth-child(1) > .ant-input"
    fieldgroupcontacts1 = ".line-2 > .item-box:nth-child(2) > .ant-input"
    fieldgroupautofare1 = ".line-4 > .ant-btn-primary"
    fieldgroupdescription = "//div[@id='content']/div/div[3]/div[3]/div[5]/div[2]/div/div/div[3]/div/textarea"
    fieldgroupremark = "//div[@id='content']/div/div[3]/div[3]/div[5]/div[2]/div/div/div[3]/div[2]/textarea"

    fieldgroupcontent2 = "//div[5]/div[2]/div/div[2]/div/div[3]/div/div"
    fieldgroupname2 = ".item:nth-child(2) > .line-2 > .item-box:nth-child(1) > .ant-input"
    fieldgroupcontacts2 = "item:nth-child(2) > .line-2 > .item-box:nth-child(2) > .ant-input"
    fieldgroupautofare2 = ".item:nth-child(2) .ant-btn-primary"

    # 乘客
    # fieldpassenger = ".ant-tabs-tab:nth-child(6) > .tab-badge"
    fieldpassenger = "#passenger"
    fieldpassengerfirstname = "#passagerForm_firstname"
    fieldpassengersecondname = "#passagerForm_secondname"
    fieldpassengeradd = ".line > .ant-btn"
    fieldpassengerdefault = "/html/body/div[1]/div/div/div[2]/div/div[3]/div[3]/div[6]/div[2]/div/form/div/div[6]/table/tbody/tr/td[1]/span/label/span/input"
    filedchoicefirstpassenger = "tr:nth-child(1) > .max-width-td .ant-checkbox-input"
    # 最后提交
    fieldfinalamount = ".total-amount:nth-child(2)"
    # fieldfinalcheck = ".confirm-bar > .ant-btn ant-btn-primary ant-btn-lg"
    # fieldfinalcheck = ".ant-btn:nth-child(2)"
    fieldfinalcheck = "#content > div > div.bottom-bar > div > button"

    # fieldfinalcheck = "//button[@type='button']"


    def group13579(self, textgroupname, textgroupcontacts, textgroupdescription, textgroupremark):
        # 創建團
        self.xpathclick(self.fieldgroup)
        self.cssclick(self.fieldgroupadd)
        self.cssclick(self.fieldgroupcontent1)
        self.cssclick(self.fieldgroupdefault1)
        self.cssclick(self.fieldgroupitem3)
        self.cssclick(self.fieldgroupitem5)
        self.cssclick(self.fieldgroupitem7)
        self.cssclick(self.fieldgroupitem9)
        self.cssclick(self.fieldgroupcontent1)
        self.csssend(self.fieldgroupname1, textgroupname)
        self.csssend(self.fieldgroupcontacts1, textgroupcontacts)
        self.cssclick(self.fieldgroupautofare1)
        self.xpathperclip(self.fieldgroupdescription, textgroupdescription)
        self.xpathperclip(self.fieldgroupremark, textgroupremark)
        print("已成功创建一个团")
        print("添加完团后的金额显示", self.cssreturntext(self.fieldfinalamount))



    def passenger(self, textpassengerfirstname, textpassengersecondname):
        self.cssclick(self.fieldpassenger)
        self.csssend(self.fieldpassengerfirstname, textpassengerfirstname)
        self.csssend(self.fieldpassengersecondname, textpassengersecondname)
        self.cssclick(self.fieldpassengeradd)
        print("已成功添加一個乘客")

    def choicepassenger(self):
        self.cssclick(self.filedchoicefirstpassenger)


    def finalcheck(self):
        time.sleep(1)
        print("创建页面显示", self.cssreturntext(self.fieldfinalamount))
        self.cssclick(self.fieldfinalcheck)
        print("已成功创建一个订单")
        # time.sleep(1000)

    def riseinvoice(self, textdiscount):
        # 选择客户
        c = QuotationPage(self.driver)
        c.riseinvoice(textdiscount)

    # 創建報價單
    def risequotation(self, textdiscount):
        # 选择客户
        c = QuotationPage(self.driver)
        c.risequotation(textdiscount)

    # xo抬头部分
    def risexo(self, textdiscount):
        # 选择客户
        c = QuotationPage(self.driver)
        c.risexo(textdiscount)



