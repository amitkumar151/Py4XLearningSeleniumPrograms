import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@allure.title("print the title of vwo app")
@allure.description("verify the title of VWO APP")
def test_ec_wait():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    time.sleep(5)
    email_webelement = driver.find_element(By.XPATH, "//input[@id='login-username']")
    email_webelement.send_keys("amit@gmail.com")
    pass_web_element = driver.find_element(By.ID, "login-password")
    pass_web_element.send_keys("amit@1211")
    button_click = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    button_click.click()
    WebDriverWait(driver=driver,timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='js-notification-box-msg']")))

    error_pop_message = driver.find_element(By.XPATH, "//div[@id='js-notification-box-msg']")
    print(error_pop_message.text)
