import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Alert")
@allure.description("alert with accept")
def test_alert_normal():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    element_normal = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    element_normal.click()
    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()
    result_text = driver.find_element(By.ID, "result").text
    print(result_text)
    assert result_text == "You successfully clicked an alert"
    time.sleep(3)


def test_alert_confirm():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    element_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    element_confirm.click()
    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.dismiss()
    result_text = driver.find_element(By.ID, "result").text
    print(result_text)
    assert result_text == "You clicked: Cancel"
    time.sleep(3)


def test_alert_prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    element_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    element_prompt.click()
    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.send_keys("amit kumar")
    alert.accept()
    result_text = driver.find_element(By.ID, "result").text
    print(result_text)
    assert result_text == "You entered: amit kumar"
    time.sleep(3)
