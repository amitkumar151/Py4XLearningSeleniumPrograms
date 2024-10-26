import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)
@allure.title("fill the form page with radio button")
@allure.description(" form page fillup ")
def test_fill_up_form():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()
    time.sleep(4)
    first_name = driver.find_element(By.NAME,"//input[@name= 'firstname']")
    first_name.send_keys("amit kumar")
    last_name = driver.find_element(By.NAME,"//input[@name='lastname']")
    first_name.send_keys("sinha")
    driver.implicitly_wait(3)
    select_gender = driver.find_element(By.CSS_SELECTOR, "#sex-1")
    select_gender.click()
    driver.implicitly_wait(2)
    select_year_ofExperience = driver.find_element(By.CSS_SELECTOR, "#sex-1")
    select_year_ofExperience.click()
    Select_profession = driver.find_element(By.CSS_SELECTOR, "#profession-1")
    Select_profession.click()
    select_auto_tool = driver.find_element(By.CSS_SELECTOR, "#tool-2")
    select_auto_tool.click()
