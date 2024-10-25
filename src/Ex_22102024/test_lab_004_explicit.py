import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)

@allure.title("App.vwo.com - Explicit Wait")
@allure.description("Verify that App.vwo.com - Explicit Wait")
def test_5():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # driver.implicitly_wait(5) # Automation - 0.01% -

    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys("abc@gmail.com")

    # Find the email,
    # Find the password,

    # <input
    # type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe"
    # data-gtm-form-interact-field-id="1">

    password_web_element = driver.find_element(By.NAME, "password")
    password_web_element.send_keys("password@1234")

    # Click on the Sign Button

    # <button type="submit"
    # id="js-login-btn"
    # class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica"
    # >

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    # Wait for sometime

    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]

    # Fluent Wait
    (WebDriverWait(driver=driver, poll_frequency=1, timeout=5, ignored_exceptions=ignore_list)
    .until(EC.visibility_of_element_located
        ((By.CLASS_NAME, "notification-box-description"))))

    # A Condition to check the element
    # error_msg_element - comes after 5 seconds
    # I have to wait with some condition -
    # wait with the condition
    # Add a condition so that Webdriver should wait for that condition.
    # element is visible then assertion
    # when  this -> then do this

    # Smart Logic to wait for the element
    # Condition based Logic

    # Verify that message is visible.
    # <div
    # class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">
    # Your email, password, IP address or location did not match</div>

    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"

    driver.quit()