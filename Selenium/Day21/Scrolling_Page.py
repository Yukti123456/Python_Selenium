from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()


driver.get("https://vinothqaacademy.com/mouse-event/")
driver.maximize_window()

#1) Scroll down page by pixel
#driver.execute_script("window.scrollBy(0,500)","")
#sleep(2)
#value = driver.execute_script("return window.pageYOffset;")
#print("Number of pixels moved:",value)

#2)Scroll down till element found
#ele = driver.find_element(By.XPATH,"//button[@id='resetBtn']")
#driver.execute_script("arguments[0].scrollIntoView();",ele)
#value = driver.execute_script("return window.pageYOffset;")
#sleep(2)
#print("Number of pixels moved:",value)
#sleep(2)

#3)Scroll down page till end
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
sleep(2)
print("Number of pixels moved:",value)
sleep(5)
#4)Scroll up to starting position
driver.execute_script("window.scrollTo(0,-document.body.scrollHeight)")
value1 = driver.execute_script("return window.pageYOffset;")
sleep(2)
print("Number of pixels moved:",value1)
driver.close()