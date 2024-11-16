import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
@allure.title("Action P1")
@allure.description("verify Action P1")
def test_action_key():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name=driver.find_element(By.XPATH,"//input[@name='firstname']")
    #//key down
    actions=ActionChains(driver=driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name,"amit kumar").key_up(Keys.SHIFT).perform()
    time.sleep(3)
    driver.quit()
