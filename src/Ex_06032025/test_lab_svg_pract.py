import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
@allure.title("SVG")
@allure.description("verify SVG")
def test_svg_normal():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    search_box=driver.find_element(By.XPATH, "//input[@name='q']")
    search_box.send_keys("macmini")
    list_svg_element=driver.find_elements(By.XPATH, "//*[name()='svg']")
    list_svg_element[0].click()