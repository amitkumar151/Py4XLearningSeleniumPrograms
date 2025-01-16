import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("svg")
@allure.description("verify svg with states")
def test_alert_normal():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    element=driver.find_element(By.ID, "this id doesnot exist")
    #esponse = {'status': 404, 'value':
    # '{"value":{"error":"no such element",
    # "message":"no such element: Unable to locate element: