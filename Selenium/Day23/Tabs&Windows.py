from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

'''driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Udemy Courses']").send_keys(Keys.CONTROL+Keys.RETURN)
sleep(4)'''

#New Tab - Selenium4: Opens a new tab and switches to new tab
#driver.get("https://testautomationpractice.blogspot.com/")
#driver.switch_to.new_window('tab')
#driver.get("https://www.hotstar.com/in/home")
#sleep(3)
#New Tab - Selenium4: Opens a new browser and switches to new tab
driver.get("https://testautomationpractice.blogspot.com/")
driver.switch_to.new_window('window')
driver.get("https://www.hotstar.com/in/home")
sleep(3)

driver.close()

