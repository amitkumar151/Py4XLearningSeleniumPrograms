import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


@allure.title("Exception -StaleElementReferenceException")
@allure.description("verify Exception -StaleElementReferenceException")
def test_alert_normal():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    try:
        search_box = driver.find_element(By.ID, "APjFqb")
        driver.refresh()
        search_box.send_keys("macmini")
    except StaleElementReferenceException as see:
        print(see.msg)
