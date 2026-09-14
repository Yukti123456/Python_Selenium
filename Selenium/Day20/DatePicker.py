from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime

from trio import sleep_until

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)
#directly assinging value
#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("05/03/2023")

#Approach 2 ---> By using calender
year ="2027"
month ="March"
day ="01"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click() # Open datepicker
#Selcting month and year
'''while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
        driver.find_element(By.XPATH,"//span[ @class ='ui-icon ui-icon-circle-triangle-w']").click()

date = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody//tr/td/a")
#Selecting day
for ele in date:
    if ele.text == day:
        ele.click()
        break
'''
# Target date
target_date = "15/08/2026"

# Convert target date into datetime
target = datetime.strptime(target_date, "%d/%m/%Y")

while True:

    # Get currently displayed month and year
    mon = driver.find_element(
        By.XPATH, "//span[@class='ui-datepicker-month']"
    ).text

    yr = driver.find_element(
        By.XPATH, "//span[@class='ui-datepicker-year']"
    ).text

    # Convert displayed month/year into datetime
    current = datetime.strptime(
        f"{mon} {yr}", "%B %Y"
    )

    # Compare target month/year with displayed month/year
    if target.year == current.year and target.month == current.month:
        break

    elif target > current:
        # Target date is in future
        driver.find_element(
            By.XPATH,
            "//span[@class='ui-icon ui-icon-circle-triangle-e']"
        ).click()

    else:
        # Target date is in past
        driver.find_element(
            By.XPATH,
            "//span[@class='ui-icon ui-icon-circle-triangle-w']"
        ).click()




        
#Select Date

