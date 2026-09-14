from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/practice/")
driver.maximize_window()
#driver.save_screenshot(r"C:\Users\yukti\PycharmProjects\PythonProject3\Selenium\Day23\home.png")
#driver.save_screenshot(os.getcwd() +"\\home.png")
#driver.get_screenshot_as_png() #save in binary format
#driver.get_screenshot_as_base64() #save in binary format
driver.get_screenshot_as_file(os.getcwd() +"\\home.png")
driver.close()

