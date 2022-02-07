import unittest
import time


from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase(unittest.TestCase):

   def test_01_login(self):
        global driver
        #打开浏览器
        driver = webdriver.Chrome()
        #加载网页
        driver.get("http://192.168.18.2/erp")
        #输入账号密码
        driver.find_element(By.ID,"username").send_keys("admin")
        driver.find_element(By.ID,"password").send_keys("admin")
        time.sleep(2)
        driver.find_element(By.ID,"btnLogin").click()

        #定位
        driver.find_element(By.LINK_TEXT,"")


        #value = driver.find_element(By.XPATH, "//span[text()='按图片搜索']").get_attribute("class")


    #
    # def test_02_login(self):
    #     print("测试")


