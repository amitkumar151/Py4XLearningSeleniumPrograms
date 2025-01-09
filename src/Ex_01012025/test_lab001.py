import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@allure.title("ebay list of title fetch ")
def test_all_title():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    search_input = driver.find_element(By.ID, "gh-ac")
    search_input.send_keys("macmini")
    search_button = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    search_button.click()

    time.sleep(5)
    all_title_list= driver.find_elements(By.CSS_SELECTOR, ".s-item__title" )
    for i in all_title_list:
        print(i.text)

    assert len(all_title_list)==62
