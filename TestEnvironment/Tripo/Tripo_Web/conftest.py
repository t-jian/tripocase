import pytest
# from TripoTest.Tripo.Tripo_Api_Automation.common.yaml_util import clear_yaml
from webdriver_helper import get_webdriver


# @pytest.fixture(scope="function", autouse=False)
# def driver():
#     b = get_webdriver("chrome")
#     # b.get("http://tripo.hotfix.travelconnect.co/#/login")
#     yield b
#     b.quit()



@pytest.fixture(scope="session", autouse=False)
def driver():
    b = get_webdriver("chrome")
    # b.get("http://tripo.hotfix.travelconnect.co/#/login")
    yield b
    b.quit()

#
# @pytest.fixture(scope="function", autouse=False)
# def select_database():
#     print("用例之前执行")
#     yield
#     print("用例后执行")
#
#
# @pytest.fixture(scope="class", autouse=False)
# def select_database1():
#     print("类之前执行")
#     yield
#     print("类之后后执行")
#
# @pytest.fixture(scope="session", autouse=True)
# def select_database1():
#     clear_yaml()
#     print("开始前清空存储变量extract.yaml的文档")
#
#     yield
#     print("David 测试完成")