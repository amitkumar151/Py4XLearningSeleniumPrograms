import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("Action P2")
@allure.description("verify mouseBack P2")
def test_action_key():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name=driver.find_element(By.XPATH,"//input[@name='firstname']")