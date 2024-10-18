import allure
import pytest
from selenium import webdriver


@allure.title("Verify the Katalon demo Home page")
def test_Katalon__Home():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    current_url = driver.current_url
    title = driver.title
    source = driver.page_source

    # Verify the current URL
    assert current_url == "https://katalon-demo-cura.herokuapp.com/"
    # Verfiy the current title
    assert title == "CURA Healthcare Service"
    # Verify the page in soucre
    assert title in source