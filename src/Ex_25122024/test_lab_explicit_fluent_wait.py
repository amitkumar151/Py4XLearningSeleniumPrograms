import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)


@allure.title("explicite fluent wait code ")
@allure.description("verify the title of VWO APP")
def test_ec_wait():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    email_webelement = driver.find_element(By.XPATH, "//input[@id='login-username']")
    email_webelement.send_keys("amit@gmail.com")
    pass_web_element = driver.find_element(By.ID, "login-password")
    pass_web_element.send_keys("amit@1211")
    button_click = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")
    button_click.click()
    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    WebDriverWait(driver=driver, poll_frequency=1, timeout=5, ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='js-notification-box-msg']")))

    error_pop_message = driver.find_element(By.XPATH, "//div[@id='js-notification-box-msg']")
    print(error_pop_message.text)
