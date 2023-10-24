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
import allure
import logging

logger = logging.getLogger(__name__)

# 百度搜索page
# 創建發票/XO/報價單第一個頁面
logger = logging.getLogger(__name__)


class QuotationPage(BasePage):
    # 元素集
    # 抬头
    # 发票
    createinvoce = ".btn-bar-line-2 > .ant-btn:nth-child(3)"
    fieldinvoice_popcustomer = ".select-customer .PopoverSearchTable > .ant-input"  # 弹出客户

    # 弹出客户欄輸入客戶姓名
    fieldinvoice_popcustomer_list = '//*[@id="content"]/div/div[2]/div/div[3]/div[1]/div[2]/form/div[1]/div[1]/div[1]/div/div[2]/div/span/div/div/div[2]/div[1]/div[1]/span/span/input'
    # 搜索客戶按鈕
    fieldinvoice_popcustomer_select_button = '//*[@id="content"]/div/div[2]/div/div[3]/div[1]/div[2]/form/div[1]/div[1]/div[1]/div/div[2]/div/span/div/div/div[2]/div[1]/div[1]/span/span/span[2]/span/i'

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
    defaultcustomer2 = ".ant-table-row:nth-child(2) > .ant-table-column-has-actions:nth-child(2)"  # 第二個客戶
    fieldphone = "#infoForm_Mobile"  # 电话
    fielddiscount = ".ant-input-number-input-wrap > #infoForm_Discount"  # 折扣
    fieldpaymentmethod = "#infoForm_PaymentType > div > div"
    fieldpaymentmethoddefault = "//li[contains(.,\'Bank in')]"
    fieldpaymentmethoddefault_tc0141 = '//*[@id="ae4da87e-cd7a-4a7e-da69-cfe3f413d5a4"]/ul/li[2]'


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

    # 输入机场编号
    fieldhand_Input_Route = '//*[@id="content"]/div/div[3]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/input'
    # 确认航线
    fieldhand_Route_Confirm = '//*[@id="content"]/div/div[3]/div/div[3]/div[2]/div[2]/div/div[1]/div[3]/button'

    # = '//*[@id="content"]/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div/table/tbody/tr/td[5]/input'
    # = '//*[@id="content"]/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div/table/tbody/tr/td[6]/input'
    # = '//*[@id="content"]/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div/table/tbody/tr/td[7]/input'



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

    fieldbasicfare_invoice = "//*[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div[1]/div[1]/div[2]/div/div[2]/input"
    fieldbasicfare_xo = "//*[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div[1]/div[6]/div[2]/div/div[2]/input"
    fieldtickettax_invoice = "//*[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div[1]/div[4]/div[2]/div/div[2]/input"
    fieldtickettax_xo = "//*[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div[1]/div[9]/div[2]/div/div[2]/input"
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
    fieldhotelfare_invoice = "//*[@id='content']/div/div[3]/div/div[3]/div[3]/div[2]/div[1]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div[2]/input"

    fieldhotelfare_xo = "/html/body/div[1]/div/div/div[2]/div/div[3]/div/div[3]/div[3]/div[2]/div[1]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div/div[3]/div/div/div[2]/input"
    fieldhotelfare_unit = "//*[@id='content']/div/div[3]/div/div[3]/div[3]/div[2]/div[1]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div/div[5]/input[2]"
    fieldhotelfare_remark = "//*[@id='content']/div/div[3]/div/div[3]/div[3]/div[2]/div[1]/div[3]/div[1]/div[2]/div/div[2]/div[1]/div/div[6]/textarea"
    fieldhoteladd = ".add-hotel > .custom-fee-bar > .ant-btn"

    # 其他费用
    fieldothercharge = ".ant-tabs-tab:nth-child(4)"
    fieldotherchargecontent = "/html/body/div[1]/div/div/div[2]/div/div[3]/div/div[3]/div[4]/div[2]/div[3]/div[1]/div/div"  # 通用其他费用栏位
    # fieldotherchargecontent1 = ".select-has-search-icon .ant-select-selection__placeholder"  #第一次点击其他费用栏位
    # fieldotherchargeitem1 = "//li[contains(.,\'ADMIN FEE\')]"
    fieldotherchargeitem1 = "//li[contains(.,\'AAMSIC\')]"

    # 其他費用Jayce
    # 服務項目搜索欄位
    field_other_search = '//*[@id="content"]/div/div[3]/div/div[3]/div[4]/div[2]/div[1]/div/input'
    # 選擇其他費用項目(選擇第9個.1-10)
    field_other_project = '//*[@id="content"]/div/div[3]/div/div[3]/div[4]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr[9]'
    # 項目列表(定位一組元素可根據下表取值)
    field_other_project_list = '//*[@id="content"]/div/div[3]/div/div[3]/div[4]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr'

    # fieldotherchargeitem1 = "/html/body/div[2]/div/div/div/ul/li[1]"
    fieldotherchargeitem2 = "//li[contains(.,\'AAMSIC1\')]"
    # fieldotherchargeitem2 = "//li[contains(.,\'保險費用:保險費用\')]"
    # fieldotherchargeitem2 = "/html/body/div[2]/div/div/div/ul/li[2]"

    fieldothercharge_invoice = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[4]/div[2]/div[3]/div[2]/div[2]/input"
    fieldothercharge_xo = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[4]/div[2]/div[3]/div[3]/div[2]/input"
    fieldothercharge_unit = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[4]/div[2]/div[3]/input"
    fieldothercharge_remark = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[4]/div[2]/div[3]/textarea[2]"

    fieldotherchargeadd = ".other-fee > .custom-fee-bar > .ant-btn"

    # 一日游
    fielddaytour = ".ant-tabs-tab:nth-child(5)"
    fielddaytourcontent = ".ant-row-flex .ant-row .PopoverSearchTable > .ant-input"

    # 所有一日游项目
    fielddaytour_all = '//*[@id="content"]/div/div[3]/div/div[3]/div[5]/div[2]/div/form/div[1]/div/div/div[2]/div/span/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr'

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
    # 獲取創建總價格
    create_all_price = (By.XPATH, '//*[@id="content"]/div/div[4]/div/div[3]/div/div[2]/span')
    # 獲取編輯頁面總價格
    edit_all_price = (By.XPATH, '//*[@id="content"]/div/div[4]/h2[2]/span')

    # 最后提交
    fieldfinalamount = ".total-amount:nth-child(2)"
    # fieldfinalcheck = ".confirm-bar > .ant-btn ant-btn-primary ant-btn-lg"
    # fieldfinalcheck = ".ant-btn:nth-child(2)"
    fieldfinalcheck = "#content > div > div.bottom-bar > div > button"

    # fieldfinalcheck = "//button[@type='button']"

    # 创建发票客户篩選客戶
    def create_invoice(self, textpassager_name, textdiscount):  # , num4, text4, text5):
        # 选择客户
        self.cssclick(self.fieldinvoice_popcustomer)
        # 搜索客戶
        self.xpathsend(self.fieldinvoice_popcustomer_list, textpassager_name)
        self.xpathclick(self.fieldinvoice_popcustomer_select_button)
        # 選擇搜索的客戶
        # self.cssclick(self.defaultcustomer)
        self.cssclick(self.defaultcustomer)
        # 輸入折扣
        self.csssend(self.fielddiscount, textdiscount)
        # 選擇付款方式
        self.cssclick(self.fieldpaymentmethod)
        self.xpathclick(self.fieldpaymentmethoddefault)
        # self.xpathclick(self.fieldpaymentmethoddefault_tc0141)
        logger.info("发票页头已填完")

    # 创建发票客户誤默認第一個
    def riseinvoice(self, textdiscount):
        # 选择客户
        try:
            self.cssclick(self.fieldinvoice_popcustomer)
            self.cssclick(self.defaultcustomer)
            # 16 | runScript | window.scrollTo(0,405) |
            self.cssclick(self.fieldxo_popconsultant)
            self.cssclick(self.fieldxo_consultant)
            self.csssend(self.fielddiscount, textdiscount)
            self.cssclick(self.fieldpaymentmethod)
            self.xpathclick(self.fieldpaymentmethoddefault)
            logger.info("選擇客戶成功！")
        except Exception as e:
            logger.error(f"選擇客戶失敗.{e}")
            raise

    # 创建报价单筛选客户
    def create_quotation(self, textpassager_name, textdiscount):
        # 选择客户
        self.cssclick(self.fieldquotation_popustomer)
        # 搜索客戶
        self.xpathsend(self.fieldinvoice_popcustomer_list, textpassager_name)
        self.xpathclick(self.fieldinvoice_popcustomer_select_button)
        # 選擇搜索的客戶
        # self.cssclick(self.defaultcustomer)
        self.cssclick(self.defaultcustomer)
        # 輸入折扣
        self.csssend(self.fielddiscount, textdiscount)
        # self.xpathclick(self.fieldpaymentmethoddefault_tc0141)
        logger.info("报价单页头已填完")

    # 創建報價單客户默认选择第一个
    def risequotation(self, textdiscount):
        # 选择客户
        self.cssclick(self.fieldquotation_popustomer)
        self.cssclick(self.defaultcustomer)
        # 16 | runScript | window.scrollTo(0,405) |
        self.cssclick(self.fieldxo_popconsultant)
        self.cssclick(self.fieldxo_consultant)
        self.csssend(self.fielddiscount, textdiscount)
        # self.cssclick(self.fieldpaymentmethod)
        # self.xpathclick(self.fieldpaymentmethoddefault)

    # 创建XO抬头
    def create_XO(self, testsupplier_name, textdiscount):
        # 选择客户
        self.cssclick(self.fieldxo_popsupplier)
        # 搜索客戶
        self.xpathsend(self.fieldinvoice_popcustomer_list, testsupplier_name)
        self.xpathclick(self.fieldinvoice_popcustomer_select_button)
        # 選擇搜索的客戶
        self.cssclick(self.defaultcustomer)
        # 选择旅游顾问（默认第一个）
        self.cssclick(self.fieldxo_popconsultant)
        self.cssclick(self.fieldxo_consultant)
        # 輸入折扣
        self.csssend(self.fielddiscount, textdiscount)
        # 選擇付款方式
        self.cssclick(self.fieldpaymentmethod)
        self.xpathclick(self.fieldpaymentmethoddefault)
        logger.info("XO页头已填完")

    # xo抬头部分
    def risexo(self, textdiscount):
        # 选择客户
        self.cssclick(self.fieldxo_popsupplier)
        self.cssclick(self.fieldxo_supplier)
        # 16 | runScript | window.scrollTo(0,405) |
        # 选择旅游顾问（默认第一个）
        self.cssclick(self.fieldxo_popconsultant)
        self.cssclick(self.fieldxo_consultant)
        # 输入折扣
        self.csssend(self.fielddiscount, textdiscount)
        # 选择付款方式
        self.cssclick(self.fieldpaymentmethod)
        self.xpathclick(self.fieldpaymentmethoddefault)

        print("xo页头已填完")

    def apiticket(self, texttrip, textreturn):
        self.cssclick(self.fieldtrip)
        time.sleep(1)
        self.csssend(self.searchtrip, texttrip)
        self.xpathclick(self.defaulttrip)
        self.cssclick(self.fieldreturn)
        self.csssend(self.searchreturn, textreturn)
        self.xpathclick(self.defaultreturn)
        self.cssclick(self.fieldcalendar)
        self.cssclick(self.fieldcalendarmonth)
        self.driver.find_element(By.CSS_SELECTOR, self.fieldcalendarday).click()
        self.driver.find_element(By.CSS_SELECTOR, self.fieldroute_search).click()
        self.cssclick(self.defaultroute1)

        # 32 | click | css=.item-v1:nth-child(2) .ant-btn |
        self.driver.find_element(By.CSS_SELECTOR, self.defaultroute2).click()
        print("已选完俩个api搜索机票行程")

    def handticket(self, textcontentpnr, textbasicfare_invoice, textbasicfare_xo, texttickettax_invoice,
                   texttickettax_xo):
        try:
            # 選擇手動機票項目
            self.cssclick(self.fieldhandticket)
            self.cssclick(self.fieldfetchpnr)
            self.cssclick(self.fieldcontentpnr)
            self.cssperclip(self.fieldcontentpnr, textcontentpnr)
            self.cssclick(self.fieldnextpnr1)
            # self.cssclick(self.fieldtickettype1)
            self.cssclick(self.fieldnextpnr2)
            self.xpathsend(self.fieldbasicfare_invoice, textbasicfare_invoice)
            self.xpathsend(self.fieldbasicfare_xo, textbasicfare_xo)
            self.xpathsend(self.fieldtickettax_invoice, texttickettax_invoice)
            self.xpathsend(self.fieldtickettax_xo, texttickettax_xo)
            self.cssclick(self.fieldhandticketsubmit)
            logger.info("手動創建航線成功！")
        except Exception as e:
            logger.error(f"手動創建航線失敗！{e}")
            raise

    # 创建手动输入航线项目
    def create_PNR_route(self, route, airline_code1, flight_number, airline_code2, ticket_price, XO_price, tax_price,
                          XO_tax_price):
        self.cssclick(self.fieldhandticket)

    def handapiticket(self, textcontentapipnr, textbasicfare_invoice, textbasicfare_xo, texttickettax_invoice,
                      texttickettax_xo):
        # 選擇手動機票項目
        self.cssclick(self.fieldhandticket)
        self.cssclick(self.fieldfetchpnr)
        self.xpathclick(self.fieldhandapiticket)
        self.cssclick(self.fieldcontentpnr)
        self.cssperclip(self.fieldcontentpnr, textcontentapipnr)
        # time.sleep(5)
        self.cssclick(self.fieldnextpnr1)
        # self.cssclick(self.fieldtickettype1)
        self.cssclick(self.fieldnextapipnr2)
        self.xpathsend(self.fieldbasicfare_invoice, textbasicfare_invoice)
        self.xpathsend(self.fieldbasicfare_xo, textbasicfare_xo)
        self.xpathsend(self.fieldtickettax_invoice, texttickettax_invoice)
        self.xpathsend(self.fieldtickettax_xo, texttickettax_xo)
        self.cssclick(self.fieldhandticketsubmit)
        print("已成功添加第一个手入api机票")

    def handhotel(self, texthotel_search, texthotelcity, texthotelcountry, texthotelpropertytype, texthotelroomplan,
                  texthotelspecial, texthotelfare_invoice, texthotelfare_xo, texthotelfare_unit, texthotelfare_remark):
        try:
            # 酒店项目
            self.cssclick(self.fieldhotel)
            self.cssclick(self.fieldhotelcontent)
            self.cssclick(self.fieldhotelcontent)
            self.csssend(self.fieldhotel_search, texthotel_search)
            self.csssend(self.fieldhotelcity, texthotelcity)
            self.csssend(self.fieldhotelcountry, texthotelcountry)
            self.csssend(self.fieldhotelpropertytype, texthotelpropertytype)
            self.csssend(self.fieldhotelroomplan, texthotelroomplan)
            self.csssend(self.fieldhotelspecial, texthotelspecial)
            self.cssclick(self.fieldhoteltype1)
            self.cssclick(self.fieldhotelcalendar)
            self.cssclick(self.fieldcalendarmonth)
            self.cssclick(self.fieldcalendarday)
            self.xpathclick(self.fieldhotelroomtype)
            self.cssclick(self.fieldhotelroomtypedefault)
            self.xpathsend(self.fieldhotelfare_invoice, texthotelfare_invoice)
            self.xpathsend(self.fieldhotelfare_xo, texthotelfare_xo)
            self.xpathsend(self.fieldhotelfare_unit, texthotelfare_unit)
            self.xpathperclip(self.fieldhotelfare_remark, texthotelfare_remark)
            self.cssclick(self.fieldhoteladd)
            logger.info("添加一個酒店項目成功！")
        except Exception as e:
            logger.error(f"添加酒店項目失敗！{e}")
            raise

    # 创建其他费用项目(Jayce)
    def create_other(self, subscript, textothercharge_invoice, textothercharge_xo, textothercharge_unit,
                     textothercharge_remark):
        try:
            # 選擇其他費用欄位
            self.cssclick(self.fieldothercharge)
            # 點擊服務項目搜索欄位
            self.xpathclick(self.field_other_search)
            # 定位一組元素取下标為subscript值
            # logger.info(f"下表为{subscript}----{self.xpathclick_list(self.field_other_project_list, subscript)}")
            self.xpathclick_list1(self.field_other_project_list, subscript)
            # # 選擇其他費用項目
            # self.xpathclick(self.field_other_project)
            # 輸入金額
            self.xpathsend(self.fieldothercharge_invoice, textothercharge_invoice)
            # 輸入成本
            self.xpathsend(self.fieldothercharge_xo, textothercharge_xo)
            # 輸入單位
            self.xpathsend(self.fieldothercharge_unit, textothercharge_unit)
            # 輸入備註
            self.xpathperclip(self.fieldothercharge_remark, textothercharge_remark)
            # 点击确认
            self.cssclick(self.fieldotherchargeadd)
            logger.info("創建一個其他費用項目成功")
        except Exception as e:
            logger.error(f"創建其他費用項目失敗！{e}")
            raise

    # @allure.title('測試')
    def othercharge(self, textothercharge_invoice, textothercharge_xo, textothercharge_unit, textothercharge_remark):
        # 選擇其他費用
        # @allure.title('添加其他費用')
        # logger.info("創建其他費用")
        self.cssclick(self.fieldothercharge)
        time.sleep(0.5)
        self.xpathclick(self.fieldotherchargecontent)
        time.sleep(0.5)
        self.xpathclick(self.fieldotherchargeitem1)
        time.sleep(0.5)
        self.xpathsend(self.fieldothercharge_invoice, textothercharge_invoice)
        self.xpathsend(self.fieldothercharge_xo, textothercharge_xo)
        self.xpathsend(self.fieldothercharge_unit, textothercharge_unit)
        self.xpathperclip(self.fieldothercharge_remark, textothercharge_remark)
        self.cssclick(self.fieldotherchargeadd)
        print("已成功添加一个其他费用")

    # 创建一日游项目(按下标选择)
    def create_daytour(self, subscript, textdaytour_invoice, textdaytour_xo, textdaytour_unit, textdaytour_remark,
                       textdaytour_itemremark):
        try:
            # 选择一日游栏位
            self.cssclick(self.fielddaytour)
            # 选择一日游项目
            self.cssclick(self.fielddaytourcontent)
            # 选择下标为subscript的一日游项目
            self.xpathclick_list1(self.fielddaytour_all, subscript)

            self.cssclick(self.fielddaytourcalendar)
            self.cssclick(self.fieldcalendarmonth)
            self.cssclick(self.fieldcalendarday)
            self.xpathsend(self.fielddaytour_invoice, textdaytour_invoice)
            self.xpathsend(self.fielddaytour_xo, textdaytour_xo)
            self.xpathsend(self.fielddaytour_unit, textdaytour_unit)
            self.xpathperclip(self.fielddaytour_remark, textdaytour_remark)
            self.xpathperclip(self.fielddaytour_itemremark, textdaytour_itemremark)
            self.cssclick(self.fielddaytouradd)
            logger.info("創建一個一日遊項目成功！")
        except Exception as e:
            logger.error(f"創建一日遊項目失敗！{e}")
            raise

    # 创建一日游项目(默认第一个)
    def daytour(self, textdaytour_invoice, textdaytour_xo, textdaytour_unit, textdaytour_remark,
                textdaytour_itemremark):
        try:
            self.cssclick(self.fielddaytour)
            self.cssclick(self.fielddaytourcontent)
            self.cssclick(self.fielddaytouritem1)
            self.cssclick(self.fielddaytourcalendar)
            self.cssclick(self.fieldcalendarmonth)
            self.cssclick(self.fieldcalendarday)
            self.xpathsend(self.fielddaytour_invoice, textdaytour_invoice)
            self.xpathsend(self.fielddaytour_xo, textdaytour_xo)
            self.xpathsend(self.fielddaytour_unit, textdaytour_unit)
            self.xpathperclip(self.fielddaytour_remark, textdaytour_remark)
            self.xpathperclip(self.fielddaytour_itemremark, textdaytour_itemremark)
            self.cssclick(self.fielddaytouradd)
            logger.info("創建一個一日遊項目成功！")
        except Exception as e:
            logger.error(f"創建一日遊項目失敗！{e}")
            raise

    def nextquotation(self):
        global all_price1
        self.cssclick(self.shoppingcart)
        all_price1 = self.get_element(self.create_all_price)
        # 切片
        all_price1 = all_price1[4:]
        self.cssclick(self.nextpage)
        time.sleep(5)
        all_price2 = self.get_element(self.edit_all_price)
        logger.info(f"創建頁面總價格為{all_price1},編輯頁面總價格為{all_price2}")
        time.sleep(5)
        try:
            assert all_price2 == all_price1
            logger.info("斷言通過,進入下一頁！")
        except Exception as e:
            logger.error(f"断言不通过{e}")
            raise

        # try:
        #     assert all_price2 == all_price1
        #     logger.info("斷言通過,進入下一頁！")
        # except AssertionError as e:
        #     logger.error(f"断言不通过{e}")
        #     sys.exit()
