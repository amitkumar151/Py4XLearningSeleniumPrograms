from selenium import webdriver
import pytest
import allure


@allure.title("verify the title of web page of app.vwo.com")
def test_sample():
    driver =webdriver.Chrome()
    driver.get("https://courses.thetestingacademy.com/")
