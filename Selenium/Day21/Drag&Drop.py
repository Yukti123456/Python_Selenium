from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()


driver.get("https://vinothqaacademy.com/mouse-event/")
driver.maximize_window()

drag = driver.find_element(By.ID,"dragItem")
drop = driver.find_element(By.ID,"dropZone")

ac = ActionChains(driver)
ac.drag_and_drop(drag,drop).perform()
sleep(3)
driver.quit()