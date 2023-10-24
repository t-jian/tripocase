__author__ = 'david'

import time
import unittest
import sys
import pytest
import os
import allure
import pytest

from selenium import webdriver

from Tripo.Tripo_Web.pages.Addenquiry import AddenquiryPage
from Tripo.Tripo_Web.pages.LoginPage import LoginPage
from Tripo.Tripo_Web.pages.MakeInvoicePage import MakeInvoicePage
from Tripo.Tripo_Web.pages.PayOrderPage import PayOrderPage
from Tripo.Tripo_Web.pages.QuotationAddPage import QuotationAddPage
from Tripo.Tripo_Web.pages.RefundApplicationPage import RefundApplicationPage
from Tripo.Tripo_Web.pages.RefundPage import RefundPage
from Tripo.Tripo_Web.pages.data import *
from Tripo.Tripo_Web.pages.LeadlisteningPage import LeadlisteningPage
from Tripo.Tripo_Web.pages.QuotationPage import QuotationPage

import logging

logger = logging.getLogger(__name__)


class Test_Create_XO:
    @pytest.mark.parametrize("caseinfo",
                             read_testcase("test_case", "\datas\login.yaml"))
    def test_login(self, driver, caseinfo):
        logger.info("开始执行用例")
        allure.attach(driver.get_screenshot_as_png(), '开始执行用例')
        login1 = LoginPage(driver)
        driver.get(caseinfo["login"]["url"])
        login1.login(caseinfo["login"]["textaccount"], caseinfo["login"]["textpassword"],
                     caseinfo["login"]["textcompanycode"])
        # msg =
        # assert sys_msg == msg
        logger.info("测试通过")
        allure.attach(driver.get_screenshot_as_png(), '用例后')

    @pytest.mark.parametrize("caseinfo",
                             read_testcase("test_case", "\datas\quotation_rise.yaml"))
    def test_createxo(self, driver, caseinfo):
        b = LeadlisteningPage(driver)
        b.createxo()
        a = AddenquiryPage(driver)
        # a.risebooking()
        a.risebooking_select(caseinfo["textuser_name"])
        c = QuotationPage(driver)
        c.create_XO(caseinfo["testsupplier_name"], caseinfo["textdiscount"])
        # c.risexo(caseinfo["textdiscount"])

    # @pytest.mark.parametrize("caseinfo1",
    #                          read_testcase(
    #                              "test_case", "\datas\quotation_apiticket.yaml"))
    # def test_apiticket(self, driver, caseinfo1):
    #     e = QuotationPage(driver)
    #     e.apiticket(caseinfo1["texttrip"], caseinfo1["textreturn"])

    @pytest.mark.parametrize("caseinfo2",
                             read_testcase(
                                 "test_case", "\datas\quotation_handticket.yaml"))
    @allure.title("创建PNR输入航线项目")
    def test_handticket(self, driver, caseinfo2):
        f = QuotationPage(driver)
        f.handticket(caseinfo2["textcontentpnr"], caseinfo2["textbasicfare_invoice"], caseinfo2["textbasicfare_xo"],
                     caseinfo2["texttickettax_invoice"], caseinfo2["texttickettax_xo"])

    # @pytest.mark.parametrize("caseinfo2",
    #                          read_testcase(
    #                              "test_case", "\datas\quotation_handapiticket.yaml"))
    # @allure.title("创建手动输入航线项目")
    # def test_handapiticket(self, driver, caseinfo2):
    #     f = QuotationPage(driver)
    #     f.handapiticket(caseinfo2["textcontentapipnr"], caseinfo2["textbasicfare_invoice"],
    #                     caseinfo2["textbasicfare_xo"], caseinfo2["texttickettax_invoice"],
    #                     caseinfo2["texttickettax_xo"])

    @pytest.mark.parametrize("caseinfo2",
                             read_testcase(
                                 "test_case", "\datas\quotation_handhotel.yaml"))
    @allure.title("创建酒店项目")
    def test_handhotel(self, driver, caseinfo2):
        f = QuotationPage(driver)
        f.handhotel(caseinfo2["texthotel_search"], caseinfo2["texthotelcity"], caseinfo2["texthotelcountry"],
                    caseinfo2["texthotelpropertytype"], caseinfo2["texthotelspecial"], caseinfo2["texthotelroomplan"],
                    caseinfo2["texthotelfare_invoice"], caseinfo2["texthotelfare_xo"], caseinfo2["texthotelfare_unit"],
                    caseinfo2["texthotelfare_remark"])

    @pytest.mark.parametrize("caseinfo2",
                             read_testcase(
                                 "test_case", "\datas\quotation_othercharge.yaml"))
    @allure.title("创建其他费用项目")
    def test_othercharge(self, driver, caseinfo2):
        f = QuotationPage(driver)
        # f.othercharge(caseinfo2["textothercharge_invoice"], caseinfo2["textothercharge_xo"], caseinfo2["textothercharge_unit"], caseinfo2["textothercharge_remark"])
        f.create_other(caseinfo2["subscript"], caseinfo2["textothercharge_invoice"], caseinfo2["textothercharge_xo"],
                       caseinfo2["textothercharge_unit"], caseinfo2["textothercharge_remark"])

    @pytest.mark.parametrize("caseinfo2",
                             read_testcase(
                                 "test_case", "\datas\quotation_daytour.yaml"))
    @allure.title("创建一日游项目")
    def test_daytour(self, driver, caseinfo2):
        f = QuotationPage(driver)
        f.create_daytour(caseinfo2["subscript"], caseinfo2["textdaytour_invoice"], caseinfo2["textdaytour_xo"],
                         caseinfo2["textdaytour_unit"],
                         caseinfo2["textdaytour_remark"], caseinfo2["textdaytour_itemremark"])
        # f.daytour(caseinfo2["textdaytour_invoice"], caseinfo2["textdaytour_xo"], caseinfo2["textdaytour_unit"],
        #           caseinfo2["textdaytour_remark"], caseinfo2["textdaytour_itemremark"])

    @allure.title("进入编辑页面")
    def test_next(self, driver):
        f = QuotationPage(driver)
        f.nextquotation()

    @pytest.mark.parametrize("caseinfo2",
                             read_testcase(
                                 "test_case", "\datas\QuotationAdd_passenger.yaml"))
    @allure.title("添加乘客")
    def test_passenger(self, driver, caseinfo2):
        f = QuotationAddPage(driver)
        f.passenger(caseinfo2["textpassengerfirstname"], caseinfo2["textpassengersecondname"])

    @allure.title("点击确认创建XO")
    def test_finalcheck(self, driver):
        f = QuotationAddPage(driver)
        # f.choicepassenger()
        f.finalcheck()

    @allure.title("編輯XO複製XO")
    def test_XO_copy(self, driver):
        xo = LeadlisteningPage(driver)
        xo.printout_booking()
        xo.copy_XO()
    time.sleep(5)


if __name__ == '__main__':
    pytest.main(['-s', './test1.py', '--clean-alluredir', '--alluredir=./temps/test_smoke_xo_allure'])
    os.system('allure generate ./temps/test_smoke_xo_allure -o ./allure-report/test_smoke_xo_allure --clean')
