import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


@allure.title("Print the Titles of the Ebay sites after searching")
@allure.description("Verify that 62 items are there for macmini")
def test_5():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    search_box_input_xpath = driver.find_element(By.XPATH, "//input[@placeholder='Search for anything']")
    # search_box_inout_css = driver.find_element(By.CSS_SELECTOR,"#gh-ac")
    search_box_input_xpath.send_keys("macmini")

    search_box_button = driver.find_element(By.CSS_SELECTOR, "input[value='Search']")
    search_box_button.click()

    list_of_items = driver.find_elements(By.CSS_SELECTOR, ".s-item__title")
    list_of_items_price = driver.find_elements(By.CSS_SELECTOR, ".s-item__price")
    len_item = len(list_of_items)
    len_item_price = len(list_of_items_price)

    # for i in len(list_of_items_price):
    # print(list_of_items[i].text + " || " + list_of_items_price[i].text)
    min_items = min(len_item, len_item_price)
    print(min_items)
    #for i in range(1,min_items+1):
        #print(i)


    time.sleep(5)
    driver.quit()
