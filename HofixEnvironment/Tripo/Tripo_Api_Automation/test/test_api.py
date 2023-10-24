# -*- coding: UTF-8 -*-

import requests
import pytest
import re
# import sys
# sys.path.append("..\common")
from common.send_request import SendRequest
from common.yaml_util import read_yaml, write_yaml, clear_yaml, read_testcase
# from common.yaml_util import write_yaml
# from common.yaml_util import read_testcase
# , write_yaml, clear_yaml, read_testcase
# from common.yaml_util import clear_yaml
# from common import send_request.SendRequest

import json


# @pytest.fixture(scope="function", autouse=False)
# def select_database():
#     print("用例之前执行")
#     yield
#     print("用例后执行")

class TestApi:
    # access_token = ""
    # Data_ID = ""

    # def setup_class(self):
    #     print("用类之前的操作")
    #
    # def setup(self):
    #     print("用例之前的操作")
    # def teardown_class(self):
    #     print("用类后的操作")
    #
    # def teardown(self):
    #     print("用例之后的操作")

    # sess = requests.session()
    # 获取鉴权码
    # @pytest.mark.smoke
    @pytest.mark.parametrize("caseinfo", read_testcase("test/test_post_token.yaml"))
    def test_post_token(self, select_database, caseinfo):
        print(caseinfo)
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        headers = caseinfo["request"]["headers"]
        json = caseinfo["request"]["json"]

        # url = "http://tripo.hotfix.travelconnect.co/api/v1/token/AcquireAuthorization"
        # header = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
        # json = {
        #     "CompanyCode": "TC0139",
        #     "UserName": "DAVID",
        #     "Password": "Travel2021"
        # }
        # res = requests.post(url=url, headers=header, json=json)
        # res = TestApi.sess.request(method="post", url=url, headers=header, json=json)
        res = SendRequest().send_all_request(method=method, url=url, headers=headers, json=json)
        print(res.json())

        write_yaml(data={"access_token": res.json()["Data"]})
        # print(res.text)
        # TestApi.access_token = res.json()["Data"]

    @pytest.mark.parametrize("caseinfo", read_testcase("test/test_post_creatinvoice1.yaml"))
    def test_creatinvoice1(self, caseinfo):

        # print(caseinfo)
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        headers = caseinfo["request"]["headers"]
        #添加字典
        headers["Authorization"] = read_yaml("access_token")

        # print(headers)

        json = caseinfo["request"]["json"]

        res = SendRequest().send_all_request(method=method, url=url, headers=headers, json=json)

        # print(det.text)
        print(res.json())
        write_yaml(data={"Data_ID": res.json()["Data"]["ID"][0]})
        # TestApi.Data_ID = det.json()["Data"]["ID"][0]
        print(read_yaml("Data_ID"))

    # @pytest.mark.parametrize("caseinfo", read_testcase("test/test_post_file_upload.yaml"))
    # def test_file_upload(self, caseinfo):
    #
    #     method = caseinfo["request"]["method"]
    #     url = caseinfo["request"]["url"]
    #     headers = caseinfo["request"]["headers"]
    #     # 添加字典
    #     headers["Authorization"] = read_yaml("access_token")
    #
    #
    #     files = caseinfo["request"]["files"]
    #     for key,value in files.items():
    #         files[key] = open(value,"rb")
    #         print(key,value)
    #
    #     res = SendRequest().send_all_request(method=method, url=url, headers=headers, files=files)
    #     print(res.json())


    # mode

    # def test_get_token(self):
    #     url = "http://tripo.hotfix.travelconnect.co/api/v1/token/AcquireAuthorization"
    #     params = {
    #         "CompanyCode": "TC0139",
    #         "UserName": "DAVID",
    #         "Password": "Travel2021"
    #     }
    #     res = requests.get(url=url, params=params)
    #     print(res.json())
    #
    # def test_post_token1(self):
    #     url = "http://tripo.hotfix.travelconnect.co/api/v1/token/AcquireAuthorization"
    #     header = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    #     files= {
    #         "media": open("E:\\SHUJ.png")
    #     }
    #     res = requests.post(url=url, headers=header, files=files)
    #     print(res.json())
    #     # print(res.text)
    #     TestApi.access_token = res.json()["Data"]
    #
    # def phpwind_start(self):
    #     url = "http://tripo.hotfix.travelconnect.co/api/v1/token/AcquireAuthorization"
    #     res = requests.get(url=url)
    #
    #     token = re.search('name="csrf_token" value="(.*?)"',res.text).group(1)
    #     re.findall();
    #
    #


    # def test_creatinvoice1(self, caseinfo):
    #     url = "http://tripo.hotfix.travelconnect.co/api/v1/b2bapp/Order/CreateManualInvoice"
    #     headers = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    #         # "Authorization": "84B23461-E186-4F43-B726-5BEBA0E55044"
    #         # "Authorization": TestApi.access_token
    #         "Authorization": read_yaml("access_token")
    #     }
    #
    #     json = {
    #
    #         "invoice": {
    #             "CustomerID": "771f3aa7-42ff-43c3-afab-6da587e16c5b",
    #             "SupplierID": "",
    #             "FollowID": 808,
    #             "ShipID": "",
    #             "ShipName": "",
    #             "CurrentID": 562,
    #             "CompanyName": "額度0921",
    #             "CountType": 0,
    #             "PayTime": "2022-12-05",
    #             "InvoiceTime": "2022-12-05",
    #             "LastName": ".",
    #             "FirstName": ".",
    #             "ClientName": "",
    #             "Phone": "",
    #             "Mobile": "123555",
    #             "Fax": "",
    #             "Email": "",
    #             "Currency": 132,
    #             "ExchangeRate": 1,
    #             "Discount": "",
    #             "PaymentType": 503,
    #             "BankChargesPercentage": 0,
    #             "BankCharges": 0,
    #             "CardChargesPercentage": 0,
    #             "CardCharges": 0,
    #             "AddressProvince": "",
    #             "AddressCity": "",
    #             "Address": "",
    #             "Remarks": "",
    #             "RemarksOne": "",
    #             "RemarksTwo": "",
    #             "RemarksThress": "",
    #             "ChargeTypeCard": 0,
    #             "ChargeTypeBank": 0
    #         },
    #         "quoteFInquiry": "",
    #         "Requirementid": 1,
    #         "QuoteFilghtInfoList": [],
    #         "otherFeetype": {
    #             "Feetypelist": [
    #                 {
    #                     "ID": "3a9848b4-cfa3-41fd-be10-0cd6030a07b9",
    #                     "Number": 1,
    #                     "MinFee": 1,
    #
    #                     "Remarks": "二日遊",
    #                     "Unit": "HKD",
    #                     "AdjustQuotion": 1,
    #                     "EntryName": "二日遊",
    #                     "PassengerList": [],
    #                     "list": [],
    #                     "keyWord": "",
    #
    #                     "tablePager": {
    #                         "page": 1,
    #                         "pageTotal": 5,
    #                         "total": 0
    #                     },
    #                     "OriginalQuotation": 1,
    #                     "feeID": 1
    #                 }
    #             ]
    #         },
    #         "manuallist": [],
    #         "hotellist": [],
    #         "PNRhotellist": [],
    #         "OneDayTourlist": [],
    #         "Parms": []
    #
    #     }
    #
    #     det = requests.post(url=url, headers=headers, json=json)
    #
    #
    #     # print(det.text)
    #     print(res.json())
    #     write_yaml(data={"Data_ID": res.json()["Data"]["ID"][0]})
    #     # TestApi.Data_ID = det.json()["Data"]["ID"][0]
    #     print(read_yaml("Data_ID"))
