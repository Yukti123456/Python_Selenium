from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import ExcelUtils
driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

file = "caldata.xlsx"
rows = ExcelUtils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
  principle =  ExcelUtils.readData(file,"Sheet1",r,1)
  rate = ExcelUtils.readData(file,"Sheet1",r,2)
  period1= ExcelUtils.readData(file, "Sheet1", r, 3)
  period2 = ExcelUtils.readData(file, "Sheet1", r, 4)
  fre = ExcelUtils.readData(file, "Sheet1", r, 5)
  exp_value = ExcelUtils.readData(file, "Sheet1", r, 6)
  #passing data to the application
  driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(principle)
  driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rate)
  driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(period1)
  periodDrp = Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
  periodDrp.select_by_visible_text(period2)
  freDrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
  freDrp.select_by_visible_text(fre)
  driver.execute_script("""
      var overlay = document.querySelector('.wzrk-overlay');
      if (overlay) {
          overlay.remove();
      }
  """)
  #Calculate Button
  driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()
  actual_Result = driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text
  #Validation
  if float(exp_value) == float(actual_Result):
      print("test Passed")
      ExcelUtils.writeData(file,"Sheet1",r,8,"Passed")
      ExcelUtils.fillGreenColor(file,"Sheet1",r,8)

  else:
      print("test Failed")
      ExcelUtils.writeData(file,"Sheet1",r,8,"Failed")
      ExcelUtils.fillRedColor(file, "Sheet1", r, 8)
      sleep(2)
  driver.find_element(By.XPATH,"//img[@class='PL5']").click()



m