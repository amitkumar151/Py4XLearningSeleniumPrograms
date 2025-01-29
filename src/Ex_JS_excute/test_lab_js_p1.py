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
    driver.get("https://app.vwo.com/#/login")
    driver.execute_script("alert(1)")
    time.sleep(4)