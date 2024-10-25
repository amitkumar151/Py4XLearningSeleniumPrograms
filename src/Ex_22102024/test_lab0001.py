import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
@allure.title("print the title of macmini by search in ebay")
@allure.description("verify the macmini by search in ebay by 62")
def test_ebay_search():
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    search_box_input = driver.find_element(By.XPATH, "//input[@placeholder='Search for anything']")
    search_box_input.send_keys("macmini")
    button_click_search = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    button_click_search.click()

    list_of_item = driver.find_elements(By.CSS_SELECTOR, ".s-item_title")
    for i in list_of_item:
        print(i.text)
        assert len(list_of_item) == 62
    time.sleep(4)
    driver.quit()
