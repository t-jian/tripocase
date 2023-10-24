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
class AddenquiryPage(BasePage):
    # 元素集
    # 抬头
    # 发票
    createinvoce = ".btn-bar-line-2 > .ant-btn:nth-child(3)"
    fieldinvoice_popcustomer = ".select-customer .PopoverSearchTable > .ant-input"  # 弹出客户
    # 报价单
    createquotation = ".btn-bar:nth-child(3) > .ant-btn:nth-child(3)"
    fieldquotation_popustomer = ".quotation-detail .ant-input"
    # xo
    createxo = ".btn-bar-line-2 > .ant-btn:nth-child(2)"
    fieldxo_popustomer = ".value-el"
    fieldxo_customer = ".ant-table-row:nth-child(1) > .ant-table-column-has-actions:nth-child(2)"
    fieldxo_next = ".ant-btn:nth-child(1)"
    fieldxo_popsupplier = ".supplier-box .PopoverSearchTable > .ant-input"
    fieldxo_supplier = ".ant-table-row:nth-child(1) > .ant-table-column-has-actions:nth-child(2) > .line-clamp"

    fieldxo_popconsultant = "#infoForm_FollowID > div > div"
    fieldxo_consultant = "li.ant-select-dropdown-menu-item:nth-child(1)"
    # 公共頁頭部分

    defaultcustomer = ".ant-table-row:nth-child(1) > .ant-table-column-has-actions:nth-child(2)"  # 选择第一个客户
    fieldphone = "#infoForm_Mobile"  # 电话
    fielddiscount = ".ant-input-number-input-wrap > #infoForm_Discount"  # 折扣
    fieldpaymentmethod = "#infoForm_PaymentType > div > div"
    fieldpaymentmethoddefault = "//li[contains(.,\'Bank in')]"

    # api机票
    fieldtrip = "#from\\[0\\] .ant-select-selection__placeholder"  # 点击去程
    searchtrip = "#from\\[0\\] .ant-select-search__field"
    defaulttrip = "//li[contains(.,\'台北所有機場\')]"
    fieldreturn = "#to\\[0\\] .ant-select-selection__placeholder"  # 点击回程
    searchreturn = "#to\\[0\\] .ant-select-search__field"
    defaultreturn = "//li[contains(.,\'東京所有機場\')]"
    fieldcalendar = "#fromCityDate\\[0\\] .ant-calendar-picker-input"  # 点击日历选项
    fieldcalendarmonth = ".ant-calendar-next-month-btn"  # 点击下一个月
    fieldcalendarday = "tr:nth-child(5) > .ant-calendar-cell:nth-child(3) > .ant-calendar-date"
    # fieldroute_search = ".ant-form-item-children > .ant-btn"
    fieldroute_search = ".ant-form-item-children > .ant-btn:nth-child(1)"
    defaultroute1 = ".item-v1:nth-child(1) .ant-btn"  # 选择自动搜索机票的第一个行程
    defaultroute2 = ".item-v1:nth-child(2) .ant-btn"  # 选择自动搜索机票的第二个行程
    # 手输机票
    fieldhandticket = ".tickets > .ant-tabs > .ant-tabs-bar .ant-tabs-tab:nth-child(2)"
    fieldfetchpnr = ".ant-col:nth-child(2) > .ant-btn:nth-child(1)"
    fieldcontentpnr = ".body-content-1 > .ant-input"
    fieldnextpnr1 = ".ture-page-button > .ant-btn:nth-child(2)"
    fieldtickettype1 = "div.airline-ticket-item:nth-child(3) > div:nth-child(2) > div:nth-child(1) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)"
    # fieldhandapiticket = "#content > div > div.manual-control-add-route > div > div.body > div > div.ant-radio-group.ant-radio-group-outline.ant-radio-group-default > label:nth-child(2) > span.ant-radio > input"
    fieldhandapiticket = "//span[contains(.,' BookingAccount')]"
    fieldnextpnr2 = ".action-button > button:nth-child(2)"
    fieldnextapipnr2 = "#content > div > div.manual-control-add-route > div > div.footer.has-next-step > div.action-button > button:nth-child(3)"
    # fieldtickettype1 = "#content > div > div.tickets > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.custom-flight.other-fee > div > div.custom-flight-table-contain.form > div:nth-child(3) > div:nth-child(1) > div.ant-checkbox-group > label:nth-child(1) > span.ant-checkbox > input"  # x选择第一个机票类型

    fieldbasicfare_invoice = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[2]/input"
    fieldbasicfare_xo = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[6]/div[2]/div[2]/input"
    fieldtickettax_invoice = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[4]/div[2]/div[2]/input"
    fieldtickettax_xo = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[9]/div[2]/div[2]/input"
    fieldhandticketsubmit = ".custom-flight-btn > .ant-btn"

    # 酒店项目
    # fieldhotel = "css=.ant-tabs-tab:nth-child(3)"
    # fieldhotel = "//div[contains(.,\'酒店\')]"
    fieldhotel = ".tickets > .ant-tabs > .ant-tabs-bar .ant-tabs-tab:nth-child(3)"
    fieldhotelcontent = ".ant-select-selection--multiple > .ant-select-selection__rendered"
    fieldhotel_search = ".ant-select-search:nth-child(1) .ant-select-search__field"
    fieldhotelcity = ".add-hotel #City"
    fieldhotelcountry = ".add-hotel #Country"
    fieldhotelcalendar = "#CheckInDate .ant-calendar-picker-input"  # 酒店日历
    fieldhotelroomtype = "//div[@id=\'RoomType\']/div/div"
    fieldhotelpropertytype = ".add-hotel #TotherType"
    fieldhotelroomplan = ".add-hotel #RoomPlan"
    fieldhotelspecial = ".add-hotel #Special"
    fieldhoteltype1 = "#IfPostpone"

    fieldhotelroomtypedefault = ".ant-select-dropdown-menu-item-active"
    fieldhotelfare_invoice = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[3]/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/input"
    fieldhotelfare_xo = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[3]/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/input"
    fieldhotelfare_unit = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[3]/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div/div[5]/input[2]"
    fieldhotelfare_remark = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[3]/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div/div[6]/textarea"
    fieldhoteladd = ".add-hotel > .custom-fee-bar > .ant-btn"

    # 其他费用
    fieldothercharge = ".ant-tabs-tab:nth-child(4)"
    fieldotherchargecontent = "/html/body/div[1]/div/div/div[2]/div/div[3]/div/div[3]/div[4]/div[2]/div[3]/div[1]/div/div"  # 通用其他费用栏位
    # fieldotherchargecontent1 = ".select-has-search-icon .ant-select-selection__placeholder"  #第一次点击其他费用栏位
    fieldotherchargeitem1 = "//li[contains(.,\'機票服務:機票服務\')]"
    # fieldotherchargeitem1 = "/html/body/div[2]/div/div/div/ul/li[1]"
    fieldotherchargeitem2 = "//li[contains(.,\'機票升級:機票升級\')]"
    # fieldotherchargeitem2 = "/html/body/div[2]/div/div/div/ul/li[2]"

    fieldothercharge_invoice = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[4]/div[2]/div[3]/div[2]/div[2]/input"
    fieldothercharge_xo = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[4]/div[2]/div[3]/div[3]/div[2]/input"
    fieldothercharge_unit = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[4]/div[2]/div[3]/input"
    fieldothercharge_remark = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[4]/div[2]/div[3]/textarea[2]"

    fieldotherchargeadd = ".other-fee > .custom-fee-bar > .ant-btn"

    # 一日游
    fielddaytour = ".ant-tabs-tab:nth-child(5)"
    fielddaytourcontent = ".ant-row-flex .ant-row .PopoverSearchTable > .ant-input"
    fielddaytouritem1 = ".ant-table-row:nth-child(1) > .ant-table-column-has-actions:nth-child(2)"
    fielddaytourcalendar = "#StartDate .ant-calendar-picker-input"
    # StartDate .ant-calendar-picker-input
    fielddaytour_invoice = "/html/body/div[1]/div/div/div[2]/div/div[3]/div/div[3]/div[5]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/input"
    fielddaytour_xo = "/html/body/div[1]/div/div/div[2]/div/div[3]/div/div[3]/div[5]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[3]/div/div[2]/input"
    fielddaytour_unit = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[5]/div[2]/div/div/div/div[2]/div/div/div[5]/input[2]"
    fielddaytour_remark = "//textarea[@id=\'Remarks\']"
    fielddaytour_itemremark = "//div[@id='content']/div/div[3]/div/div[3]/div[5]/div[2]/div/div/div/div[2]/div/div/div[6]/textarea"

    fielddaytouradd = ".AddDaytour .ant-btn"
    fielddaytouritem2 = ".ant-table-row:nth-child(2) > .ant-table-column-has-actions:nth-child(2)"

    # 发票下一页
    shoppingcart = ".icon-container use"
    nextpage = ".create-button"

    # 最后提交
    fieldfinalamount = ".total-amount:nth-child(2)"
    # fieldfinalcheck = ".confirm-bar > .ant-btn ant-btn-primary ant-btn-lg"
    # fieldfinalcheck = ".ant-btn:nth-child(2)"
    fieldfinalcheck = "#content > div > div.bottom-bar > div > button"

    # fieldfinalcheck = "//button[@type='button']"

    def risebooking(self):
      
        # 选择客户
        self.cssclick(self.fieldxo_popustomer)
        self.cssclick(self.fieldxo_customer)
        self.cssclick(self.fieldxo_next)
        print("booking页头已填完")

