from debugpy.server.cli import switches
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://vinothqaacademy.com/iframe/")
driver.maximize_window()
sleep(2)
driver.switch_to.frame("employeetable")
sleep(2)
driver.find_element(By.XPATH,"//input[@id='nameInput']").click()
driver.switch_to.default_content() #Back to main Page
sleep(2)
driver.switch_to.frame("popuppage")
driver.find_element(By.XPATH,"//button[@name='alertbox']").click()
alert = driver.switch_to.alert
sleep(2)
alert.accept()
driver.switch_to.default_content() #Back to main Page
sleep(2)
driver.switch_to.frame("registeruser")
driver.find_element(By.XPATH,"//div[@id='header']//span[3]").click()

driver.close()
