#from debugpy.server.cli import switches
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://demoqa.com/webtables")
driver.maximize_window()

#1)Count no. of rows and columns
rows = len(driver.find_elements(By.XPATH,"//table[@class='-striped -highlight table table-striped table-bordered table-hover']//tr"))
print("No. of columns: ",rows)

cols = len(driver.find_elements(By.XPATH,"//table[@class='-striped -highlight table table-striped table-bordered table-hover']//tr[1]/th"))
#print("No. of rows: ",cols)

#2)Read specific row or cols data
data = driver.find_element(By.XPATH,"//table[@class='-striped -highlight table table-striped table-bordered table-hover']//tr[2]/td[4]")
#print("Data: ",data.text)

#3)Read all rows & cols data
#Approach 1
data = driver.find_elements(By.XPATH,"//table[@class='-striped -highlight table table-striped table-bordered table-hover']//tr/td")
#for i in data:
   # print("Data: ",i.text)


#Approach 2
#for r in range(1,rows+ 1):
   # for c in range(1, cols+ 1):
       # data = driver.find_element(By.XPATH,"//table[@class='-striped -highlight table table-striped table-bordered table-hover']//tr["+str(r)+"]/td["+str(c)+"]").text
       # print(data)

#4) Read data based on conditions
for r in range(1,rows):
    data1 = driver.find_element(By.XPATH,"//table[@class='-striped -highlight table table-striped table-bordered table-hover']//tbody/tr["+str(r)+"]/td[3]").text
    if int(data1) >= 30:
        data2 = driver.find_element(By.XPATH,"//table[@class='-striped -highlight table table-striped table-bordered table-hover']//tbody/tr[" + str(r) + "]/td[5]").text
        print("Age: ",data1,"Salary: ",data2)


