from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get("https://www.hotstar.com/in/home")
driver.maximize_window()

#Capture Cookies from the browser
cookies = driver.get_cookies()
print("Size of Cookies: ", len(cookies))
#Print details of all Cookies
for c in cookies:
    print(c.get('name'),":",c.get('value'),c.get('expiry'))
#Add new cookie to the browser
driver.add_cookie({"name":"MyCookie","value":"123456"})
cookies = driver.get_cookies()
print("Size of Cookies after adding new one: ", len(cookies))

#Delete a specific cookie from browser
driver.delete_cookie("MyCookie")
cookies = driver.get_cookies()
print("Size of Cookies after deleting new one: ", len(cookies))
#Delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Size of Cookies after deleting all: ", len(cookies))
driver.quit()