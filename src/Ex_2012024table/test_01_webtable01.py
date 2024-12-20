from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtable():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    #driver.maximize_window()
    # ROW xpath -//table[contains(@id,'customers')]
    row_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr")
    row =len(row_elements)
    print(row)

    # COlum
    col_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'customers')]/tbody/tr[2]/td")
    col =len(col_elements)
    print(col)


    #//table[contains(@id,'customers')]/tbody/tr[7]/td[3]
    #//table[contains(@id,'customers')]/tbody/tr[
    # 7 i(2,7)
    # ]/td[
    # 3 j(1,3)
    # ]
    first_part = "//table[contains(@id,'customers')]/tbody/tr["
    second_part= "]/td["
    third_part= "]"

    for i in range(2,row+1):
        for j in range(1,col+1):
            dyanmic_path=f" {first_part}{i}{second_part}{j}{third_part}"
            print(dyanmic_path)
            data=driver.find_element(By.XPATH,dyanmic_path)
            print(data.text, end=" ")

