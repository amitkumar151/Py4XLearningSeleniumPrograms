import time

from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By

@allure.title("open a registration page and fill the data")
def test_open_url(button=None):
    driver=webdriver.Chrome()
    driver.maximize_window()
    time.sleep(3)
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    first_name=driver.find_element(By.ID, value="input-firstname")
    first_name.send_keys("Amit Kumar")
    last_name=driver.find_element(By.ID, value="input-lastname")
    last_name.send_keys("sinha")
    insert_email=driver.find_element(By.ID, value="input-email")
    insert_email.send_keys("amit@yeopmail.com")
    insert_phoneno=driver.find_element(By.ID, value="input-telephone")
    insert_phoneno.send_keys("8776766445")
    insert_password=driver.find_element(By.ID, value="input-password")
    insert_password.send_keys("Amit20151")
    confirm_password=driver.find_element(By.ID, value="input-confirm")
    confirm_password.send_keys("Amit20151")
    driver.find_element(By.NAME, value="newsletter").click()
    driver.find_element(By.NAME, value="agree").click()
    continue_button = driver.find_element(By.XPATH, "//*[@type='submit']")
    continue_button.click()
    time.sleep(3)
    sucess_message=driver.find_element(By.XPATH, "//div[@id='content']").text
    assert "Your Account Has Been Created!" in sucess_message
    driver.implicitly_wait(4)


#hsgdhasgj