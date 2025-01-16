import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


@allure.title("Exception -No such element exception")
@allure.description("verify Exception -No such element exception")
def test_alert_normal():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    try:
        element=driver.find_element(By.ID, "this id doesnot exist")
    except NoSuchElementException as nse:
        print(nse.msg)