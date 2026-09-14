from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()


driver.get("https://text-compare.com/")
driver.maximize_window()
input_box1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input_box2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
input_box1.send_keys("Welcome")
ac = ActionChains(driver)

#Ctrl + A
ac.key_down(Keys.CONTROL) # Click on control
ac.send_keys("a") # Click A
ac.key_up(Keys.CONTROL) # Release the Key
ac.perform() # Perform action on key
sleep(2)
#Ctrl + C
ac.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
sleep(2)
# Tab
ac.send_keys(Keys.TAB).perform()
sleep(2)
#Ctrl + V
ac.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
sleep(2)