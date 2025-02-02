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
    driver.get("https://www.needdevelopers.com/")
    module_click=driver.find_element(By.XPATH, "//div[@class='mat-ripple menu-text']")
    module_click.click()
    time.sleep(5)
    python_click=driver.find_element(By.XPATH, "//a[@href='/solutions/python']")
    python_click.click()
    time.sleep(4)
    title_new=driver.title
    assert title_new=="Python Development Services | Backend Developers | Need Developers"
    driver.execute_script("window.scrollBy(0,1500)")
    get_expert_button=driver.find_element(By.XPATH, "//section[@class='module solution-module']//span[@class='mat-button-wrapper'][normalize-space()='GET EXPERT HELP']")
    time.sleep(4)
    get_expert_button.click()
    time.sleep(6)

