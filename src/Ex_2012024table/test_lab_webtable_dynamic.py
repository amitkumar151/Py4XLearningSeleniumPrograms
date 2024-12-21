from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtable():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")
    table=driver.find_elements(By.XPATH, "//table[@summary='Sample Table']/tbody")
    row_table=driver.find_elements(By.XPATH,"//table[@summary='Sample Table']/tbody/tr")

    for row in row_table:
        cols=row.find_elements(By.TAG_NAME,"td")
        for e in cols:
            if "UAE" in e.text:
                print("yes")