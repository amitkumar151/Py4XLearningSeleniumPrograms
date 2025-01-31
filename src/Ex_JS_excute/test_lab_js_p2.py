import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@allure.title("JS Excute")
@allure.description("JS excute")
def test_alert_normal():
    driver = webdriver.Chrome()
    #driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.get("https://www.needdevelopers.com/")
    driver.execute_script("window.scrollBy(0,1500)")
    title=driver.execute_script("return document.title")
    url=driver.execute_script("return document.URL")

    print(title)
    print(url)
    time.sleep(4)
    driver.quit()
