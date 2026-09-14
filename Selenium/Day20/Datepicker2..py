from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()


driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='dob']").click()

#Selecting Month
select1= Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
select1.select_by_visible_text("Sep")
sleep(2)

#Selecting year
select2= Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
select2.select_by_visible_text("2017")
sleep(2)
day = "29"
date = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")

for ele in date:
    if ele == day:
        ele.click()
        sleep(2)
        break

driver.close()