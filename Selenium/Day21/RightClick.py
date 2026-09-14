from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()


driver.get("https://vinothqaacademy.com/mouse-event/")
driver.maximize_window()
button = driver.find_element(By.XPATH,"//button[@id='rightBtn']")

act = ActionChains(driver)
act.context_click(button).perform() # right Click action
sleep(3)
