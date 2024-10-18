import time

from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By


@allure.title("open a url -https://katalon-demo-cura.herokuapp.com/")
def test_open_url():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment=driver.find_element(By.ID, value="btn-make-appointment")
    make_appointment.click()
    currenturl=driver.current_url
    assert currenturl=="https://katalon-demo-cura.herokuapp.com/profile.php#login"
    user_name=driver.find_element(By.ID, value="txt-username")
    user_name.send_keys("amitkumar")
    password=driver.find_element(By.ID, value="txt-password")
    password.send_keys("amit@8676876")
    logon_button=driver.find_element(By.ID, value="btn-login")
    logon_button.click()

