from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()


driver.get("https://practice.expandtesting.com/hovers")
driver.maximize_window()

image1 = driver.find_element(By.XPATH,"//div[@class='container']//div[1]//img[1]")
ac = ActionChains(driver)
#image2 = driver.find_element(By.XPATH,"//div[@class='container']//div[1]//img[2]")
profile = driver.find_element(By.XPATH,"//div[@class='figcaption']//a")
ac.move_to_element(image1).perform()
sleep(2)
