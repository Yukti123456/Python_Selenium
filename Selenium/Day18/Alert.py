from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://demoqa.com/alerts")
driver.maximize_window()

# Click Alert with Textbox
driver.find_element(By.XPATH,"//button[@id='promtButton']").click()
sleep(3)

#Switch to alert
alertwindow=  driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("Welcome")
sleep(3)
#alertwindow.accept()
alertwindow.dismiss()
sleep(3)
driver.quit()