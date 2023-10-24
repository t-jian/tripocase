# searchPage.py 代码如下
# _*_ coding:utf-8 _*_

__author__ = 'David'

import time

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
class LeadlisteningPage(BasePage):
    # 元素集
    # 发票
    e_createinvoce = ".btn-bar-line-2 > .ant-btn:nth-child(3)"
    # 报价单
    e_createquotation = ".btn-bar:nth-child(3) > .ant-btn:nth-child(3)"
    # xo
    e_createxo = ".btn-bar-line-2 > .ant-btn:nth-child(2)"
    # 打印本返回列表
    fieldbooking_printout_booking = "#content > div > div > div.btn-bar > button.PublicButton.ant-btn.ant-btn-primary"

    # 詢價單
    # 選擇第一個報價單
    fieldquotation_order_one = '//*[@id="content"]/div/div[5]/div[2]/div/div[1]/div[2]/div/div/div[3]/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/label/span[1]/input'
    # 第一張報價單變價按鈕
    fieldquotation_order_one_edit = '//*[@id="content"]/div/div[5]/div[2]/div/div[1]/div[2]/div/div/div[3]/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/i[3]'
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
    fieldbooking_xo_item_invoice_confirm = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.bottom.control-bar > div > button:nth-child(3)"
    # 發票轉xo部分
    fieldbooking_invoice_item_xo = "div#content > div > div:nth-of-type(5) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div > div > div:nth-of-type(3) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > button:nth-of-type(4)"
    fieldbooking_invoice_item_xo_item = "div#content > div > div:nth-of-type(2) > div > label > span > input"
    fieldbooking_invoice_item_xo_confirm = "div#content > div > div:nth-of-type(4) > button"

    # 發票編輯部分
    fieldbooking_invoice_item_edit = ".blue:nth-child(5) use"

    # 報價單編輯
    # 發票編輯
    # 發票復製按鈕
    invoice_copy_button = '//*[@id="content"]/div/div[4]/div/button[1]'
    # 複製到現有的文件內
    old_file = '//*[@id="content"]/div/div[6]/div/div/div[2]/div/div[2]/div[2]/div[1]'
    # 複製到新文件內
    new_file = '//*[@id="content"]/div/div[6]/div/div/div[2]/div/div[2]/div[2]/div[2]'
    # 複製確定/取消按鈕
    invoice_copy_confirm = '//*[@id="content"]/div/div[6]/div/div/div[2]/div/div[2]/div[3]/button[2]'
    invoice_copy_cancel = '//*[@id="content"]/div/div[6]/div/div/div[2]/div/div[2]/div[3]/button[1]'

    # xo編輯
    # XO複製
    # 選擇第一張XO
    fieldbooking_first_XO = '//*[@id="content"]/div/div[5]/div[2]/div/div[2]/div[2]/div/div/div[3]/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/label/span[1]/input'
    # 編輯XO按鈕
    fieldbooking_edit_XO = '//*[@id="content"]/div/div[5]/div[2]/div/div[2]/div[2]/div/div/div[3]/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/i[4]'

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
    fieldbooking_invoice_item_receipt_allfare = "div#content > div > div:nth-of-type(3) > button"
    fieldbooking_invoice_item_receipt_way = "#content > div > div.reset_tabs_card.tabs.ant-tabs.ant-tabs-top.ant-tabs-card.ant-tabs-no-animation > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.order-box > div > div:nth-child(1) > div.pay-input > div > div > div"
    fieldbooking_invoice_item_receipt_waydefault = "div#dbfd488e-fa78-4853-c64f-f2222db1d9c8 > ul > li"
    fieldbooking_invoice_item_receipt_bankchage = "/html/body/div[1]/div/div/div[2]/div/div[5]/div[3]/div[1]/div[2]/div/div[2]/div[2]/span/div[1]/div[2]/input"
    fieldbooking_invoice_item_receipt_creditchage = "/html/body/div[1]/div/div/div[2]/div/div[5]/div[3]/div[1]/div[2]/div/div[3]/div[2]/span/div[1]/div[2]/input"

    fieldbooking_invoice_item_receipt_comfirm = "#content > div > div.btn-bar > button.PublicButton.ant-btn.ant-btn-primary.ant-btn-lg"

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

    def createinvoice(self):
        self.cssclick(self.e_createinvoce)

    def createxo(self):
        self.cssclick(self.e_createxo)

    def createquotation(self):
        self.cssclick(self.e_createquotation)

    # 打印本轉詢價單主頁面
    def  printout_booking(self):
        self.cssclick(self.fieldbooking_printout_booking)

    # 發票編輯
    def riseinvoice_edit(self):
        """
        进入发票编辑页面
        """
        try:
            # 1、勾線第一個發票選項
            self.cssclick(self.fieldbooking_invoice)
            # 2、勾線發票第一個項目
            self.cssclick(self.fieldbooking_invoice_item)
            # 3、點擊編輯
            self.cssclick(self.fieldbooking_invoice_item_edit)
            self.newHandle()
            logger.info("进入发票编辑页面成功！")
        except Exception as e:
            logger.error(f"进入发票编辑页面失败！{e}")
            raise

    # XO编辑
    def riseXO_edit(self):
        """
        进入XO编辑页面
        """
        try:
            # 選擇供應商欄位
            self.cssclick(self.fieldbooking_supplier)
            # 編輯XO
            self.xpathclick(self.fieldbooking_edit_XO)
            # 切換句柄
            self.newHandle()
            logger.info("进入XO编辑页面成功!")
        except Exception as e:
            logger.error(f"进入XO编辑页面失败！{e}")
            raise

    # 報價單編輯
    def riseQuotation_edit(self):
        """
        進入報價單編輯頁面
        """
        try:
            # 選擇報價單欄位
            self.cssclick(self.fieldbooking_quotation)
            # 編輯第一張報價單按鈕
            self.xpathclick(self.fieldquotation_order_one_edit)
            # 切換句柄
            self.newHandle()
            logger.info("進入報價單編輯頁面成功！")
        except Exception as e:
            logger.error(f"進入報價單編輯頁面失敗！{e}")
            raise

    # 發票複製
    def copy_invoice(self):
        """
        復製發票
        """
        try:
            # 選擇第一個項目
            self.cssclick(self.fieldbooking_invoice)
            # 選擇第一個項目
            self.cssclick(self.fieldbooking_invoice_item)
            # 進入編輯頁面
            self.cssclick(self.fieldbooking_invoice_item_edit)
            # 切換句柄
            self.newHandle()
            # 點擊復製按鈕
            self.xpathclick(self.invoice_copy_button)
            # 選擇複製到現有的文件內
            self.xpathclick(self.old_file)
            # 最後確認按鈕
            self.xpathclick(self.invoice_copy_confirm)
            logger.info("复制发票成功！")
        except Exception as e:
            logger.error(f"复制发票失败！{e}")
            raise

    # XO複製
    def copy_XO(self):
        """
        複製XO
        """
        try:
            # 選擇供應商欄位
            self.cssclick(self.fieldbooking_supplier)
            # 編輯XO
            self.xpathclick(self.fieldbooking_edit_XO)
            # 切換句柄
            self.newHandle()
            # 複製XO
            self.xpathclick(self.invoice_copy_button)
            time.sleep(1)
            # 選擇複製到現有的文件內
            self.xpathclick(self.old_file)
            # 最後確認按鈕
            self.xpathclick(self.invoice_copy_confirm)
            logger.info("复制XO成功！")
        except Exception as e:
            logger.error(f"复制XO失败！{e}")
            raise

    # 報價單複製
    def copy_quotation(self):
        """
        複製quotation(報價單)
        """
        try:
            # 選擇報價單欄位
            self.cssclick(self.fieldbooking_quotation)
            # 編輯第一張報價單按鈕
            self.xpathclick(self.fieldquotation_order_one_edit)
            # 切換句柄
            self.newHandle()
            # 複製報價單
            self.xpathclick(self.invoice_copy_button)
            # 選擇複製到現有的文件內
            self.xpathclick(self.old_file)
            # 最後確認按鈕
            self.xpathclick(self.invoice_copy_confirm)
            time.sleep(3)
            logger.info("複製報檢單成功")
        except Exception as e:
            logger.error(f"復製報價單失敗。{e}")
            raise


    # 發票轉xo的打印本頁面
    def riseinvoice_xo(self):
        self.cssclick(self.fieldbooking_invoice)
        self.cssclick(self.fieldbooking_invoice_item)
        self.cssclick(self.fieldbooking_invoice_item_xo)
        self.newHandle()


    # 發票轉收據
    def riseinvoice_receipt(self):
        self.cssclick(self.fieldbooking_invoice)
        self.cssclick(self.fieldbooking_invoice_item)
        self.cssclick(self.fieldbooking_invoice_item_receipt)
        self.newHandle()


    # 發票退款
    def riseinvoice_refund(self):
        self.cssclick(self.fieldbooking_invoice)
        self.cssclick(self.fieldbooking_invoice_item)
        self.cssclick(self.fieldbooking_invoice_item_refund)
        self.newHandle()


    def riseinvoice_refundapplication(self):
        self.cssclick(self.fieldbooking_invoice)
        self.cssclick(self.fieldbooking_invoice_item)
        self.cssclick(self.fieldbooking_invoice_item_refundapplication)
        self.newHandle()


    # 詢價單轉xo的打印本頁面
    def risequotation_invoice(self):
        self.cssclick(self.fieldbooking_quotation)
        self.cssclick(self.fieldbooking_quotation_item)
        self.cssclick(self.fieldbooking_quotation_item_invoice_confirm)
        self.newHandle()


    # 詢價單轉xo的打印本頁面
    def risequotation_xo(self):
        self.cssclick(self.fieldbooking_quotation)
        self.cssclick(self.fieldbooking_quotation_item)
        self.cssclick(self.fieldbooking_quotation_item_xo_confirm)
        self.newHandle()


    # XO轉發票的打印本頁面
    def risexo_invoice(self):
        self.cssclick(self.fieldbooking_supplier)
        self.cssclick(self.fieldbooking_xo)
        self.cssclick(self.fieldbooking_xo_item)
        self.cssclick(self.fieldbooking_xo_item_invoice_confirm)
        self.newHandle()


    # XO轉報價單的打印本頁面
    def risexo_quotation(self):
        self.cssclick(self.fieldbooking_supplier)
        self.cssclick(self.fieldbooking_xo)
        self.cssclick(self.fieldbooking_xo_item)
        self.cssclick(self.fieldbooking_xo_item_quotation_confirm)
        self.newHandle()


    # XO轉收據
    def risexo_receipt(self):
        self.cssclick(self.fieldbooking_supplier)
        self.cssclick(self.fieldbooking_xo)
        self.cssclick(self.fieldbooking_xo_item)
        self.cssclick(self.fieldbooking_xo_item_receipt)
        self.newHandle()


    # XO退款
    def risexo_refund(self):
        self.cssclick(self.fieldbooking_supplier)
        self.cssclick(self.fieldbooking_xo)
        self.cssclick(self.fieldbooking_xo_item)
        self.cssclick(self.fieldbooking_xo_item_refund)
        self.newHandle()


    # XO退款申請
    def risexo_refundapplication(self):
        self.cssclick(self.fieldbooking_supplier)
        self.cssclick(self.fieldbooking_xo)
        self.cssclick(self.fieldbooking_xo_item)
        self.cssclick(self.fieldbooking_xo_item_refundapplication)
        self.newHandle()
