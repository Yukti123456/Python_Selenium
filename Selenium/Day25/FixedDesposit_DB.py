from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.implicitly_wait(10)
import mysql.connector
select_query = "select * from calculator1"
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

try:
    con = mysql.connector.connect(host="localhost",
                                  user="root",
                                  port="3306",
                                  password="Root@123",
                                  database="company_database",
                                  use_pure=True)
    curs= con.cursor()
    curs.execute(select_query)
    for row in curs:
          principle =  row[0]
          rate =  row[1]
          period1= row[2]
          period2 = row[3]
          fre = row[4]
          exp_value = row[5]

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


          else:
              print("test Failed")
              sleep(2)
          driver.find_element(By.XPATH,"//img[@class='PL5']").click()
          sleep(2)
    con.close()
except:
    print("Connect Error")

driver.close()
