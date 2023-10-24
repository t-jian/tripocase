import pytest
import os

if __name__ == '__main__':
    pytest.main(["-vs"])
    # os.system("allure serve temps/allure")
    os.system("allure generate ./temps/allure -o ./reports --clean")
