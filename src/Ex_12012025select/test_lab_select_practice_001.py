import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
@allure.title("select")
@allure.description("verify select")
def test_alert_normal():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    select_html_tag=driver.find_element(By.ID, "dropdown")
    select= Select(select_html_tag)
    #select.select_by_index(1)
    #select.select_by_visible_text("Option 1")
    select.select_by_value("1")
