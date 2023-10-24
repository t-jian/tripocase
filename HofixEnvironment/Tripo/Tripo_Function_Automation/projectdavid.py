import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from waitdavid import WebDriverWaitDavid
import elementdavid
import pyperclip

homepage_handle = 1


# def setup_method(self, method):
#     self.driver = webdriver.Chrome()
#
#     self.vars = {}
#

def inputwaiting(self):
    print("顯示輸入進行下一步的內容", input("隨意輸入進行下一步："))


def cssprojectdavid(self, value):
    # print(value)
    # print(self.value)
    while True:
        try:
            # print("1")
            self.driver.find_element(By.CSS_SELECTOR, value).click()
            break
        except:
            time.sleep(1)
            # print("2")
            continue
            # print("超时")


def xpathprojectdavid(self, value):
    print(value)
    # print(self.value)
    while True:
        try:
            self.driver.find_element(By.XPATH, value).click()
            break
        except:
            time.sleep(1)
            continue
            # print("超时")


# 臨時報價單轉發票，發票添加其他費用
def risequotation_invoice1(self):
    global homepage_handle
    # n = self.driver.window_handles  # 获取当前页句柄
    # print(n)
    # self.driver.switch_to.window(n[1])
    # print("3")
    # 获取所有窗口的handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_quotation)

    cssprojectdavid(self, elementdavid.fieldbooking_quotation_item)

    homepage_handle = self.driver.window_handles

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, elementdavid.fieldbooking_quotation_item_invoice_confirm)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_quotation_item_invoice_confirm).click()

    handles = self.driver.window_handles
    print(homepage_handle)
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item_xo_item)

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo_confirm)))
    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item_xo_confirm)

    inputwaiting(self)
    time.sleep(1)
    nextpageadditem(self)
    apiticket(self)
    handticket1(self)
    handhotel1(self)
    othercharge1(self)
    daytour1(self)
    nextpage(self)
    inputwaiting(self)
    finalcheck(self)


# 發票轉xo，xo添加其他費用

def riseinvoice_xo1(self):
    global homepage_handle
    # n = self.driver.window_handles  # 获取当前页句柄
    # print(n)
    # self.driver.switch_to.window(n[1])
    # print("3")
    # 获取所有窗口的handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice)

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item)

    homepage_handle = self.driver.window_handles

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo).click()

    handles = self.driver.window_handles
    print(homepage_handle)
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item_xo_item)

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo_confirm)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo_confirm).click()

    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldxo_popsupplier)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldxo_popsupplier))

    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldxo_supplier)))
    cssprojectdavid(self, elementdavid.fieldxo_supplier)

    inputwaiting(self)
    time.sleep(1)
    nextpageadditem(self)
    apiticket(self)
    handticket1(self)
    handhotel1(self)
    othercharge1(self)
    daytour1(self)
    nextpage(self)
    inputwaiting(self)
    finalcheck(self)

    return homepage_handle


def login(self):
    global homepage_handle
    self.driver.get(elementdavid.web)
    # self.driver.set_window_size(1950, 939)
    self.driver.maximize_window()
    # 3 | click | css=.ant-row:nth-child(1) .ant-input |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.webaccount).click()
    # 4 | type | css=.ant-row:nth-child(1) .ant-input | david
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.webaccount).send_keys(elementdavid.textaccount)
    # 5 | pause | 1000 | 1000
    time.sleep(0.5)
    # 6 | click | css=.ant-input-affix-wrapper > .ant-input |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.webpassword).click()
    # 7 | type | css=.ant-input-affix-wrapper > .ant-input | Travel2021
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.webpassword).send_keys(elementdavid.textpassword)
    # 8 | pause | 1000 | 1000
    time.sleep(0.5)
    # 9 | click | css=.ant-row:nth-child(3) .ant-input |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.webcompanycode).click()
    # 10 | type | css=.ant-row:nth-child(3) .ant-input | TC0139
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.webcompanycode).send_keys(elementdavid.textcompanycode)
    # 11 | click | css=.login-button |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.weblogin).click()
    homepage_handle = self.driver.window_handles
    print("已点击登录")

    return homepage_handle


def risebooking(self):
    global homepage_handle
    # homepage_handle = self.driver.current_window_handle
    homepage_handle = self.driver.window_handles

    WebDriverWaitDavid(self.driver, 40).untilmyself(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, elementdavid.elementdavid.fieldbooking)))
    time.sleep(2)
    WebDriverWaitDavid(self.driver, 40).untilmyself1(
        self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking).click())
    return homepage_handle

# 打印本轉詢價單主頁面
def printout_booking(self):
    # n = self.driver.window_handles  # 获取当前页句柄
    # print(n)
    # self.driver.switch_to.window(n[2])

    cssprojectdavid(self, elementdavid.fieldbooking_printout_booking)
    # WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
    #     (By.CSS_SELECTOR, elementdavid.fieldbooking_printout_booking)))
    # self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
    #                                                                              elementdavid.fieldbooking_printout_booking))

# 報價單轉xo的打印本頁面
def risequotation_xo(self):
    global homepage_handle
    # n = self.driver.window_handles  # 获取当前页句柄
    # print(n)
    # self.driver.switch_to.window(n[1])
    # print("3")
    # 获取所有窗口的handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_quotation)

    cssprojectdavid(self, elementdavid.fieldbooking_quotation_item)

    homepage_handle = self.driver.window_handles

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, elementdavid.fieldbooking_quotation_item_xo_confirm)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_quotation_item_xo_confirm).click()

    handles = self.driver.window_handles
    print(homepage_handle)
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item_xo_item)

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo_confirm)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo_confirm).click()

    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldxo_popsupplier)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldxo_popsupplier))

    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldxo_supplier)))
    cssprojectdavid(self, elementdavid.fieldxo_supplier)

    cssprojectdavid(self, elementdavid.fieldxo_popconsultant)

    cssprojectdavid(self, elementdavid.fieldxo_consultant)

    finalcheck(self)
    return homepage_handle

# 報價單轉發票的打印本頁面
def risequotation_invoice(self):
    global homepage_handle
    # n = self.driver.window_handles  # 获取当前页句柄
    # print(n)
    # self.driver.switch_to.window(n[1])
    # print("3")
    # 获取所有窗口的handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_quotation)

    cssprojectdavid(self, elementdavid.fieldbooking_quotation_item)

    homepage_handle = self.driver.window_handles

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, elementdavid.fieldbooking_quotation_item_invoice_confirm)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_quotation_item_invoice_confirm).click()

    handles = self.driver.window_handles
    print(homepage_handle)
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item_xo_item)

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo_confirm)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo_confirm).click()


    finalcheck(self)
    return homepage_handle

# 發票轉xo的打印本頁面
def riseinvoice_xo(self):
    global homepage_handle
    # n = self.driver.window_handles  # 获取当前页句柄
    # print(n)
    # self.driver.switch_to.window(n[1])
    # print("3")
    # 获取所有窗口的handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice)

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item)

    homepage_handle = self.driver.window_handles

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo).click()

    handles = self.driver.window_handles
    print(homepage_handle)
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item_xo_item)

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo_confirm)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo_confirm).click()

    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldxo_popsupplier)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldxo_popsupplier))

    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldxo_supplier)))
    cssprojectdavid(self, elementdavid.fieldxo_supplier)

    cssprojectdavid(self, elementdavid.fieldxo_popconsultant)

    cssprojectdavid(self, elementdavid.fieldxo_consultant)


    finalcheck(self)
    return homepage_handle


# xo轉發票的打印本頁面
def risexo_invoice(self):
    global homepage_handle
    # n = self.driver.window_handles  # 获取当前页句柄
    # print(n)
    # self.driver.switch_to.window(n[1])
    # print("3")
    # 获取所有窗口的handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_supplier)
    cssprojectdavid(self, elementdavid.fieldbooking_xo)

    cssprojectdavid(self, elementdavid.fieldbooking_xo_item)

    homepage_handle = self.driver.window_handles

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, elementdavid.fieldbooking_quotation_item_invoice_confirm)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_quotation_item_invoice_confirm).click()

    handles = self.driver.window_handles
    print(homepage_handle)
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item_xo_item)

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo_confirm)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo_confirm).click()

    # 选择客户
    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldinvoice_popcustomer)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldinvoice_popcustomer))

    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.defaultcustomer)))
    cssprojectdavid(self, elementdavid.defaultcustomer)

    finalcheck(self)
    return homepage_handle


# xo轉報價單的打印本頁面
def risexo_quotation(self):
    global homepage_handle
    # n = self.driver.window_handles  # 获取当前页句柄
    # print(n)
    # self.driver.switch_to.window(n[1])
    # print("3")
    # 获取所有窗口的handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_supplier)
    cssprojectdavid(self, elementdavid.fieldbooking_xo)

    cssprojectdavid(self, elementdavid.fieldbooking_xo_item)

    homepage_handle = self.driver.window_handles

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, elementdavid.fieldbooking_xo_item_quotation_confirm)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_xo_item_quotation_confirm).click()

    handles = self.driver.window_handles
    print(homepage_handle)
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item_xo_item)

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo_confirm)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_xo_confirm).click()

    # 选择客户
    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldquotation_popustomer)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldquotation_popustomer))

    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.defaultcustomer)))
    cssprojectdavid(self, elementdavid.defaultcustomer)

    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldphone)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldphone))
    # 18 | type | css=.ant-input-number-input-wrap > #infoForm_Discount | 100
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldphone).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldphone).send_keys(Keys.DELETE)
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldphone).send_keys(elementdavid.textphone)

    finalcheck(self)
    return homepage_handle

#報價單編輯頁面



#發票編輯頁面
def riseinvoice_edit(self):
    global homepage_handle
    # n = self.driver.window_handles  # 获取当前页句柄
    # print(n)
    # self.driver.switch_to.window(n[1])
    # print("3")
    # 获取所有窗口的handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice)

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item)

    homepage_handle = self.driver.window_handles

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_edit)


    handles = self.driver.window_handles
    print(homepage_handle)
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break


    return homepage_handle


#發票從編輯頁面到複製頁面
def riseinvoice_copy(self):
    global homepage_handle
    # n = self.driver.window_handles  # 获取当前页句柄
    # print(n)
    # self.driver.switch_to.window(n[1])
    # print("3")
    # 获取所有窗口的handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_copy)
    cssprojectdavid(self, elementdavid.fieldbooking_invoice_copy_local)
    cssprojectdavid(self, elementdavid.fieldbooking_invoice_copy_confirm)


    homepage_handle = self.driver.window_handles

    handles = self.driver.window_handles
    print(homepage_handle)
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break


    return homepage_handle


#報價單編輯頁面
def risequotation_edit(self):
    global homepage_handle
    # n = self.driver.window_handles  # 获取当前页句柄
    # print(n)
    # self.driver.switch_to.window(n[1])
    # print("3")
    # 获取所有窗口的handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_quotation)

    cssprojectdavid(self, elementdavid.fieldbooking_quotation_item)

    homepage_handle = self.driver.window_handles

    cssprojectdavid(self, elementdavid.fieldbooking_quotation_edit)


    handles = self.driver.window_handles
    print(homepage_handle)
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break


    return homepage_handle


#報價單從編輯頁面到複製頁面
def risequotation_copy(self):
    global homepage_handle
    # n = self.driver.window_handles  # 获取当前页句柄
    # print(n)
    # self.driver.switch_to.window(n[1])
    # print("3")
    # 获取所有窗口的handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_copy)
    cssprojectdavid(self, elementdavid.fieldbooking_invoice_copy_local)
    cssprojectdavid(self, elementdavid.fieldbooking_quotation_copy_confirm)


    homepage_handle = self.driver.window_handles

    handles = self.driver.window_handles
    print(homepage_handle)
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break


    return homepage_handle


# 發票收款的打印本頁面
def riseinvoice_receipt(self):
    global homepage_handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice)

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item)

    homepage_handle = self.driver.window_handles

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_receipt)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_receipt).click()

    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item_receipt_allfare)

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.fieldbooking_invoice_item_receipt_bankchage)))
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_receipt_bankchage).send_keys(Keys.CONTROL,
                                                                                                           "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_receipt_bankchage).send_keys(Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_receipt_bankchage).send_keys(
        elementdavid.textbooking_invoice_item_receipt_bankchage)

    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_receipt_creditchage).send_keys(
        Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_receipt_creditchage).send_keys(
        Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_receipt_creditchage).send_keys(
        elementdavid.textbooking_invoice_item_receipt_creditchage)

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item_receipt_comfirm)
    return homepage_handle

# xo收款的打印本頁面
def risexo_receipt(self):

    global homepage_handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_supplier)
    cssprojectdavid(self, elementdavid.fieldbooking_xo)

    cssprojectdavid(self, elementdavid.fieldbooking_xo_item)

    homepage_handle = self.driver.window_handles

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, elementdavid.fieldbooking_xo_item_receipt)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_xo_item_receipt).click()

    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item_receipt_allfare)

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.fieldbooking_invoice_item_receipt_bankchage)))
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_receipt_bankchage).send_keys(Keys.CONTROL,
                                                                                                           "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_receipt_bankchage).send_keys(Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_receipt_bankchage).send_keys(
        elementdavid.textbooking_invoice_item_receipt_bankchage)

    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_receipt_creditchage).send_keys(
        Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_receipt_creditchage).send_keys(
        Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_receipt_creditchage).send_keys(
        elementdavid.textbooking_invoice_item_receipt_creditchage)

    cssprojectdavid(self, elementdavid.fieldbooking_xo_item_receipt_comfirm)
    return homepage_handle


# 發票退款的打印本頁面
def riseinvoice_refund(self):
    global homepage_handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice)

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item)

    homepage_handle = self.driver.window_handles

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_refund)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_refund).click()

    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.fieldbooking_invoice_item_refund_fare)))
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_fare).send_keys(Keys.CONTROL,
                                                                                                           "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_fare).send_keys(Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_fare).send_keys(
        elementdavid.textbooking_invoice_item_refund_fare)

    # WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
    #     (By.XPATH, elementdavid.fieldbooking_invoice_item_refund_bankchage)))
    # self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_bankchage).send_keys(Keys.CONTROL,
    #                                                                                                        "a")
    # self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_bankchage).send_keys(Keys.DELETE)
    # self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_bankchage).send_keys(
    #     elementdavid.textbooking_invoice_item_refund_bankchage)
    #
    # self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_creditchage).send_keys(
    #     Keys.CONTROL, "a")
    # self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_creditchage).send_keys(
    #     Keys.DELETE)
    # self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_creditchage).send_keys(
    #     elementdavid.textbooking_invoice_item_refund_creditchage)

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item_receipt_comfirm)
    return homepage_handle

# xo退款的打印本頁面
def risexo_refund(self):
    global homepage_handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_supplier)
    cssprojectdavid(self, elementdavid.fieldbooking_xo)

    cssprojectdavid(self, elementdavid.fieldbooking_xo_item)

    homepage_handle = self.driver.window_handles

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, elementdavid.fieldbooking_xo_item_refund)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_xo_item_refund).click()

    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.fieldbooking_invoice_item_refund_fare)))
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_fare).send_keys(Keys.CONTROL,
                                                                                                           "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_fare).send_keys(Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_fare).send_keys(
        elementdavid.textbooking_invoice_item_refund_fare)

    # WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
    #     (By.XPATH, elementdavid.fieldbooking_invoice_item_refund_bankchage)))
    # self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_bankchage).send_keys(Keys.CONTROL,
    #                                                                                                        "a")
    # self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_bankchage).send_keys(Keys.DELETE)
    # self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_bankchage).send_keys(
    #     elementdavid.textbooking_invoice_item_refund_bankchage)
    #
    # self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_creditchage).send_keys(
    #     Keys.CONTROL, "a")
    # self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_creditchage).send_keys(
    #     Keys.DELETE)
    # self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refund_creditchage).send_keys(
    #     elementdavid.textbooking_invoice_item_refund_creditchage)

    cssprojectdavid(self, elementdavid.fieldbooking_xo_item_receipt_comfirm)
    return homepage_handle


#發票的機票項目退款申請
def riseinvoice_refundapplication(self):
    global homepage_handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice)

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item)

    homepage_handle = self.driver.window_handles

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_refundapplication)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_invoice_item_refundapplication).click()

    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item_refundapplication_item)
    time.sleep(1)
    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item_refundapplication_confirm)

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_contactperson)))
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_contactperson).send_keys(Keys.CONTROL,
                                                                                                           "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_contactperson).send_keys(Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_contactperson).send_keys(
        elementdavid.textbooking_invoice_item_refundapplication_contactperson)


    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_phone).send_keys(
        Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_phone).send_keys(
        Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_phone).send_keys(
        elementdavid.textbooking_invoice_item_refundapplication_phone)

    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_calendar).click()

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcalendarmonth)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcalendarmonth).click()
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcalendarday)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcalendarday).click()


    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_remark).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_remark).send_keys(Keys.DELETE)
    pyperclip.copy(elementdavid.textbooking_invoice_item_refundapplication_remark)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_remark).send_keys(Keys.CONTROL,
                                                                                     'v')

    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_description).send_keys(
        Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_description).send_keys(
        Keys.DELETE)
    pyperclip.copy(elementdavid.textbooking_invoice_item_refundapplication_description)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_description).send_keys(
        Keys.CONTROL,
        'v')

    xpathprojectdavid(self, elementdavid.fieldbooking_invoice_item_refundapplication_xo)
    xpathprojectdavid(self, elementdavid.fieldbooking_invoice_item_refundapplication_xo_remark)

    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_xo_remark).send_keys(
        Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_xo_remark).send_keys(
        Keys.DELETE)
    pyperclip.copy(elementdavid.textbooking_invoice_item_refundapplication_xo_remark)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_xo_remark).send_keys(
        Keys.CONTROL,
        'v')

    xpathprojectdavid(self, elementdavid.fieldbooking_invoice_item_refundapplication_submit)
    return homepage_handle


#XO的機票項目退款申請

def risexo_refundapplication(self):
    global homepage_handle
    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_supplier)
    cssprojectdavid(self, elementdavid.fieldbooking_xo)

    cssprojectdavid(self, elementdavid.fieldbooking_xo_item)

    homepage_handle = self.driver.window_handles

    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located(
            (By.CSS_SELECTOR, elementdavid.fieldbooking_xo_item_refundapplication)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldbooking_xo_item_refundapplication).click()

    handles = self.driver.window_handles
    # 循环handles找出新窗口的handle
    for handle in handles:
        for oldhandle in homepage_handle:
            if handle != oldhandle:
                # 激活新窗口
                self.driver.switch_to.window(handle)
                break

    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item_refundapplication_item)
    time.sleep(1)
    cssprojectdavid(self, elementdavid.fieldbooking_invoice_item_refundapplication_confirm)

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_contactperson)))
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_contactperson).send_keys(Keys.CONTROL,
                                                                                                           "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_contactperson).send_keys(Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_contactperson).send_keys(
        elementdavid.textbooking_invoice_item_refundapplication_contactperson)


    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_phone).send_keys(
        Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_phone).send_keys(
        Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_phone).send_keys(
        elementdavid.textbooking_invoice_item_refundapplication_phone)

    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_calendar).click()

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcalendarmonth)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcalendarmonth).click()
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcalendarday)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcalendarday).click()


    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_remark).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_remark).send_keys(Keys.DELETE)
    pyperclip.copy(elementdavid.textbooking_invoice_item_refundapplication_remark)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_remark).send_keys(Keys.CONTROL,
                                                                                     'v')

    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_description).send_keys(
        Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_description).send_keys(
        Keys.DELETE)
    pyperclip.copy(elementdavid.textbooking_invoice_item_refundapplication_description)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_description).send_keys(
        Keys.CONTROL,
        'v')

    xpathprojectdavid(self, elementdavid.fieldbooking_invoice_item_refundapplication_xo)
    xpathprojectdavid(self, elementdavid.fieldbooking_invoice_item_refundapplication_xo_remark)

    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_xo_remark).send_keys(
        Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_xo_remark).send_keys(
        Keys.DELETE)
    pyperclip.copy(elementdavid.textbooking_invoice_item_refundapplication_invoice_remark)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fieldbooking_invoice_item_refundapplication_xo_remark).send_keys(
        Keys.CONTROL,
        'v')

    xpathprojectdavid(self, elementdavid.fieldbooking_invoice_item_refundapplication_submit)
    return homepage_handle

# 发票抬头部分
def riseinvoice(self):
    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, elementdavid.createinvoce)))
    # 創建發票
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.createinvoce).click()
    # WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "infoForm_Fax")))
    # WebDriverWait(self.driver, 30).until(expected_conditions.invisibility_of_element_located((By.ID, "infoForm_Fax")))
    # 选择客户
    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldinvoice_popcustomer)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldinvoice_popcustomer))

    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.defaultcustomer)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.defaultcustomer))

    # 16 | runScript | window.scrollTo(0,405) |
    cssprojectdavid(self, elementdavid.fieldxo_popconsultant)

    cssprojectdavid(self, elementdavid.fieldxo_consultant)



    # 17 | click | css=.ant-input-number-input-wrap > #infoForm_Discount |
    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fielddiscount)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fielddiscount))
    # 18 | type | css=.ant-input-number-input-wrap > #infoForm_Discount | 100
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fielddiscount).send_keys(elementdavid.textdiscount)
    # 19 | click | css=#from\[0\] .ant-select-selection__placeholder |

    cssprojectdavid(self, elementdavid.fieldpaymentmethod)
    xpathprojectdavid(self, elementdavid.fieldpaymentmethoddefault)



    print("发票页头已填完")

#創建報價單
def risequotation(self):
    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, elementdavid.createquotation)))
    # 創建报价单
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.createquotation).click()
    # 选择客户
    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldquotation_popustomer)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldquotation_popustomer))

    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.defaultcustomer)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.defaultcustomer))

    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldphone)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldphone))
    # 18 | type | css=.ant-input-number-input-wrap > #infoForm_Discount | 100
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldphone).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldphone).send_keys(Keys.DELETE)
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldphone).send_keys(elementdavid.textphone)
    # 17 | click | css=.ant-input-number-input-wrap > #infoForm_Discount |
    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fielddiscount)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fielddiscount))
    # 18 | type | css=.ant-input-number-input-wrap > #infoForm_Discount | 100
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fielddiscount).send_keys(elementdavid.textdiscount)
    # 19 | click | css=#from\[0\] .ant-select-selection__placeholder |


    print("报价单页头已填完")


# xo抬头部分
def risexo(self):
    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, elementdavid.createxo)))

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.createxo).click()
    # WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "infoForm_Fax")))
    # WebDriverWait(self.driver, 30).until(expected_conditions.invisibility_of_element_located((By.ID, "infoForm_Fax")))
    # 选择客户
    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldxo_popustomer)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldxo_popustomer))

    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldxo_customer)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldxo_customer))
    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldxo_next)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldxo_next))

    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldxo_popsupplier)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldxo_popsupplier))

    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldxo_supplier)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldxo_supplier))

    cssprojectdavid(self, elementdavid.fieldxo_popconsultant)

    cssprojectdavid(self, elementdavid.fieldxo_consultant)



    WebDriverWaitDavid(self.driver, 30).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fielddiscount)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fielddiscount))
    # 18 | type | css=.ant-input-number-input-wrap > #infoForm_Discount | 100
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fielddiscount).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fielddiscount).send_keys(Keys.DELETE)
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fielddiscount).send_keys(elementdavid.textdiscount)

    cssprojectdavid(self, elementdavid.fieldpaymentmethod)
    xpathprojectdavid(self, elementdavid.fieldpaymentmethoddefault)

    # 19 | click | css=#from\[0\] .ant-select-selection__placeholder |
    print("xo页头已填完")


# 頁頭備註部分
def riseremark(self):
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildrisephone).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildrisephone).send_keys(Keys.DELETE)
    pyperclip.copy(elementdavid.textrisephone)  # 将长文本复制到剪切板
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildrisephone).send_keys(Keys.CONTROL,
                                                                                    'v')

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildrisemobile).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildrisemobile).send_keys(Keys.DELETE)
    pyperclip.copy(elementdavid.textrisemobile)  # 将长文本复制到剪切板
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildrisemobile).send_keys(Keys.CONTROL,
                                                                                     'v')

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildrisefax).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildrisefax).send_keys(Keys.DELETE)
    pyperclip.copy(elementdavid.textrisefax)  # 将长文本复制到剪切板
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildrisefax).send_keys(Keys.CONTROL,
                                                                                  'v')

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildriseEmail).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildriseEmail).send_keys(Keys.DELETE)
    pyperclip.copy(elementdavid.textriseEmail)  # 将长文本复制到剪切板
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildriseEmail).send_keys(Keys.CONTROL,
                                                                                    'v')

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildriseprovince).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildriseprovince).send_keys(Keys.DELETE)
    pyperclip.copy(elementdavid.textriseprovince)  # 将长文本复制到剪切板
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildriseprovince).send_keys(Keys.CONTROL,
                                                                                       'v')

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildrisecity).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildrisecity).send_keys(Keys.DELETE)
    pyperclip.copy(elementdavid.textrisecity)  # 将长文本复制到剪切板
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildrisecity).send_keys(Keys.CONTROL,
                                                                                   'v')

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildriseaddress).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildriseaddress).send_keys(Keys.DELETE)
    pyperclip.copy(elementdavid.textriseaddress)  # 将长文本复制到剪切板
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fildriseaddress).send_keys(Keys.CONTROL,
                                                                                      'v')

    self.driver.find_element(By.XPATH, elementdavid.fildriseremark).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fildriseremark).send_keys(Keys.DELETE)
    pyperclip.copy(elementdavid.textriseremark)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fildriseremark).send_keys(Keys.CONTROL,
                                                                              'v')

    self.driver.find_element(By.XPATH, elementdavid.fildriseremark1).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fildriseremark1).send_keys(Keys.DELETE)
    pyperclip.copy(elementdavid.textriseremark1)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fildriseremark1).send_keys(Keys.CONTROL,
                                                                               'v')

    self.driver.find_element(By.XPATH, elementdavid.fildriseremark2).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fildriseremark2).send_keys(Keys.DELETE)
    pyperclip.copy(elementdavid.textriseremark2)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fildriseremark2).send_keys(Keys.CONTROL,
                                                                               'v')

    self.driver.find_element(By.XPATH, elementdavid.fildriseremark3).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fildriseremark3).send_keys(Keys.DELETE)
    pyperclip.copy(elementdavid.textriseremark3)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fildriseremark3).send_keys(Keys.CONTROL,
                                                                               'v')
    print("頁頭信息已填完")


# api机票部分
def apiticket(self):
    # 選擇api機票項目
    # 輸入去程
    # WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
    #     (By.CSS_SELECTOR, elementdavid.fieldtrip)))
    # self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldtrip).click()
    cssprojectdavid(self, elementdavid.fieldtrip)
    # 20 | type | css=#from\[0\] .ant-select-search__field | tpe
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.searchtrip).send_keys(elementdavid.texttrip)
    # 22 | click | css=.ant-select-dropdown-menu-item |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.defaulttrip)))
    self.driver.find_element(By.XPATH, elementdavid.defaulttrip).click()
    # 輸入回程
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldreturn).click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.searchreturn).send_keys(elementdavid.textreturn)
    # 21 | pause | 1000 | 1000
    # 22 | click | css=.ant-select-dropdown-menu-item |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.defaultreturn)))
    while True:
        try:
            self.driver.find_element(By.XPATH, elementdavid.defaultreturn).click()
            break
        except:
            time.sleep(1)
            continue
    time.sleep(1)
    # 27 | click | css=#fromCityDate\[0\] .ant-calendar-picker-input |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcalendar).click()
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcalendarmonth)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcalendarmonth).click()
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcalendarday)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcalendarday).click()
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldroute_search).click()
    # 31 | click | css=.item-v1:nth-child(1) .ant-btn |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.defaultroute1)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.defaultroute1).click()
    # 32 | click | css=.item-v1:nth-child(2) .ant-btn |

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.defaultroute2).click()
    print("已选完俩个api搜索机票行程")


# 手输机票部分
def handticket1(self):
    # 選擇手動機票項目
    cssprojectdavid(self, elementdavid.fieldhandticket)
    # self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhandticket).click()
    # 34 | click | css=.ant-col:nth-child(2) > .ant-btn:nth-child(1) |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldfetchpnr)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldfetchpnr).click()
    # 35 | click | css=.body-content-1 > .ant-input |

    # 输入第一个pnr文本
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcontentpnr)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcontentpnr).click()
    pyperclip.copy(elementdavid.textcontentpnr1)  # 将长文本复制到剪切板
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcontentpnr).send_keys(Keys.CONTROL,
                                                                                      'v')
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldnextpnr1).click()

    cssprojectdavid(self, elementdavid.fieldtickettype1)

    # 39 | click | css=.action-button > .ant-btn:nth-child(2) |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldnextpnr2)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldnextpnr2).click()
    #40 | click | css=.customFlightFeeSet > .ant-checkbox-wrapper:nth-child(1) > span:nth-child(2) |




    # 41 | click | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[2]/input |

    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_invoice).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_invoice).send_keys(Keys.DELETE)
    # 42 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_invoice).send_keys(
        elementdavid.textbasicfare_invoice1)
    # 43 | click | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[4]/div[2]/div[2]/input |
    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_xo).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_xo).send_keys(Keys.DELETE)
    # 44 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[6]/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_xo).send_keys(elementdavid.textbasicfare_xo1)
    # 45 | click | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[6]/div[2]/div[2]/input |
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_invoice).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_invoice).send_keys(Keys.DELETE)
    # 46 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[4]/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_invoice).send_keys(
        elementdavid.texttickettax_invoice1)
    # 47 | click | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[9]/div[2]/div[2]/input |
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_xo).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_xo).send_keys(Keys.DELETE)
    # 48 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[9]/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_xo).send_keys(elementdavid.texttickettax_xo1)
    # 50 | click | css=.custom-flight-btn > .ant-btn |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhandticketsubmit).click()
    print("已成功添加第一个手入机票")


# 手输机票部分
def handticket2(self):
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldfetchpnr).click()
    # 35 | click | css=.body-content-1 > .ant-input |
    # 输入第二个文本
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcontentpnr)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcontentpnr).click()
    pyperclip.copy(elementdavid.textcontentpnr2)  # 将长文本复制到剪切板
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcontentpnr).send_keys(Keys.CONTROL,
                                                                                      'v')
    # 38 | click | css=.ture-page-button > .ant-btn:nth-child(2) |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldnextpnr1).click()
    # 39 | click | css=.action-button > .ant-btn:nth-child(2) |
    cssprojectdavid(self, elementdavid.fieldtickettype1)

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldnextpnr2)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldnextpnr2).click()
    # 40 | click | css=.customFlightFeeSet > .ant-checkbox-wrapper:nth-child(1) > span:nth-child(2) |

    # 41 | click | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[2]/input |

    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_invoice).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_invoice).send_keys(Keys.DELETE)
    # 42 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_invoice).send_keys(
        elementdavid.textbasicfare_invoice2)
    # 43 | click | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[4]/div[2]/div[2]/input |
    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_xo).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_xo).send_keys(Keys.DELETE)
    # 44 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[6]/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_xo).send_keys(elementdavid.textbasicfare_xo2)
    # 45 | click | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[6]/div[2]/div[2]/input |
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_invoice).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_invoice).send_keys(Keys.DELETE)
    # 46 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[4]/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_invoice).send_keys(
        elementdavid.texttickettax_invoice2)
    # 47 | click | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[9]/div[2]/div[2]/input |
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_xo).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_xo).send_keys(Keys.DELETE)
    # 48 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[9]/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_xo).send_keys(elementdavid.texttickettax_xo2)
    # 50 | click | css=.custom-flight-btn > .ant-btn |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhandticketsubmit).click()
    print("已成功添加第二个手入机票")


# 手输api机票部分
def handapiticket1(self):
    # 選擇手動機票項目
    cssprojectdavid(self, elementdavid.fieldhandticket)
    # self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhandticket).click()
    # 34 | click | css=.ant-col:nth-child(2) > .ant-btn:nth-child(1) |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldfetchpnr)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldfetchpnr).click()
    # 35 | click | css=.body-content-1 > .ant-input |
    cssprojectdavid(self, elementdavid.fieldhandapiticket)
    # 输入第一个pnr文本
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcontentpnr)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcontentpnr).click()
    pyperclip.copy(elementdavid.textcontentapipnr1)  # 将长文本复制到剪切板
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcontentpnr).send_keys(Keys.CONTROL,
                                                                                      'v')
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldnextpnr1).click()

    # cssprojectdavid(self, elementdavid.fieldtickettype1)

    # 39 | click | css=.action-button > .ant-btn:nth-child(2) |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldnextapipnr2)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldnextapipnr2).click()
    #40 | click | css=.customFlightFeeSet > .ant-checkbox-wrapper:nth-child(1) > span:nth-child(2) |




    # 41 | click | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[2]/input |

    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_invoice).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_invoice).send_keys(Keys.DELETE)
    # 42 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_invoice).send_keys(
        elementdavid.textbasicfare_invoice1)
    # 43 | click | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[4]/div[2]/div[2]/input |
    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_xo).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_xo).send_keys(Keys.DELETE)
    # 44 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[6]/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldbasicfare_xo).send_keys(elementdavid.textbasicfare_xo1)
    # 45 | click | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[6]/div[2]/div[2]/input |
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_invoice).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_invoice).send_keys(Keys.DELETE)
    # 46 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[4]/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_invoice).send_keys(
        elementdavid.texttickettax_invoice1)
    # 47 | click | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[9]/div[2]/div[2]/input |
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_xo).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_xo).send_keys(Keys.DELETE)
    # 48 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[9]/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldtickettax_xo).send_keys(elementdavid.texttickettax_xo1)
    # 50 | click | css=.custom-flight-btn > .ant-btn |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhandticketsubmit).click()
    print("已成功添加第一个手入机票")



# 酒店部分
def handhotel1(self):
    # 酒店项目
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhotel).click()
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldhotelcontent)))
    # 第一个酒店
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhotelcontent).click()
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldhotel_search)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhotel_search).send_keys(
        elementdavid.texthotel_search1)
    self.driver.find_element(By.ID, elementdavid.fieldhotelcity).click()

    self.driver.find_element(By.ID, elementdavid.fieldhotelcity).send_keys(elementdavid.texthotelcity1)

    self.driver.find_element(By.ID, elementdavid.fieldhotelcountry).click()

    self.driver.find_element(By.ID, elementdavid.fieldhotelcountry).send_keys(elementdavid.texthotelcountry1)

    self.driver.find_element(By.ID, elementdavid.fieldhotelpropertytype).click()

    self.driver.find_element(By.ID, elementdavid.fieldhotelpropertytype).send_keys(elementdavid.texthotelpropertytype1)

    self.driver.find_element(By.ID, elementdavid.fieldhotelroomplan).click()

    self.driver.find_element(By.ID, elementdavid.fieldhotelroomplan).send_keys(elementdavid.texthotelroomplan1)

    self.driver.find_element(By.ID, elementdavid.fieldhotelspecial).click()

    self.driver.find_element(By.ID, elementdavid.fieldhotelspecial).send_keys(elementdavid.texthotelspecial1)

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhoteltype1).click()

    # 84 | click | css=#CheckInDate .ant-calendar-picker-input |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhotelcalendar).click()

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcalendarmonth)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcalendarmonth).click()

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcalendarday)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcalendarday).click()
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.fieldhotelroomtype)))

    while True:
        try:
            self.driver.find_element(By.XPATH, elementdavid.fieldhotelroomtype).click()
            WebDriverWaitDavid(self.driver, 1).untilmyself(expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, elementdavid.fieldhotelroomtypedefault)))
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                         elementdavid.fieldhotelroomtypedefault))
            break
        except:
            time.sleep(0.5)
            continue

    # self.driver.find_element(By.XPATH, elementdavid.fieldhotelroomtype).click()
    # # 88 | pause | 1000 | 1000
    # time.sleep(1)
    # # 89 | click | css=.ant-select-dropdown-menu-item-active |
    # WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
    #     (By.CSS_SELECTOR, elementdavid.fieldhotelroomtypedefault)))

    # self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
    #                                                                              elementdavid.fieldhotelroomtypedefault))
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.fieldhotelfare_invoice)))
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_invoice).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_invoice).send_keys(Keys.DELETE)
    # 42 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_invoice).send_keys(
        elementdavid.texthotelfare_invoice1)
    # 43 | click | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[4]/div[2]/div[2]/input |
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_xo).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_xo).send_keys(Keys.DELETE)
    # 44 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[6]/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_xo).send_keys(elementdavid.texthotelfare_xo1)
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_unit).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_unit).send_keys(Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_unit).send_keys(elementdavid.texthotelfare_unit1)

    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_remark).click()
    pyperclip.copy(elementdavid.texthotelfare_remark1)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_remark).send_keys(Keys.CONTROL,
                                                                                     'v')

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhoteladd).click()
    print("已成功添加第一个手入酒店")


# 酒店部分
def handhotel2(self):
    # 第二个酒店
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhotel).click()
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldhotelcontent)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhotelcontent).click()
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldhotel_search)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhotel_search).send_keys(
        elementdavid.texthotel_search2)
    self.driver.find_element(By.ID, elementdavid.fieldhotelcity).click()

    self.driver.find_element(By.ID, elementdavid.fieldhotelcity).send_keys(elementdavid.texthotelcity2)

    self.driver.find_element(By.ID, elementdavid.fieldhotelcountry).click()

    self.driver.find_element(By.ID, elementdavid.fieldhotelcountry).send_keys(elementdavid.texthotelcountry2)

    self.driver.find_element(By.ID, elementdavid.fieldhotelpropertytype).click()

    self.driver.find_element(By.ID, elementdavid.fieldhotelpropertytype).send_keys(elementdavid.texthotelpropertytype2)

    self.driver.find_element(By.ID, elementdavid.fieldhotelroomplan).click()

    self.driver.find_element(By.ID, elementdavid.fieldhotelroomplan).send_keys(elementdavid.texthotelroomplan2)

    self.driver.find_element(By.ID, elementdavid.fieldhotelspecial).click()

    self.driver.find_element(By.ID, elementdavid.fieldhotelspecial).send_keys(elementdavid.texthotelspecial2)

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhoteltype1).click()
    # 84 | click | css=#CheckInDate .ant-calendar-picker-input |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhotelcalendar).click()

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcalendarmonth)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcalendarmonth).click()

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcalendarday)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldcalendarday).click()

    while True:
        try:
            self.driver.find_element(By.XPATH, elementdavid.fieldhotelroomtype).click()
            WebDriverWaitDavid(self.driver, 1).untilmyself(expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, elementdavid.fieldhotelroomtypedefault)))
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                         elementdavid.fieldhotelroomtypedefault))
            break
        except:
            time.sleep(0.5)
            continue
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.fieldhotelfare_invoice)))
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_invoice).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_invoice).send_keys(Keys.DELETE)
    # 42 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_invoice).send_keys(
        elementdavid.texthotelfare_invoice2)
    # 43 | click | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[4]/div[2]/div[2]/input |
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_xo).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_xo).send_keys(Keys.DELETE)
    # 44 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[6]/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_xo).send_keys(elementdavid.texthotelfare_xo2)
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_unit).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_unit).send_keys(Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_unit).send_keys(elementdavid.texthotelfare_unit2)

    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_remark).click()
    pyperclip.copy(elementdavid.texthotelfare_remark2)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fieldhotelfare_remark).send_keys(Keys.CONTROL,
                                                                                     'v')

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldhoteladd).click()
    print("已成功添加第二个手入酒店")


# 其他费用部分
def othercharge1(self):
    # 選擇其他費用
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fielddaytour)))

    while True:
        try:
            self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldothercharge).click()
            break
        except:
            time.sleep(1)
            continue

    # 117 | click | css=.select-has-search-icon .ant-select-selection__placeholder |

    # WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
    #     (By.XPATH, elementdavid.fieldotherchargecontent)))
    #
    # self.driver.find_element(By.XPATH, elementdavid.fieldotherchargecontent).click()

    xpathprojectdavid(self, elementdavid.fieldotherchargecontent)

    # 118 | click | xpath=//li[contains(.,'Fare Services:機票服務')] |
    xpathprojectdavid(self, elementdavid.fieldotherchargeitem1)
    # cssprojectdavid(self, elementdavid.fieldotherchargeitem1)


    # WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
    #     (By.XPATH, elementdavid.fieldotherchargeitem1)))
    # self.driver.find_element(By.XPATH, elementdavid.fieldotherchargeitem1).click()

    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_invoice).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_invoice).send_keys(Keys.DELETE)
    # 42 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_invoice).send_keys(
        elementdavid.textothercharge_invoice1)
    # 43 | click | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[4]/div[2]/div[2]/input |
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_xo).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_xo).send_keys(Keys.DELETE)
    # 44 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[6]/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_xo).send_keys(elementdavid.textothercharge_xo1)
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_unit).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_unit).send_keys(Keys.DELETE)
    # 44 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[6]/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_unit).send_keys(elementdavid.textothercharge_unit1)

    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_remark).click()
    pyperclip.copy(elementdavid.textothercharge_remark1)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_remark).send_keys(Keys.CONTROL,
                                                                                       'v')

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldotherchargeadd).click()
    print("已成功添加第一个其他费用")


# 其他费用部分
def othercharge2(self):
    # 選擇其他費用

    # self.driver.find_element(By.XPATH, elementdavid.fieldotherchargecontent).click()
    xpathprojectdavid(self, elementdavid.fieldotherchargecontent)

    # 118 | click | xpath=//li[contains(.,'Fare Services:機票服務')] |
    # WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
    #     (By.XPATH, elementdavid.fieldotherchargeitem2)))
    # self.driver.find_element(By.XPATH, elementdavid.fieldotherchargeitem2).click()
    xpathprojectdavid(self, elementdavid.fieldotherchargeitem2)

    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_invoice).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_invoice).send_keys(Keys.DELETE)
    # 42 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_invoice).send_keys(
        elementdavid.textothercharge_invoice2)
    # 43 | click | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[4]/div[2]/div[2]/input |
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_xo).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_xo).send_keys(Keys.DELETE)
    # 44 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[6]/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_xo).send_keys(elementdavid.textothercharge_xo2)
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_unit).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_unit).send_keys(Keys.DELETE)
    # 44 | type | xpath=//div[@id='content']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[6]/div[2]/div[2]/input | 300.00
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_unit).send_keys(elementdavid.textothercharge_unit2)
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_remark).click()
    pyperclip.copy(elementdavid.textothercharge_remark2)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fieldothercharge_remark).send_keys(Keys.CONTROL,
                                                                                       'v')

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldotherchargeadd).click()
    print("已成功添加第二个其他费用")


# 添加一日游项目
def daytour1(self):
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fielddaytour)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fielddaytour))
    # 132 | click | css=.ant-row-flex .ant-row .PopoverSearchTable > .ant-input |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fielddaytourcontent)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fielddaytourcontent).click()
    # 133 | click | css=.ant-table-row:nth-child(1) > .ant-table-column-has-actions:nth-child(2) |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fielddaytouritem1)))
    while True:
        try:
            self.driver.find_element(By.CSS_SELECTOR,
                                     elementdavid.fielddaytouritem1).click()
            break
        except:
            time.sleep(1)
            continue
    # 134 | click | css=#StartDate .ant-calendar-picker-input |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fielddaytourcalendar)))
    while True:
        try:
            self.driver.find_element(By.CSS_SELECTOR, elementdavid.fielddaytourcalendar).click()
            break
        except:
            time.sleep(1)
            continue
    # self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
    #                                                                              elementdavid.fielddaytourcalendar))
    # 135 | click | css=.ant-calendar-next-month-btn |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcalendarmonth)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldcalendarmonth))

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcalendarday)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldcalendarday))
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.fielddaytour_invoice)))
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_invoice).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_invoice).send_keys(Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_invoice).send_keys(
        elementdavid.textdaytour_invoice1)
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_xo).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_xo).send_keys(Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_xo).send_keys(elementdavid.textdaytour_xo1)
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_unit).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_unit).send_keys(Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_unit).send_keys(elementdavid.textdaytour_unit1)

    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_remark).click()
    pyperclip.copy(elementdavid.textdaytour_remark1)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_remark).send_keys(Keys.CONTROL,
                                                                                   'v')
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_itemremark).click()
    pyperclip.copy(elementdavid.textdaytour_itemremark1)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_itemremark).send_keys(Keys.CONTROL,
                                                                                       'v')
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fielddaytouradd).click()
    print("已成功添加第一个一日游")


# 添加一日游项目
def daytour2(self):
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fielddaytourcontent)))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fielddaytourcontent).click()
    # 133 | click | css=.ant-table-row:nth-child(1) > .ant-table-column-has-actions:nth-child(2) |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fielddaytouritem2)))
    while True:
        try:
            self.driver.find_element(By.CSS_SELECTOR,
                                     elementdavid.fielddaytouritem2).click()
            break
        except:
            time.sleep(1)
            continue

    # 134 | click | css=#StartDate .ant-calendar-picker-input |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fielddaytourcalendar)))
    while True:
        try:
            self.driver.find_element(By.CSS_SELECTOR, elementdavid.fielddaytourcalendar).click()
            break
        except:
            time.sleep(1)
            continue
    # 135 | click | css=.ant-calendar-next-month-btn |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcalendarmonth)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldcalendarmonth))

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldcalendarday)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldcalendarday))
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.fielddaytour_invoice)))
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_invoice).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_invoice).send_keys(Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_invoice).send_keys(
        elementdavid.textdaytour_invoice2)
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_xo).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_xo).send_keys(Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_xo).send_keys(elementdavid.textdaytour_xo2)
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_unit).send_keys(Keys.CONTROL, "a")
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_unit).send_keys(Keys.DELETE)
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_unit).send_keys(elementdavid.textdaytour_unit2)
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_remark).click()
    pyperclip.copy(elementdavid.textdaytour_remark2)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_remark).send_keys(Keys.CONTROL,
                                                                                   'v')
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_itemremark).click()
    pyperclip.copy(elementdavid.textdaytour_itemremark2)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fielddaytour_itemremark).send_keys(Keys.CONTROL,
                                                                                       'v')
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fielddaytouradd).click()
    print("已成功添加第二个一日游")


# 发票下一页
def nextpage(self):
    print("创建页面显示", self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldfinalamount).text)
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.shoppingcart).click()
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.nextpage)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.nextpage))
    print("已成功进入下一页")
    WebDriverWaitDavid(self.driver, 400).untilmyself((expected_conditions.presence_of_element_located(
        (By.CSS_SELECTOR, elementdavid.fieldfinalamount))))
    while True:
        try:
            print("下一页初步显示", self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldfinalamount).text)
            break
        except:
            time.sleep(1)
            continue


# 突然想再添加額外的項目
def nextpageadditem(self):
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.fildnextpageadditem)))
    while True:
        try:
            self.driver.find_element(By.XPATH, elementdavid.fildnextpageadditem).click()
            break
        except:
            time.sleep(1)
            continue

    # self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,
    #                                                                              elementdavid.fildnextpageadditem))
    # # 158 | click | css=.add-icon > svg |
    # WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
    #     (By.XPATH, elementdavid.fildnextpageadditem)))
    print("添加新項目頁面")


# 团
def group1(self):
    # 創建團
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.fieldgroup)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,
                                                                                 elementdavid.fieldgroup))
    # 158 | click | css=.add-icon > svg |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldgroupadd)))

    while True:
        try:
            self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupadd).click()
            break
        except:
            time.sleep(1)
            continue

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldgroupcontent1)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldgroupcontent1))
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldgroupdefault1)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldgroupdefault1))
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldgroupname1)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldgroupname1))
    # 167 | type | css=.line-2 > .item-box:nth-child(1) > .ant-input | 團
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupname1).send_keys(elementdavid.textgroupname1)
    # 168 | click | css=.line-2 > .item-box:nth-child(2) > .ant-input |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupcontacts1).click()
    # 169 | type | css=.line-2 > .item-box:nth-child(2) > .ant-input | david
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupcontacts1).send_keys(
        elementdavid.textgroupcontacts1)
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupautofare1).click()

    self.driver.find_element(By.XPATH, elementdavid.fieldgroupdescription).click()
    pyperclip.copy(elementdavid.textgroupdescription1)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fieldgroupdescription).send_keys(Keys.CONTROL,
                                                                                     'v')
    self.driver.find_element(By.XPATH, elementdavid.fieldgroupremark).click()
    pyperclip.copy(elementdavid.textgroupremark1)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fieldgroupremark).send_keys(Keys.CONTROL,
                                                                                'v')

    print("已成功创建一个团，只包含第一个项目")
    WebDriverWaitDavid(self.driver, 400).untilmyself((expected_conditions.presence_of_element_located(
        (By.CSS_SELECTOR, elementdavid.fieldfinalamount))))
    print("添加完团后的金额显示", self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldfinalamount).text)


# 团
def group13579(self):
    # 創建團
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.fieldgroup)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,
                                                                                 elementdavid.fieldgroup))

    # 158 | click | css=.add-icon > svg |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldgroupadd)))

    # self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupadd))
    while True:
        try:
            self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupadd).click()
            break
        except:
            time.sleep(1)
            continue

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldgroupcontent1)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldgroupcontent1))
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldgroupdefault1)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldgroupdefault1))

    # 160 | click | css=.ant-select-dropdown-menu-item-active |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupitem3).click()
    # 161 | click | css=.ant-select-dropdown-menu-item:nth-child(3) |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupitem5).click()
    # 162 | click | css=.ant-select-dropdown-menu-item:nth-child(5) |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupitem7).click()
    # 163 | click | css=.ant-select-dropdown-menu-item:nth-child(7) |

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupitem9).click()

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldgroupname1)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldgroupname1))
    # 167 | type | css=.line-2 > .item-box:nth-child(1) > .ant-input | 團
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupname1).send_keys(elementdavid.textgroupname1)
    # 168 | click | css=.line-2 > .item-box:nth-child(2) > .ant-input |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupcontacts1).click()
    # 169 | type | css=.line-2 > .item-box:nth-child(2) > .ant-input | david
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupcontacts1).send_keys(
        elementdavid.textgroupcontacts1)

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupautofare1).click()
    self.driver.find_element(By.XPATH, elementdavid.fieldgroupdescription).click()
    pyperclip.copy(elementdavid.textgroupdescription1)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fieldgroupdescription).send_keys(Keys.CONTROL,
                                                                                     'v')
    self.driver.find_element(By.XPATH, elementdavid.fieldgroupremark).click()
    pyperclip.copy(elementdavid.textgroupremark1)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fieldgroupremark).send_keys(Keys.CONTROL,
                                                                                'v')
    print("已成功创建一个团，只包含排序第一、三、五、七、九的项目")
    WebDriverWaitDavid(self.driver, 400).untilmyself((expected_conditions.presence_of_element_located(
        (By.CSS_SELECTOR, elementdavid.fieldfinalamount))))
    print("添加完团后的金额显示", self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldfinalamount).text)


# 添加第二个团，还未测试过
def group2(self):
    # 还没有测试通过
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldgroupadd)))

    # self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupadd))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupadd).click()

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.XPATH, elementdavid.fieldgroupcontent2)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,
                                                                                 elementdavid.fieldgroupcontent2))
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldgroupitem2)))
    # self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
    #                                                                              elementdavid.fieldgroupitem1))
    #
    # # 160 | click | css=.ant-select-dropdown-menu-item-active |
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupdefault1).click()
    # self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupitem3).click()
    # # 161 | click | css=.ant-select-dropdown-menu-item:nth-child(3) |
    # self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupitem5).click()
    # # 162 | click | css=.ant-select-dropdown-menu-item:nth-child(5) |
    # self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupitem7).click()
    # # 163 | click | css=.ant-select-dropdown-menu-item:nth-child(7) |
    # self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupitem9).click()

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldgroupname2)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldgroupname2))
    # 167 | type | css=.line-2 > .item-box:nth-child(1) > .ant-input | 團
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupname2).send_keys(elementdavid.textgroupname2)
    # 168 | click | css=.line-2 > .item-box:nth-child(2) > .ant-input |
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldgroupcontacts2)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldgroupcontacts2))
    # 169 | type | css=.line-2 > .item-box:nth-child(2) > .ant-input | david
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupcontacts2).send_keys(
        elementdavid.textgroupcontacts2)

    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldgroupautofare2).click()
    self.driver.find_element(By.XPATH, elementdavid.fieldgroupdescription).click()
    pyperclip.copy(elementdavid.textgroupdescription1)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fieldgroupdescription).send_keys(Keys.CONTROL,
                                                                                     'v')
    self.driver.find_element(By.XPATH, elementdavid.fieldgroupremark).click()
    pyperclip.copy(elementdavid.textgroupremark1)  # 将长文本复制到剪切板
    self.driver.find_element(By.XPATH, elementdavid.fieldgroupremark).send_keys(Keys.CONTROL,
                                                                                'v')
    print("已成功创建二个团，只包含第二个项目")
    WebDriverWaitDavid(self.driver, 400).untilmyself((expected_conditions.presence_of_element_located(
        (By.CSS_SELECTOR, elementdavid.fieldfinalamount))))
    print("添加完团后的金额显示", self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldfinalamount).text)


# 还剩勾选乘客问题
def passenger1(self):
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldpassenger)))
    while True:
        try:
            self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldpassenger).click()
            break
        except:
            time.sleep(1)
            continue

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldpassengerfirstname)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldpassengerfirstname))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldpassengerfirstname).send_keys(
        elementdavid.textpassengerfirstname1)
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldpassengersecondname)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldpassengersecondname))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldpassengersecondname).send_keys(
        elementdavid.textpassengersecondname1)
    cssprojectdavid(self, elementdavid.fieldpassengeradd)
    # 默认会报错，先不处理
    # WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
    #     (By.XPATH, elementdavid.fieldpassengerdefault)))
    # self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,
    #                                                                              elementdavid.fieldpassengerdefault))
    print("已成功添加機票乘客")


def passenger2(self):
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldpassenger)))
    while True:
        try:
            self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldpassenger).click()
            break
        except:
            time.sleep(1)
            continue

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldpassengerfirstname)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldpassengerfirstname))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldpassengerfirstname).send_keys(
        elementdavid.textpassengerfirstname2)
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldpassengersecondname)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldpassengersecondname))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldpassengersecondname).send_keys(
        elementdavid.textpassengersecondname2)
    cssprojectdavid(self, elementdavid.fieldpassengeradd)
    # 默认会报错，先不处理
    # WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
    #     (By.XPATH, elementdavid.fieldpassengerdefault)))
    # self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,
    #                                                                              elementdavid.fieldpassengerdefault))
    print("已成功添加酒店乘客")


def passenger3(self):
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldpassenger)))
    while True:
        try:
            self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldpassenger).click()
            break
        except:
            time.sleep(1)
            continue

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldpassengerfirstname)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldpassengerfirstname))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldpassengerfirstname).send_keys(
        elementdavid.textpassengerfirstname3)
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldpassengersecondname)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldpassengersecondname))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldpassengersecondname).send_keys(
        elementdavid.textpassengersecondname3)
    cssprojectdavid(self, elementdavid.fieldpassengeradd)
    # 默认会报错，先不处理
    # WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
    #     (By.XPATH, elementdavid.fieldpassengerdefault)))
    # self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,
    #                                                                              elementdavid.fieldpassengerdefault))
    print("已成功添加其他費用乘客")


def passenger4(self):
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldpassenger)))
    while True:
        try:
            self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldpassenger).click()
            break
        except:
            time.sleep(1)
            continue

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldpassengerfirstname)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldpassengerfirstname))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldpassengerfirstname).send_keys(
        elementdavid.textpassengerfirstname4)
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldpassengersecondname)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldpassengersecondname))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldpassengersecondname).send_keys(
        elementdavid.textpassengersecondname4)
    cssprojectdavid(self, elementdavid.fieldpassengeradd)

    # 默认会报错，先不处理
    # WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
    #     (By.XPATH, elementdavid.fieldpassengerdefault)))
    # self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,
    #                                                                              elementdavid.fieldpassengerdefault))
    print("已成功添加一日遊乘客")


def passenger5(self):
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldpassenger)))
    while True:
        try:
            self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldpassenger).click()
            break
        except:
            time.sleep(1)
            continue

    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldpassengerfirstname)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldpassengerfirstname))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldpassengerfirstname).send_keys(
        elementdavid.textpassengerfirstname5)
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldpassengersecondname)))
    self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
                                                                                 elementdavid.fieldpassengersecondname))
    self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldpassengersecondname).send_keys(
        elementdavid.textpassengersecondname5)
    cssprojectdavid(self, elementdavid.fieldpassengeradd)
    # 默认会报错，先不处理
    # WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
    #     (By.XPATH, elementdavid.fieldpassengerdefault)))
    # self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH,
    #                                                                              elementdavid.fieldpassengerdefault))
    print("已成功添加團乘客")


def passengerall(self):
    passenger1(self)
    passenger2(self)
    passenger3(self)
    passenger4(self)
    passenger5(self)


def finalcheck(self):
    WebDriverWaitDavid(self.driver, 400).untilmyself((expected_conditions.presence_of_element_located(
        (By.CSS_SELECTOR, elementdavid.fieldfinalamount))))
    time.sleep(1)
    print("最后提交订单前显示", self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldfinalamount).text)
    WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, elementdavid.fieldfinalcheck)))
    while True:
        try:
            self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldfinalcheck).click()
            break
        except:
            time.sleep(1)
            continue
    # self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR,
    #                                                                              elementdavid.fieldfinalcheck))
    # self.driver.find_element(By.CSS_SELECTOR, elementdavid.fieldfinalcheck).click()

    # WebDriverWaitDavid(self.driver, 400).untilmyself(expected_conditions.element_to_be_clickable(
    #     (By.XPATH, elementdavid.fieldfinalcheck)))
    # self.driver.find_element(By.XPATH, elementdavid.fieldfinalcheck).click()

    print("已成功创建一个订单")
