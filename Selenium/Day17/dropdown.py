
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
driver = webdriver.Chrome()

driver.get("https://vinothqaacademy.com/drop-down/")
driver.maximize_window()

#1)Selecting dropdown
#drp1 = driver.find_element(By.XPATH,"//select[@id='FromAccount']")
select= Select(driver.find_element(By.XPATH,"//select[@id='FromAccount']"))

#2)Select option from dropdown
#select.select_by_visible_text("8400001 Bal - $3,881.62")
#sleep(2)
#select.select_by_value("Current")
#sleep(2)
#select.select_by_index(3)


#3)Capture all the option in dropdown
'''allop = select.options

for option in allop:
    print("Text:", option.text)
    print("Value:", option.get_attribute("value"))

print(len(allop))

#4)Select option from dropdown without using builtin method
for opt in allop:
    if opt.text == "8400045 Bal - $8,758.78":
        opt.click()
        sleep(2)
        break'''

#5)If select class is not available
op = driver.find_elements(By.XPATH,"//select[@id='FromAccount']/'options'")
print(op)


driver.close()

