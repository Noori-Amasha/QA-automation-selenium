from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org")

time.sleep(3)

print("Page title is:", driver.title)

driver.quit()