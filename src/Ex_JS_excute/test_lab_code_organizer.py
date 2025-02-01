import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSelenium:

    def __init__(self):
        self.driver= None
    @allure.title("JS Excute")
    @allure.description("JS excute")
    def test_open_browser(self):
        self.driver = webdriver.Chrome()
        # driver.get("https://selectorshub.com/xpath-practice-page/")
        self.driver.get("https://www.needdevelopers.com/")
        self.driver.maximize_window()

    def test_js(self):
        self.driver.execute_script("window.scrollBy(0,500)")
        title = self.driver.execute_script("return document.title")
        url = self.driver.execute_script("return document.URL")
        print(title)
        print(url)
    def close_browser(self):

        time.sleep(4)
        self.driver.quit()


test= TestSelenium()
test.test_open_browser
#test.test_js()
test.close_browser()
