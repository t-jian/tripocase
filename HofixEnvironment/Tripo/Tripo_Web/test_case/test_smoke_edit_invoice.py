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
class TestInvoice:
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
        # msg =
        # assert sys_msg == msg
        logger.info("测试通过")
        allure.attach(driver.get_screenshot_as_png(), '用例后')

    @pytest.mark.parametrize("caseinfo",
                             read_testcase("test_case", "\datas\quotation_rise.yaml"))
    def test_createinvoice(self, driver, caseinfo):
        b = LeadlisteningPage(driver)
        b.createinvoice()
        c = QuotationPage(driver)
        c.riseinvoice(caseinfo["textdiscount"])

    # @pytest.mark.parametrize("caseinfo1",
    #                          read_testcase(
    #                              "test_case", "\datas\quotation_apiticket.yaml"))
    # def test_apiticket(self, driver, caseinfo1):
    #     e = QuotationPage(driver)
    #     e.apiticket(caseinfo1["texttrip"], caseinfo1["textreturn"])
    #
    # @pytest.mark.parametrize("caseinfo2",
    #                          read_testcase(
    #                              "test_case", "\datas\quotation_handticket.yaml"))
    # def test_handticket(self, driver, caseinfo2):
    #     f = QuotationPage(driver)
    #     f.handticket(caseinfo2["textcontentpnr"], caseinfo2["textbasicfare_invoice"], caseinfo2["textbasicfare_xo"],
    #                  caseinfo2["texttickettax_invoice"], caseinfo2["texttickettax_xo"])
    #
    # @pytest.mark.parametrize("caseinfo2",
    #                          read_testcase(
    #                              "test_case", "\datas\quotation_handapiticket.yaml"))
    # def test_handapiticket(self, driver, caseinfo2):
    #     f = QuotationPage(driver)
    #     f.handapiticket(caseinfo2["textcontentapipnr"], caseinfo2["textbasicfare_invoice"],
    #                     caseinfo2["textbasicfare_xo"], caseinfo2["texttickettax_invoice"],
    #                     caseinfo2["texttickettax_xo"])
    #
    # @pytest.mark.parametrize("caseinfo2",
    #                          read_testcase(
    #                              "test_case", "\datas\quotation_handhotel.yaml"))
    # def test_handhotel(self, driver, caseinfo2):
    #     f = QuotationPage(driver)
    #     f.handhotel(caseinfo2["texthotel_search"], caseinfo2["texthotelcity"], caseinfo2["texthotelcountry"],
    #                 caseinfo2["texthotelpropertytype"], caseinfo2["texthotelspecial"], caseinfo2["texthotelroomplan"],
    #                 caseinfo2["texthotelfare_invoice"], caseinfo2["texthotelfare_xo"], caseinfo2["texthotelfare_unit"],
    #                 caseinfo2["texthotelfare_remark"])

    @pytest.mark.parametrize("caseinfo2",
                             read_testcase(
                                 "test_case", "\datas\quotation_othercharge.yaml"))
    def test_othercharge(self, driver, caseinfo2):
        f = QuotationPage(driver)
        f.othercharge(caseinfo2["textothercharge_invoice"], caseinfo2["textothercharge_xo"],
                      caseinfo2["textothercharge_unit"], caseinfo2["textothercharge_remark"])

    # @pytest.mark.parametrize("caseinfo2",
    #                          read_testcase(
    #                              "test_case", "\datas\quotation_daytour.yaml"))
    # def test_daytour(self, driver, caseinfo2):
    #     f = QuotationPage(driver)
    #     f.daytour(caseinfo2["textdaytour_invoice"], caseinfo2["textdaytour_xo"], caseinfo2["textdaytour_unit"],
    #               caseinfo2["textdaytour_remark"], caseinfo2["textdaytour_itemremark"])

    def test_next(self, driver):
        f = QuotationPage(driver)
        f.nextquotation()

    # @pytest.mark.parametrize("caseinfo2",
    #                          read_testcase(
    #                              "test_case", "\datas\QuotationAdd_group.yaml"))
    # def test_group(self, driver, caseinfo2):
    #     f = QuotationAddPage(driver)
    #     f.group13579(caseinfo2["textgroupname"], caseinfo2["textgroupcontacts"], caseinfo2["textgroupdescription"],
    #                  caseinfo2["textgroupremark"])

    @pytest.mark.parametrize("caseinfo2",
                             read_testcase(
                                 "test_case", "\datas\QuotationAdd_passenger.yaml"))
    def test_passenger(self, driver, caseinfo2):
        f = QuotationAddPage(driver)
        f.passenger(caseinfo2["textpassengerfirstname"], caseinfo2["textpassengersecondname"])
        # time.sleep(20)

    def test_finalcheck(self, driver):
        f = QuotationAddPage(driver)
        f.choicepassenger()
        f.finalcheck()

    # invoice編輯
    @pytest.mark.parametrize("caseinfo",
                             read_testcase("test_case", "\datas\quotation_rise.yaml"))
    def test_riseinvoice_edit(self, driver, caseinfo):
        f = LeadlisteningPage(driver)
        f.printout_booking()
        f.riseinvoice_edit()

    # 編輯其他費用
    @pytest.mark.parametrize("caseinfo2",
                             read_testcase(
                                 "test_case", "\datas\quotation_othercharge.yaml"))
    def test_riseinvoice_edit_othercharge(self, driver, caseinfo2):
        f = QuotationEditPage(driver)
        f.riseinvoice_othercharge(caseinfo2["textothercharge_invoice_edit"], caseinfo2["textothercharge_xo_edit"],
                      caseinfo2["textothercharge_unit_edit"], caseinfo2["textothercharge_remark_edit"])

        f.finalcheck()
        time.sleep(100)

    #
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_testcase("test_case", "\datas\quotation_rise.yaml"))
    # def test_invoice_to_xo(self, driver, caseinfo):
    #     f = LeadlisteningPage(driver)
    #     f.printout_booking()
    #     f.riseinvoice_xo()
    #     d = MakeInvoicePage(driver)
    #     d.choice_invoice_to_xo_item()
    #     c = QuotationAddPage(driver)
    #     c.risexo(caseinfo["textdiscount"])
    #     c.finalcheck()
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_testcase("test_case", "\datas\PayOrder.yaml"))
    # def test_invoice_to_receipt(self, driver, caseinfo):
    #     f = LeadlisteningPage(driver)
    #     f.printout_booking()
    #     f.riseinvoice_receipt()
    #     d = PayOrderPage(driver)
    #     d.receipt(caseinfo["receipt_fare"], caseinfo["receipt_bankchage"], caseinfo["receipt_creditchage"])
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_testcase("test_case", "\datas\Refund.yaml"))
    # def test_invoice_to_refund(self, driver, caseinfo):
    #     f = LeadlisteningPage(driver)
    #     f.printout_booking()
    #     f.riseinvoice_refund()
    #     d = RefundPage(driver)
    #     d.refund(caseinfo["refund_fare"], caseinfo["refund_bankchage"], caseinfo["refund_creditchage"])
    #     # time.sleep(1000)
    #
    # @pytest.mark.parametrize("caseinfo",
    #                          read_testcase("test_case", "\datas\RefundApplication.yaml"))
    # def test_invoice_to_refundapplication(self, driver, caseinfo):
    #     f = LeadlisteningPage(driver)
    #     f.printout_booking()
    #     f.riseinvoice_refundapplication()
    #     d = RefundApplicationPage(driver)
    #     d.refundapplication(caseinfo["textcontactperson"], caseinfo["textphone"], caseinfo["refundapplication_remark"],
    #                         caseinfo["refundapplication_description"], caseinfo["refundapplication_xo_remark"])
    #     f.printout_booking()
    #     # time.sleep(1000)


if __name__ == '__main__':
    pytest.main(['-s', './test1.py', '--clean-alluredir', '--alluredir=./temps/test_smoke_invoice_allure'])
    os.system('allure generate ./temps/test_smoke_invoice_allure -o ./allure-report --clean')
