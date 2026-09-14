from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from Selenium.Day18.Alert import alertwindow

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://demoqa.com/alerts")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[@id='alertButton']").click()

alert = driver.switch_to.alert
sleep(2)
alert.accept()
driver.close()
