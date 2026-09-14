from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.NAME,"Email").clear()
driver.find_element(By.NAME,"Email").send_keys("admin@yourstore.com")
time.sleep(3)
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)
t = driver.title
at = ("Dashboard / nopCommerce administration")
if at == t:
    print("Login test passed")
else:
    print("Login Test failed")
driver.close()