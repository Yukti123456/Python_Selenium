from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()


driver.get("https://vinothqaacademy.com/mouse-event/")
driver.maximize_window()

double_click = driver.find_element(By.ID,"doubleBtn")
ac = ActionChains(driver)

ac.double_click(double_click).perform()
driver.quit()