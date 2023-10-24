__author__ = 'david'

import time
import unittest
import sys
import pytest
import os
import allure
import pytest

from selenium import webdriver
from Tripo.Tripo_Web.pages.LoginPage import LoginPage
from Tripo.Tripo_Web.pages.MakeInvoicePage import MakeInvoicePage
from Tripo.Tripo_Web.pages.PayOrderPage import PayOrderPage
from Tripo.Tripo_Web.pages.QuotationAddPage import QuotationAddPage
from Tripo.Tripo_Web.pages.QuotationEditPage import QuotationEditPage
from Tripo.Tripo_Web.pages.RefundApplicationPage import RefundApplicationPage
from Tripo.Tripo_Web.pages.RefundPage import RefundPage
from Tripo.Tripo_Web.pages.data import *
from Tripo.Tripo_Web.pages.LeadlisteningPage import LeadlisteningPage
from Tripo.Tripo_Web.pages.QuotationPage import QuotationPage

import logging

logger = logging.getLogger(__name__)


@allure.feature('創建發票\轉XO\發票付款\發票退款\發票退款申請流程')
class Test_Edit_Invoice:
    # @pytest.mark.parametrize("no,username,password,code,msg", read_xlsx("../datas/login.xlsx"))
    # @pytest.mark.parametrize("no,username,password,code,msg", read_xlsx("test_case", "\datas\login.xlsx"))
    @pytest.mark.parametrize("caseinfo",
                             read_testcase("test_case", "\datas\login.yaml"))
    @allure.title('登錄測試')
    def test_login(self, driver, caseinfo):
        logger.info("开始执行用例")
        allure.attach(driver.get_screenshot_as_png(), '开始执行用例')
        login1 = LoginPage(driver)
        driver.get(caseinfo["login"]["url"])
        login1.login(caseinfo["login"]["textaccount"], caseinfo["login"]["textpassword"],
                     caseinfo["login"]["textcompanycode"])
        allure.attach(driver.get_screenshot_as_png(), '用例后')

    @pytest.mark.parametrize("caseinfo",
                             read_testcase("test_case", "\datas\quotation_rise.yaml"))
    @allure.title('填寫發票抬頭')
    def test_createinvoice(self, driver, caseinfo):
        b = LeadlisteningPage(driver)
        b.createinvoice()
        c = QuotationPage(driver)
        # 默認選中第一個客戶
        # c.riseinvoice(caseinfo["textdiscount"])
        # 篩選客戶
        c.create_invoice(caseinfo["textuser_name"], caseinfo["textdiscount"])

    # @pytest.mark.parametrize("caseinfo1",
    #                          read_testcase(
    #                              "test_case", "\datas\quotation_apiticket.yaml"))
    # @pytest.mark.title('創建API接口航線')
    # def test_apiticket(self, driver, caseinfo1):
    #     e = QuotationPage(driver)
    #     e.apiticket(caseinfo1["texttrip"], caseinfo1["textreturn"])

    @pytest.mark.parametrize("caseinfo2",
                             read_testcase(
                                 "test_case", "\datas\quotation_handticket.yaml"))
    @allure.title('創建手動輸入機票')
    def test_handticket(self, driver, caseinfo2):
        f = QuotationPage(driver)
        f.handticket(caseinfo2["textcontentpnr"], caseinfo2["textbasicfare_invoice"], caseinfo2["textbasicfare_xo"],
                     caseinfo2["texttickettax_invoice"], caseinfo2["texttickettax_xo"])

    @pytest.mark.parametrize("caseinfo2",
                             read_testcase(
                                 "test_case", "\datas\quotation_handhotel.yaml"))
    @allure.title('創建酒店項目')
    def test_handhotel(self, driver, caseinfo2):
        f = QuotationPage(driver)
        f.handhotel(caseinfo2["texthotel_search"], caseinfo2["texthotelcity"], caseinfo2["texthotelcountry"],
                    caseinfo2["texthotelpropertytype"], caseinfo2["texthotelspecial"], caseinfo2["texthotelroomplan"],
                    caseinfo2["texthotelfare_invoice"], caseinfo2["texthotelfare_xo"], caseinfo2["texthotelfare_unit"],
                    caseinfo2["texthotelfare_remark"])

    @pytest.mark.parametrize("caseinfo2",
                             read_testcase(
                                 "test_case", "\datas\quotation_othercharge.yaml"))
    @allure.title('創建其他費用項目')
    def test_othercharge(self, driver, caseinfo2):
        f = QuotationPage(driver)
        f.create_other(caseinfo2["subscript"], caseinfo2["textothercharge_invoice"], caseinfo2["textothercharge_xo"],
                       caseinfo2["textothercharge_unit"], caseinfo2["textothercharge_remark"])
        # f.othercharge(caseinfo2["textothercharge_invoice"], caseinfo2["textothercharge_xo"], caseinfo2["textothercharge_unit"], caseinfo2["textothercharge_remark"])

    @pytest.mark.parametrize("caseinfo2",
                             read_testcase(
                                 "test_case", "\datas\quotation_daytour.yaml"))
    @allure.title('創建一日遊項目')
    def test_daytour(self, driver, caseinfo2):
        f = QuotationPage(driver)
        f.create_daytour(caseinfo2["subscript"], caseinfo2["textdaytour_invoice"], caseinfo2["textdaytour_xo"],
                         caseinfo2["textdaytour_unit"],
                         caseinfo2["textdaytour_remark"], caseinfo2["textdaytour_itemremark"])
        # f.daytour(caseinfo2["textdaytour_invoice"], caseinfo2["textdaytour_xo"], caseinfo2["textdaytour_unit"],
        #           caseinfo2["textdaytour_remark"], caseinfo2["textdaytour_itemremark"])

    @allure.title('創建發票確定進入下一頁')
    def test_next(self, driver):
        f = QuotationPage(driver)
        f.nextquotation()

    # @pytest.mark.parametrize("caseinfo2",
    #                          read_testcase(
    #                              "test_case", "\datas\QuotationAdd_group.yaml"))
    # @allure.title('添加團')
    # def test_group(self, driver, caseinfo2):
    #     f = QuotationAddPage(driver)
    #     f.group(caseinfo2["textgroupname"], caseinfo2["textgroupcontacts"], caseinfo2["textgroupdescription"],
    #             caseinfo2["textgroupremark"], caseinfo2["textnumber"])
    #
    @pytest.mark.parametrize("caseinfo2",
                             read_testcase(
                                 "test_case", "\datas\QuotationAdd_passenger.yaml"))
    @allure.title('添加乘客')
    def test_passenger(self, driver, caseinfo2):
        f = QuotationAddPage(driver)
        f.passenger(caseinfo2["textpassengerfirstname"], caseinfo2["textpassengersecondname"])

    @allure.title('創建發票進入打印本頁面')
    def test_finalcheck(self, driver):
        f = QuotationAddPage(driver)
        # f.choicepassenger()
        f.finalcheck()

    @allure.title("进入发票编辑页面")
    def test_invoice_copy(self, driver):
        inv = LeadlisteningPage(driver)
        inv.printout_booking()
        # 选择第一个项目点击编辑
        inv.riseinvoice_edit()
        # time.sleep(30)

    @pytest.mark.parametrize("caseinfo2",
                             read_testcase("test_case", "\datas\invoice_edit\Invoice_edit_route.yaml"))
    @allure.title("编辑航线项目")
    def test_edit_route(self, driver, caseinfo2):
        inv = QuotationEditPage(driver)
        inv.quotation_edit_route(caseinfo2["subscript_0"], caseinfo2["textbasicfare_invoice"], caseinfo2["subscript_1"],
                               caseinfo2["textbasicfare_xo"], caseinfo2["subscript_2"],
                               caseinfo2["texttickettax_invoice"], caseinfo2["subscript_3"],
                               caseinfo2["texttickettax_xo"], caseinfo2["subscript0"], caseinfo2["passenger0"],
                               caseinfo2["subscript1"], caseinfo2["passenger1"], caseinfo2["subscript2"],
                               caseinfo2["passenger2"], caseinfo2["subscript3"], caseinfo2["passenger3"],
                               caseinfo2["subscript4"], caseinfo2["passenger4"])

    @allure.title("点击确认完成编辑")
    def test_edit_finsh(self, driver):
        inv = QuotationEditPage(driver)
        inv.finalcheck()


if __name__ == '__main__':
    pytest.main(['-s', './test1.py', '--clean-alluredir', '--alluredir=./temps/test_smoke_invoice_allure'])
    os.system('allure generate ./temps/test_temp_invoice_allure -o ./allure-report --clean')
