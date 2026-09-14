from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://vinothqaacademy.com/multiple-windows/")
driver.maximize_window()

driver.find_element(By.XPATH,"//div[@class='elementor-element elementor-element-f5f0e8d elementor-widget elementor-widget-html']//button[@id='button1']").click()
windowid = driver.window_handles
#Approach 1
'''windowid = driver.current_window_handle
#print(windowid)#53EB4DAC29FF56BA988720AD727F1C9E
sleep(4)
driver.find_element(By.XPATH,"//div[@class='elementor-element elementor-element-f5f0e8d elementor-widget elementor-widget-html']//button[@id='button1']").click()
windowid = driver.window_handles
parentwindowid=windowid[0]
childwindowid=windowid[1]
driver.switch_to.window(childwindowid)
print(driver.title)
driver.switch_to.window(parentwindowid)
print(driver.title)'''
for wind in windowid:
    driver.switch_to.window(wind)
    print(driver.title)
#Close an particular window
for wind in windowid:
    driver.switch_to.window(wind)
    if driver.title == "Demo Site – Multiple Windows – Vinoth Tech Solutions":
        driver.close()

driver.close()