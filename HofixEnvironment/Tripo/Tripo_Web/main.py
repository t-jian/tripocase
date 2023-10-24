import pytest
import os

if __name__ == '__main__':
    # pytest.main(["-vs"])
    # os.system("allure serve temps/allure")
    # os.system("allure generate ./temps/allure -o ./reports --clean")


# 測試報告用例
    pytest.main(['-vs', './test_case/test_create_invoice_Jayce.py', '--clean-alluredir', '--alluredir=./temps/test1_allure'])
#     pytest.main(['-vs', './test_case/test_order_create', '--clean-alluredir', '--alluredir=./temps/test1_allure'])
    # pytest.main(['-s', './test_case/test2.py', '--clean-alluredir', '--alluredir=./temps/test2_allure'])
    os.system('allure generate ./temps/test1_allure -o ./allure-report  --clean')

 # 冒煙測試用例
 #    pytest.main(['-s', './test_case/test_smoke_invoice.py', '--clean-alluredir', '--alluredir=./temps/test_smoke_invoice_allure'])
 #    pytest.main(['-s', './test_case/test_smoke_quotation.py', '--clean-alluredir', '--alluredir=./temps/test_smoke_quotation_allure'])
 #    pytest.main(['-s', './test_case/test_smoke_xo.py', '--clean-alluredir', '--alluredir=./temps/test_smoke_xo_allure'])
 #    os.system('allure generate ./temps/test_smoke_invoice_allure ./temps/test_smoke_quotation_allure ./temps/test_smoke_xo_allure  -o ./allure-report --clean')


