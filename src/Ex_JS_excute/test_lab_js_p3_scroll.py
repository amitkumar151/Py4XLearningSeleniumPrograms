import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@allure.title("Shadow Dom")
@allure.description("verify shadow Dom")
def test_alert_normal():
    driver = webdriver.Chrome()
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()
    username_div=driver.find_element(By.XPATH, "//div[@id='userName']")
    driver.execute_script("arguments[0].scrollIntoView(true);", username_div)
    time.sleep(4)
    input_box=driver.execute_script(
        "return document.querySelector('div#userName').shadowRoot.querySelector('#app2').shadowRoot.querySelector('#pizza');")
    input_box.send_keys("farmhouse")
    time.sleep(4)
    driver.quit()