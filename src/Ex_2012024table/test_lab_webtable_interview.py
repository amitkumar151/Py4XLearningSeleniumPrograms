from selenium import webdriver
from selenium.webdriver.common.by import By

def test_webtable():
    driver=webdriver.Chrome()
    driver.get("https://practice.expandtesting.com/tables")
    #driver.maximize_window()

    row_elements= driver.find_elements(By.XPATH,"//table[contains(@id, table1)]/tbody/tr")
    row=len(row_elements)
    print(row)

    col_elements = driver.find_elements(By.XPATH, "//table[contains(@id, table1)]/tbody/tr[1]/td")
    col = len(col_elements)
    print(col)

    first_part="//table[contains(@id, table1)]/tbody/tr["
    second_part="]/td["
    third_part="]"

    for i in range(2,row+1):
        for j in range(1,col+1):
            dynamic_path=f"{first_part}{i}{second_part}{j}{third_part}"
            print(dynamic_path)
            data=driver.find_element(By.XPATH, dynamic_path)
            print(data.text, end=" ")

