from selenium import webdriver
from selenium.webdriver.common.by import By


def test_no_of_button():
    driver=webdriver.Chrome()
    driver.get("https://www.needdevelopers.com/contact")
    title=driver.title
    print(title)
    button=driver.find_elements(By.TAG_NAME, "button")
    print(len(button))
    for i in button:
        print(i.text)

    all_link= driver.find_elements(By.TAG_NAME,"a")
    print(len(all_link))
    for i in all_link:
        print(i.text)

def test_button_click():
    driver = webdriver.Chrome()
    driver.get("https://www.needdevelopers.com/")
    button_click=driver.find_element(By.XPATH,"(//button[contains(@class,'mat-focus-indicator mat-flat-button')])[2]")
    button_click.click()
