from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()

try:
    driver.get("http://localhost/opencart/")
    sleep(2)
    print("Title:", driver.title)
    print("URL:", driver.current_url)

finally:
    driver.quit()