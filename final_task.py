from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")

time.sleep(2)

checkbox_link = driver.find_element(By.LINK_TEXT, "Checkboxes")
checkbox_link.click()

time.sleep(2)

checkboxes = driver.find_elements(
    By.CSS_SELECTOR,
    "input[type=checkbox]"
)

first_checkbox = checkboxes[0]

if not first_checkbox.is_selected():
    first_checkbox.click()

print("First checkbox selected:", first_checkbox.is_selected())

driver.quit()