# Generated by Selenium IDE
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
import projectdavid
import pyperclip

class Test():
  def setup_method(self, method):
    # desired_capabilities = DesiredCapabilities.CHROME
    # desired_capabilities["pageLoadStrategy"] = "eager"
    self.driver = webdriver.Chrome()

    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def david(self):
    # elementdavid.web = "https://system.tripo.ai/#/login"
    # elementdavid.web = "http://tripo.staging.travelconnect.co/#/login"
    # elementdavid.textaccount = "test@travelconnect.co"
    # elementdavid.textpassword = "123456789"
    # elementdavid.textcompanycode = "TC0186"
    projectdavid.login(self)
    projectdavid.risebooking(self)
    projectdavid.risexo_invoice(self)
    projectdavid.printout_booking(self)
    projectdavid.risexo_quotation(self)
    projectdavid.printout_booking(self)
    projectdavid.risexo_refundapplication(self)
    projectdavid.printout_booking(self)
    projectdavid.risexo_receipt(self)
    projectdavid.printout_booking(self)
    projectdavid.risexo_refund(self)
    projectdavid.printout_booking(self)

    # projectdavid.inputwaiting(self)






  
if __name__ == '__main__':
  test = Test()
  test.setup_method(0)
  test.david()
  # print("输入内容进行关闭 ", input("请输入："))
  # test.teardown_method()