from debugpy.server.cli import switches
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
outer = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer)
inner = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(inner)
sleep(4)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Welcome")
driver.switch_to.parent_frame() #go o outerframe from inner frame
driver.close()