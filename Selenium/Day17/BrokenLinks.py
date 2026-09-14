from itertools import count
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/broken-links.php")
sleep(4)
alllinks = driver.find_elements(By.TAG_NAME,"a")
count =0
for link in alllinks:
    url= link.get_attribute("href")
    try:
         res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url," is broken link")
        count+=1
    else:
        print(url," is valid link")
driver.close()