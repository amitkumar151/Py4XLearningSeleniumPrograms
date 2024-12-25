import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options


def test_chrome_current_url_verification():
    driver = webdriver.Chrome()
    driver.get("https://www.needdevelopers.com/")
    assert driver.current_url == "https://www.needdevelopers.com/"
    time.sleep(6)
    driver.quit()


def test_edge_current_url_verification():
    driver = webdriver.Edge()
    driver.get("https://www.needdevelopers.com/")
    assert driver.current_url == "https://www.needdevelopers.com/"
    time.sleep(7)
    driver.quit()


"""def test_firefox_current_url_verification():
    driver = webdriver.Firefox()
    driver.get("https://www.needdevelopers.com/")
    assert driver.current_url == "https://www.needdevelopers.com/"
    time.sleep(7)
    driver.quit()"""
