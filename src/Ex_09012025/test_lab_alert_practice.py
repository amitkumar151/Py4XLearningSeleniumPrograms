import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@allure.title("Alert")
@allure.description("alert with accept")
def test_ec_wait():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    element_promot=driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
    element_promot.click()
    WebDriverWait(driver=driver,timeout=5).until(EC.alert_is_present())

    alert=driver.switch_to.alert
    alert.accept()
    result_text=driver.find_element(By.ID,"result").text
    print(result_text)
    assert result_text=="You successfully clicked an alert"
    time.sleep(3)

