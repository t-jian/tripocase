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
class PayOrderPage(BasePage):
    # 元素集
    # 发票
    e_createinvoce = ".btn-bar-line-2 > .ant-btn:nth-child(3)"
    # 报价单
    e_createquotation = ".btn-bar:nth-child(3) > .ant-btn:nth-child(3)"
    # xo
    e_createxo = ".btn-bar-line-2 > .ant-btn:nth-child(2)"
    # 打印本回詢價單
    fieldbooking_printout_booking = "#content > div > div > div.btn-bar > button.PublicButton.ant-btn.ant-btn-primary"

    # 詢價單
    fieldbooking = ".bottom-detail .font-ari"
    # fieldbooking_invoice = ".ant-tabs-nav-container:nth-child(2) .ant-tabs-tab:nth-child(2)"
    # fieldbooking_invoice = "/html/body/div[1]/div/div/div[2]/div/div[5]/div[2]/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[2]"

    fieldbooking_invoice = "div#content > div > div:nth-of-type(5) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div > div > div > div > div > div > div > div > div:nth-of-type(2)"
    fieldbooking_invoice_item = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.list-detail.ant-spin-nested-loading > div > div.list.heighter > div > div.clearfix.control-bar > label > span.ant-checkbox > input"

    # 報價單轉發票和xo部分
    fieldbooking_quotation = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-bar.ant-tabs-top-bar.ant-tabs-card-bar > div > div > div > div > div:nth-child(1) > div.ant-tabs-tab-active.ant-tabs-tab"
    fieldbooking_quotation_item = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.list-detail.ant-spin-nested-loading > div > div.list.heighter > div > div.clearfix.control-bar > label > span.ant-checkbox > input"
    fieldbooking_quotation_item_xo_confirm = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.bottom.control-bar > div > button:nth-child(4)"
    fieldbooking_quotation_item_invoice_confirm = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.bottom.control-bar > div > button:nth-child(3)"
    # xo轉報價單單部分
    fieldbooking_supplier = ".quote-list > div:nth-child(2) > span:nth-child(2)"
    fieldbooking_xo = ".ant-collapse-content-active > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)"
    fieldbooking_xo_item = ".ant-collapse-content-active > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)"
    fieldbooking_xo_item_quotation_confirm = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.bottom.control-bar > div > button:nth-child(6)"

    # 發票轉xo部分
    fieldbooking_invoice_item_xo = "div#content > div > div:nth-of-type(5) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div > div > div:nth-of-type(3) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > button:nth-of-type(4)"
    fieldbooking_invoice_item_xo_item = "div#content > div > div:nth-of-type(2) > div > label > span > input"
    fieldbooking_invoice_item_xo_confirm = "div#content > div > div:nth-of-type(4) > button"

    # 報價單編輯

    # 發票編輯
    # xo編輯
    # 報價單、發票、xo編輯
    fieldbooking_invoice_edit = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.list-detail.ant-spin-nested-loading > div > div.list.heighter > div:nth-child(1) > div.clearfix.control-bar > i:nth-child(5) > svg"
    fieldbooking_quotation_edit = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.list-detail.ant-spin-nested-loading > div > div.list.heighter > div:nth-child(1) > div.clearfix.control-bar > i:nth-child(4) > svg"
    # 發票複製：
    fieldbooking_invoice_copy = "#content > div > div.bottom-bar > div > button:nth-child(1)"
    # 選擇複製到本地文件夾
    fieldbooking_invoice_copy_local = "#content > div > div.copy-mount-node > div > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div:nth-child(1)"
    fieldbooking_invoice_copy_confirm = "#content > div > div.copy-mount-node > div > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > button.ant-btn.ant-btn-primary"
    fieldbooking_quotation_copy_confirm = "#content > div > div.copy-mount-node > div > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button.PublicButton.ant-btn.ant-btn-primary"
    # 發票退款申請部分
    fieldbooking_invoice_item_refundapplication = "div#content > div > div:nth-of-type(5) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div > div > div:nth-of-type(3) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > button:nth-of-type(1)"
    # fieldbooking_invoice_item_refundapplication_item = ".list-info > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)"

    fieldbooking_invoice_item_refundapplication_item = "#content > div > div.RefundApplicationContent > div.code-tabs.ant-tabs.ant-tabs-top.ant-tabs-card.ant-tabs-no-animation > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div > div.reset_tabs_card.two-tabs.ant-tabs.ant-tabs-top.ant-tabs-card.ant-tabs-no-animation > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.air-tickets.ant-tabs-tabpane.ant-tabs-tabpane-active > div.list-info > div > div:nth-child(2) > div.top > label > span > input"
    fieldbooking_invoice_item_refundapplication_confirm = "button.ant-btn-primary:nth-child(1)"
    fieldbooking_invoice_item_refundapplication_contactperson = "/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/form/div[1]/div[2]/div/span/input"
    fieldbooking_invoice_item_refundapplication_phone = "/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/form/div[2]/div[2]/div/span/input"
    fieldbooking_invoice_item_refundapplication_remark = "/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/form/div[8]/div[2]/div/span/div/div/div[1]/textarea"
    fieldbooking_invoice_item_refundapplication_description = "/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/form/div[9]/div[2]/div/span/div/div/div[1]/textarea"
    fieldbooking_invoice_item_refundapplication_calendar = "/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[6]/div[2]/div/span/span/span/div/input"  # 酒店日历
    fieldbooking_invoice_item_refundapplication_xo = "/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]"
    fieldbooking_invoice_item_refundapplication_xo_remark = "/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/form/div[2]/div[2]/div/span/textarea"
    fieldbooking_invoice_item_refundapplication_submit = "/html/body/div[1]/div/div/div[2]/div/div[3]/button[2]"

    # xo退款申請部分
    fieldbooking_xo_item_refundapplication = ".ant-collapse-content-active > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)"

    # 發票收款部分
    fieldbooking_invoice_item_receipt = "div#content > div > div:nth-of-type(5) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div > div > div:nth-of-type(3) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > button:nth-of-type(3)"
    filedreceipt_fare = "//div[2]/div/div/div/ul/li"
    receipt_allfare = "div#content > div > div:nth-of-type(3) > button"
    receipt_way = ".service-input .ant-select-selection__rendered"
    receipt_waydefault = ".ant-select-dropdown-menu-item-active"
    filedreceipt_bankchage = "/html/body/div[1]/div/div/div[2]/div/div[5]/div[3]/div[1]/div[2]/div/div[2]/div[2]/span/div[1]/div[2]/input"
    filedreceipt_creditchage = "/html/body/div[1]/div/div/div[2]/div/div[5]/div[3]/div[1]/div[2]/div/div[3]/div[2]/span/div[1]/div[2]/input"

    receipt_comfirm = "#content > div > div.btn-bar > button.PublicButton.ant-btn.ant-btn-primary.ant-btn-lg"

    # xo付款部分
    fieldbooking_xo_item_receipt = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.bottom.control-bar > div > button:nth-child(5)"
    fieldbooking_xo_item_receipt_comfirm = "button.ant-btn-lg:nth-child(2)"
    fieldbooking_xo_item_refund = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.bottom.control-bar > div > button:nth-child(4)"

    # xo收款部分

    # 發票退款部分
    fieldbooking_invoice_item_refund = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.bottom.control-bar > div > button:nth-child(3)"
    fieldbooking_invoice_item_refund_fare = "/html/body/div/div/div/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr/td[6]/div/div[2]/input"
    fieldbooking_invoice_item_refund_way = "#content > div > div.reset_tabs_card.tabs.ant-tabs.ant-tabs-top.ant-tabs-card.ant-tabs-no-animation > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.order-box > div > div:nth-child(1) > div.pay-input > div > div > div"
    fieldbooking_invoice_item_refund_waydefault = "div#dbfd488e-fa78-4853-c64f-f2222db1d9c8 > ul > li"
    fieldbooking_invoice_item_refund_bankchage = "/html/body/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div[2]/div[4]/div[1]/div[2]/span/div[1]/div[2]/input"
    fieldbooking_invoice_item_refund_creditchage = "/html/body/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div[2]/div[4]/div[2]/div[2]/span/div[1]/div[2]/input"

    # fieldbooking_invoice_item_refund_comfirm = "#content > div > div.btn-bar > button.PublicButton.ant-btn.ant-btn-primary.ant-btn-lg"


    # 收款的打印本頁面
    def receipt(self, receipt_fare, receipt_bankchage, receipt_creditchage):
        if(receipt_fare==0):
            self.cssclick(self.receipt_allfare)
        else:
            self.xpathsend(self.filedreceipt_fare, receipt_fare)
        self.cssclick(self.receipt_way)
        self.cssclick(self.receipt_waydefault)
        self.xpathsend(self.filedreceipt_bankchage, receipt_bankchage)
        self.xpathsend(self.filedreceipt_creditchage, receipt_creditchage)
        self.cssclick(self.receipt_comfirm)
        self.newHandle()




