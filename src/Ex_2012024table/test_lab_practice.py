import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_verification_title():
    driver= webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    email_address=driver.find_element(By.ID, "login-username")
    email_address.send_keys("amit@gmail.com")
    password_enter=driver.find_element(By.NAME, "password")
    password_enter.send_keys("password@1234")
    button_click=driver.find_element(By.ID, "js-login-btn")
    button_click.click()
    time.sleep(4)
    error_msg=driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg.text)
    assert error_msg.text =="Your email, password, IP address or location did not match"