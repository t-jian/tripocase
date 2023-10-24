# testSearchPage.py代码如下

# _*_ coding:utf-8 _*_

__author__ = 'david'

import unittest
import sys
import pytest
import os
import allure
import pytest

from selenium import webdriver
from Tripo.Tripo_Web.pages.LoginPage import LoginPage
from Tripo.Tripo_Web.pages.data import *
import logging
logger = logging.getLogger(__name__)

class TestLogin:
    # @pytest.mark.parametrize("no,username,password,code,msg", read_xlsx("../datas/login.xlsx"))
    # @pytest.mark.parametrize("no,username,password,code,msg", read_xlsx(r"D:\Learn\PYTHON\GitTest\tripo-test\Tripo\Tripo_Web\datas\login.xlsx"))
    @pytest.mark.parametrize("caseinfo", read_testcase("test_case", "\datas\login.yaml"))
    def test_login(self, driver, caseinfo):
        logger.info("开始执行用例")
        allure.attach(driver.get_screenshot_as_png(), '开始执行用例')
        login1 = LoginPage(driver)
        driver.get(login1.url)
        login1.login(caseinfo["login"]["textaccount"], caseinfo["login"]["textpassword"], caseinfo["login"]["textcompanycode"])
        # msg =
        # assert sys_msg == msg
        logger.info("测试通过")
        allure.attach(driver.get_screenshot_as_png(), '用例后')

