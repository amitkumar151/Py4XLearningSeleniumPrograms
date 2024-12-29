import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
def test_ebay_product_list():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver =webdriver.Chrome(chrome_options)
    driver.get("https://www.flipkart.com/")
    time.sleep(4)
    search_input=driver.find_element(By.CSS_SELECTOR,".zDPmFV")
    search_input.send_keys("macmini")
    search_button=driver.find_element(By.XPATH, "//button[@class='MJG8Up']")
    search_button.click()
    list_of_item=driver.find_elements(By.CSS_SELECTOR,".s-item__title")
    for i in list_of_item:
        print(i.text)

        time.sleep(5)

