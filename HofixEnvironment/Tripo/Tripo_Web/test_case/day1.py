import time
from selenium.webdriver.common.by import By
from webdriver_helper import get_webdriver

#例子1 自动安装浏览器驱动、安装selenium等库、启动浏览器、截图
driver = get_webdriver("chrome")
# driver = get_webdriver("firefox")
driver.maximize_window()
driver.get_screenshot_as_file("./report/1.启动浏览器.png")
driver.get("http://tripo.hotfix.travelconnect.co")
driver.get_screenshot_as_file("./report/2.Tripo.png")
print(driver.current_url)
print(driver.title)
input()
driver.quit()

#例子2定位元素

# driver = get_webdriver("chrome")
# driver.maximize_window()
# driver.get("http://tripo.hotfix.travelconnect.co")
# #属性定位
# e1 = driver.find_element(By.TAG_NAME, "input")
# # e2 = driver.find_element(By.ID, "input")
# # e3 = driver.find_element(By.NAME, "input")
# # e4 = driver.find_element(By.CLASS_NAME, "input")
# e1.click()
# print(e1.tag_name)
#
#
# #文本定位，只能定位a标签的内容
# e5 = driver.find_element(By.LINK_TEXT, "電子印花")
# e6 = driver.find_element(By.PARTIAL_LINK_TEXT, "印花")
# # e3 = driver.find_element(By.NAME, "input")
# # e4 = driver.find_element(By.CLASS_NAME, "input")
# e5.click()
# e6.click()
#
#
# e7 = driver.find_element(By.XPATH, "//")
# e8 = driver.find_element(By.CSS_SELECTOR, "///")
#
# input()
# driver.quit()


# #搜寻和断点
# driver = get_webdriver("chrome")
# driver.maximize_window()
# driver.get("http://tripo.hotfix.travelconnect.co")
# #属性定位
#
# e_list = self.driver.find_elements(By.XPATH, '//*[@class="bottom-detail"]//*[@class="B_TextStyle font-ari"]')
# print(len(e_list))
# assert len(e_list) == 19, f"len(e_list) !== 20"
# for el in e_list:
#     print(el.text)
#     assert "QE" in el.text
# print("测试完成")
# input()
