from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org")

search_box = driver.find_element(By.NAME, "search")

search_box.send_keys("Software Engineering")

time.sleep(2)

search_box.submit()

time.sleep(3)

print("New page title:", driver.title)

driver.quit()