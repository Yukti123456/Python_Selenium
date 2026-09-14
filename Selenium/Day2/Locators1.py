from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# id & name loacators
driver.find_element(By.ID, "small-searchterms").send_keys("Phone")
#Linktext & Patial Linktext