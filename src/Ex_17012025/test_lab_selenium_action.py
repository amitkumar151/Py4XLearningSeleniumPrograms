import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
@allure.title("action mouse back")
@allure.description("verify action mouse back")
def test_svg_normal():
    driver = webdriver.Chrome()
    driver.get("https://www.needdevelopers.com/")
    button_element=driver.find_element(By.XPATH, "(//button[contains(@class,'mat-focus-indicator mat-flat-button')])[2]")
    time.sleep(4)
    button_element.click()
    time.sleep(4)
    # Key Down
    action_builder=ActionBuilder(driver=driver)
    action_builder.pointer_action.pointer_up(MouseButton.BACK)
    action_builder.perform()