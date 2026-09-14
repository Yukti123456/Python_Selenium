from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()


driver.get("https://vinothqaacademy.com/mouse-event/")
driver.maximize_window()

slider = driver.find_element(By.XPATH,"//div[@id='handle_max']")
print("Location of Slider before Moving.....")
print(slider.location)
ac = ActionChains(driver)
ac.drag_and_drop_by_offset(slider,100,0).perform()
print("Location of Slider after Moving.....")
print(slider.location)
