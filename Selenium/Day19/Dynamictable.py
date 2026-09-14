#from debugpy.server.cli import switches
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from Selenium.Day17.BrokenLinks import count

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://practice.expandtesting.com/dynamic-table")
driver.maximize_window()
#Finding no. of rows
rows = len(driver.find_elements(By.XPATH,"//table[@class='table table-striped']//tbody/tr"))
print(rows)
count = 0
for r in range(1,rows):
    disk = driver.find_element(By.XPATH, "//table[@class='table table-striped']//tbody/tr["+str(r)+"]/td[4]").text
    if disk > "1 Mbps":
       print(disk)
       count = count + 1

print(count)



driver.close()

