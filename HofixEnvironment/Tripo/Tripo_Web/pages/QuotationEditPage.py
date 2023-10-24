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


class QuotationEditPage(BasePage):
    # 元素集
    # 编辑航线项目
    field_route_button = '//*[@id="content"]/div/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span'
    # 第一个航线项目编辑按钮
    fieldinvoice_edit_route_button1 = '//*[@id="content"]/div/div[3]/div[3]/div[1]/div[2]/div[2]/span/div[1]/div/div/div[1]/div/div[1]/i'
    # 第二个航线项目编辑按钮
    fieldinvoice_edit_route_button2 = '//*[@id="content"]/div/div[3]/div[3]/div[1]/div[2]/div[2]/span/div[2]/div/div/div[1]/div/div[1]/i'

    # 费用栏位(一组元素)
    fieldinvoice_edit_route_price_lists = '//*[@id="content"]/div/div[3]/div[3]/div[1]/div[2]/div[2]/span/div[1]/div/div/div[3]/div/div[3]/div[1]/div[2]/table/tr[3]/td'

    # 乘客机票号栏位
    fieldinvoice_edit_passengerNumber = '//*[@id="content"]/div/div[3]/div[3]/div[1]/div[2]/div[2]/span/div[1]/div/div/div[3]/div/div[1]/div/div/div/div/div[1]/div[3]'
    fieldinvoice_edit_passengerNumber2 = '//*[@id="content"]/div/div[3]/div[3]/div[1]/div[2]/div[2]/span/div[2]/div/div/div[3]/div/div[1]/div/div/div/div/div[1]/div[3]'

    # 全部添加
    fieldinvoice_edit_passengerNumber_addAll = '//*[@id="content"]/div/div[3]/div[3]/div[1]/div[2]/div[2]/span/div[1]/div/div/div[3]/div/div[3]/div[3]/div[2]/div[1]/button[1]'
    fieldinvoice_edit_passengerNumber_addAll2 = '//*[@id="content"]/div/div[3]/div[3]/div[1]/div[2]/div[2]/span/div[2]/div/div/div[3]/div/div[3]/div[3]/div[2]/div[1]/button[1]'
    # 机票号栏位(一组元素)
    fieldinvoice_edit_routeNumber_lists = '//*[@id="content"]/div/div[3]/div[3]/div[1]/div[2]/div[2]/span/div[1]/div/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[2]'
    fieldinvoice_edit_routeNumber_lists2 = '//*[@id="content"]/div/div[3]/div[3]/div[1]/div[2]/div[2]/span/div[2]/div/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[2]'
    # 储存按钮
    fieldinvoice_edit_route_save = '//*[@id="content"]/div/div[3]/div[3]/div[1]/div[2]/div[2]/span/div[1]/div/div/div[1]/div[1]/span[2]'
    fieldinvoice_edit_route_save2 = '//*[@id="content"]/div/div[3]/div[3]/div[1]/div[2]/div[2]/span/div[2]/div/div/div[1]/div[1]/span[2]'

    # 编辑酒店项目
    # 选择酒店栏位
    fieldXO_edit_hotel_button = '//*[@id="content"]/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/span'
    # 金额
    fieldXO_edit_hotel_price = '//*[@id="content"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/input'
    # 成本
    fieldXO_edit_hotel_cost = '//*[@id="content"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/input'
    # 数量
    fieldXO_edit_hotel_number = '//*[@id="content"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div[3]/div/div[2]/input'
    # 备注
    fieldXO_edit_hotel_remark = '//*[@id="content"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div[6]/textarea'

    # 获取航线熟料
    field_route_number = '//*[@id="content"]/div/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/sup/span/p[3]'

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
    fieldfinalcheck = ".ant-btn:nth-child(3)"

    # fieldfinalcheck = "//button[@type='button']"

    # 編輯
    fieldothercharge = ".ant-tabs-tab:nth-child(3)"
    fieldothercharge_invoice_edit = "/html/body/div[1]/div/div/div[2]/div/div[3]/div[3]/div[3]/div[2]/div[1]/div[2]/div/div[2]/input"
    fieldothercharge_xo_edit = "/html/body/div[1]/div/div/div[2]/div/div[3]/div[3]/div[3]/div[2]/div[1]/div[3]/div/div[2]/input"
    fieldothercharge_unit_edit = "/html/body/div[1]/div/div/div[2]/div/div[3]/div[3]/div[3]/div[2]/div[1]/div[5]/input"
    fieldothercharge_remark_edit = "/html/body/div[1]/div/div/div[2]/div/div[3]/div[3]/div[3]/div[2]/div[1]/div[7]/textarea"

    # def group13579(self, textgroupname, textgroupcontacts, textgroupdescription, textgroupremark):
    #     # 創建團
    #     self.xpathclick(self.fieldgroup)
    #     self.cssclick(self.fieldgroupadd)
    #     self.cssclick(self.fieldgroupcontent1)
    #     self.cssclick(self.fieldgroupdefault1)
    #     self.cssclick(self.fieldgroupitem3)
    #     self.cssclick(self.fieldgroupitem5)
    #     self.cssclick(self.fieldgroupitem7)
    #     self.cssclick(self.fieldgroupitem9)
    #     time.sleep(2)
    #     self.cssclick(self.fieldgroupcontent1)
    #     time.sleep(0.5)
    #     self.csssend(self.fieldgroupname1, textgroupname)
    #     self.csssend(self.fieldgroupcontacts1, textgroupcontacts)
    #     self.cssclick(self.fieldgroupautofare1)
    #     self.xpathperclip(self.fieldgroupdescription, textgroupdescription)
    #     self.xpathperclip(self.fieldgroupremark, textgroupremark)
    #     print("已成功创建一个团")
    #     print("添加完团后的金额显示", self.cssreturntext(self.fieldfinalamount))
    #
    # def group(self, textgroupname, textgroupcontacts, textgroupdescription, textgroupremark, textnumber):
    #     # 創建團
    #     self.xpathclick(self.fieldgroup)
    #     self.cssclick(self.fieldgroupadd)
    #     self.cssclick(self.fieldgroupcontent1)
    #     if(textnumber<=8):
    #         self.cssclick(self.fieldgroupdefault1)
    #     if(textnumber>9):
    #         self.cssclick(self.fieldgroupdefault1)
    #         self.cssclick(self.fieldgroupitem3)
    #         self.cssclick(self.fieldgroupitem5)
    #         self.cssclick(self.fieldgroupitem7)
    #         self.cssclick(self.fieldgroupitem9)
    #     time.sleep(0.5)
    #     self.cssclick(self.fieldgroupcontent1)
    #     self.csssend(self.fieldgroupname1, textgroupname)
    #     self.csssend(self.fieldgroupcontacts1, textgroupcontacts)
    #     self.cssclick(self.fieldgroupautofare1)
    #     self.xpathperclip(self.fieldgroupdescription, textgroupdescription)
    #     self.xpathperclip(self.fieldgroupremark, textgroupremark)
    #     print("已成功创建一个团")
    #     print("添加完团后的金额显示", self.cssreturntext(self.fieldfinalamount))

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
        logger.info("编辑成功！")
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

    # 發票編輯
    # 添加机票号
    def quotation_add_Ticket_number(self, subscript0, passenger0, subscript1,
                                    passenger1, subscript2, passenger2,
                                    subscript3, passenger3, subscript0_2, passenger0_2, subscript1_2, passenger1_2,
                                    subscript2_2, passenger2_2, subscript3_2, passenger3_2):

        Ticket_num = self.get_element_attribute(self.field_route_number, 'title')
        logger.info(f"拿到的值{Ticket_num}，类型{type(Ticket_num)}")
        Ticket_num = int(Ticket_num)
        logger.info(f"拿到的值{Ticket_num}，类型{type(Ticket_num)}")
        try:
            if Ticket_num == 2:
                # 选择航线项目编辑
                self.xpathclick(self.field_route_button)
                self.xpathclick(self.fieldinvoice_edit_route_button1)
                # 填写机票号
                self.xpathclick(self.fieldinvoice_edit_passengerNumber)
                self.xpathclick(self.fieldinvoice_edit_passengerNumber_addAll)
                self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists, subscript0, passenger0)
                self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists, subscript1, passenger1)
                self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists, subscript2, passenger2)
                self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists, subscript3, passenger3)
                self.xpathclick(self.fieldinvoice_edit_route_save)
                time.sleep(3)
                self.xpathclick(self.fieldinvoice_edit_route_button2)
                # 填写机票号
                self.xpathclick(self.fieldinvoice_edit_passengerNumber2)
                self.xpathclick(self.fieldinvoice_edit_passengerNumber_addAll2)
                self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists2, subscript0_2, passenger0_2)
                self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists2, subscript1_2, passenger1_2)
                self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists2, subscript2_2, passenger2_2)
                self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists2, subscript3_2, passenger3_2)
                self.xpathclick(self.fieldinvoice_edit_route_save2)
                time.sleep(3)
            else:
                logger.info(f"{type(Ticket_num)}")
            logger.info(f"此订单填写机票号成功")
            # logger.info(f"此订单有f{Ticket_num}个航线项目，填写机票号成功")
        except Exception as e:
            logger.error(f"填写机票号失败。f{e}")
            raise

    # 编辑航线项目
    def quotation_edit_route(self, subscript_0, textbasicfare_invoice, subscript_1, textbasicfare_xo, subscript_2,
                             texttickettax_invoice, subscript_3, texttickettax_xo, subscript0, passenger0, subscript1,
                             passenger1, subscript2, passenger2,
                             subscript3, passenger3, subscript4, passenger4):

        # 选择航线项目编辑
        self.xpathclick(self.field_route_button)
        self.xpathclick(self.fieldinvoice_edit_route_button1)
        self.xpathclick_list_text(self.fieldinvoice_edit_route_price_lists, subscript_0, textbasicfare_invoice)
        self.xpathclick_list_text(self.fieldinvoice_edit_route_price_lists, subscript_1, textbasicfare_xo)
        self.xpathclick_list_text(self.fieldinvoice_edit_route_price_lists, subscript_2, texttickettax_invoice)
        self.xpathclick_list_text(self.fieldinvoice_edit_route_price_lists, subscript_3, texttickettax_xo)
        # time.sleep(3)
        # 填写机票号
        self.xpathclick(self.fieldinvoice_edit_passengerNumber)
        self.xpathclick(self.fieldinvoice_edit_passengerNumber_addAll)
        self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists, subscript0, passenger0)
        self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists, subscript1, passenger1)
        self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists, subscript2, passenger2)
        self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists, subscript3, passenger3)
        self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists, subscript4, passenger4)
        self.xpathclick(self.fieldinvoice_edit_route_save)
        # time.sleep(60)

    # 编辑酒店项目
    def quotation_edit_hotel(self, texthotelfare_invoice, texthotelfare_xo, texthotelfare_num,
                             texthotelfare_remark):
        try:
            # 选择酒店栏位
            self.xpathclick(self.fieldXO_edit_hotel_button)
            # 编辑金额
            self.xpathsend(self.fieldXO_edit_hotel_price, texthotelfare_invoice)
            # 编辑成本
            self.xpathsend(self.fieldXO_edit_hotel_cost, texthotelfare_xo)
            # 编辑数量
            self.xpathsend(self.fieldXO_edit_hotel_number, texthotelfare_num)
            # 编辑备注
            self.xpathsend(self.fieldXO_edit_hotel_remark, texthotelfare_remark)
            logger.info("編輯酒店成功！")
        except Exception as e:
            logger.error(f"編輯酒店失敗！{e}")
            raise

    # 编辑其他费用
    def riseinvoice_othercharge(self, textothercharge_invoice, textothercharge_xo, textothercharge_unit,
                                textothercharge_remark):
        # 选择其他費用欄位
        self.cssclick(self.fieldothercharge)

        self.xpathsend(self.fieldothercharge_invoice_edit, textothercharge_invoice)
        self.xpathsend(self.fieldothercharge_xo_edit, textothercharge_xo)
        self.xpathsend(self.fieldothercharge_unit_edit, textothercharge_unit)
        self.xpathperclip(self.fieldothercharge_remark_edit, textothercharge_remark)

    # def othercharge(self, textothercharge_invoice, textothercharge_xo, textothercharge_unit,
    #                 textothercharge_remark):
    #     # 選擇其他費用
    #     # @allure.title('添加其他費用')
    #
    #     # logger.info("創建其他費用")
    #
    #     self.xpathsend(self.fieldothercharge_invoice, textothercharge_invoice)
    #     self.xpathsend(self.fieldothercharge_xo, textothercharge_xo)
    #     self.xpathsend(self.fieldothercharge_unit, textothercharge_unit)
    #     self.xpathperclip(self.fieldothercharge_remark, textothercharge_remark)
    #     self.cssclick(self.fieldotherchargeadd)
    #     print("已成功添加一个其他费用")

    # # 选择航线项目编辑
    # self.xpathclick(self.field_route_button)
    # self.xpathclick(self.fieldinvoice_edit_route_button1)
    # # 填写机票号
    # self.xpathclick(self.fieldinvoice_edit_passengerNumber)
    # self.xpathclick(self.fieldinvoice_edit_passengerNumber_addAll)
    # self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists, subscript0, passenger0)
    # self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists, subscript1, passenger1)
    # self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists, subscript2, passenger2)
    # self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists, subscript3, passenger3)
    # self.xpathclick(self.fieldinvoice_edit_route_save)
    # time.sleep(3)
    # self.xpathclick(self.fieldinvoice_edit_route_button2)
    # # 填写机票号
    # self.xpathclick(self.fieldinvoice_edit_passengerNumber2)
    # self.xpathclick(self.fieldinvoice_edit_passengerNumber_addAll2)
    # self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists2, subscript0_2, passenger0_2)
    # self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists2, subscript1_2, passenger1_2)
    # self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists2, subscript2_2, passenger2_2)
    # self.xpathclick_list_text(self.fieldinvoice_edit_routeNumber_lists2, subscript3_2, passenger3_2)
    # self.xpathclick(self.fieldinvoice_edit_route_save2)
    # time.sleep(3)
