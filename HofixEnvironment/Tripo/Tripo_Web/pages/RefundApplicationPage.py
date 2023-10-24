# searchPage.py 代码如下
# _*_ coding:utf-8 _*_

__author__ = 'David'
#
# import sys
# from selenium.webdriver.common.by import By
# from pages.BasePage import BasePage
# import time
# import os
# import pyperclip
# from webdriver_helper import get_webdriver
# import pytest
# reload(sys)
# sys.setdefaultencoding("utf-8")
from Tripo.Tripo_Web.pages.BasePage import *


# 百度搜索page
class RefundApplicationPage(BasePage):
    # 元素集


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
    fieldcalendarday = "tr:nth-child(5) > .ant-calendar-cell:nth-child(3) > .ant-calendar-date"
    fieldcalendar = "#fromCityDate\\[0\\] .ant-calendar-picker-input"  # 点击日历选项
    fieldcalendarmonth = ".ant-calendar-next-month-btn"  # 点击下一个月
    # xo退款申請部分
    fieldbooking_xo_item_refundapplication = ".ant-collapse-content-active > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)"

    # 發票收款部分
    fieldbooking_invoice_item_receipt = "div#content > div > div:nth-of-type(5) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div > div > div:nth-of-type(3) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > button:nth-of-type(3)"
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
    refund_way = ".ant-select-selection__rendered"
    refund_waydefault = ".ant-select-dropdown-menu-item-active"
    fieldrefund_bankchage = "/html/body/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div[2]/div[4]/div[1]/div[2]/span/div[1]/div[2]/input"
    fieldrefund_creditchage = "/html/body/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div[2]/div[4]/div[2]/div[2]/span/div[1]/div[2]/input"

    fieldrefund_comfirm = ".ant-btn-primary"


    # 退款的頁面
    def refundapplication(self, textcontactperson, textphone, refundapplication_remark, refundapplication_description, refundapplication_xo_remark):

        self.cssclick(self.fieldbooking_invoice_item_refundapplication_item)
        time.sleep(1)
        self.cssclick(self.fieldbooking_invoice_item_refundapplication_confirm)

        self.xpathsend(self.fieldbooking_invoice_item_refundapplication_contactperson, textcontactperson)
        self.xpathsend(self.fieldbooking_invoice_item_refundapplication_phone, textphone)
        self.xpathclick(self.fieldbooking_invoice_item_refundapplication_calendar)
        self.cssclick(self.fieldcalendarmonth)
        self.cssclick(self.fieldcalendarday)
        self.xpathperclip(self.fieldbooking_invoice_item_refundapplication_remark, refundapplication_remark)
        self.xpathperclip(self.fieldbooking_invoice_item_refundapplication_description, refundapplication_description)
        self.xpathclick(self.fieldbooking_invoice_item_refundapplication_xo)
        self.xpathperclip(self.fieldbooking_invoice_item_refundapplication_xo_remark,refundapplication_xo_remark)
        self.xpathclick(self.fieldbooking_invoice_item_refundapplication_submit)
        self.newHandle()



