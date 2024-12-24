import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_chrome_option():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.thenavsoft.com/")
    time.sleep(10)
    pagesource_data=driver.page_source
    print(pagesource_data)
