from pytz import country_names
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
wait = WebDriverWait(driver, 10)
driver.maximize_window()
name = wait.until(
    EC.visibility_of_element_located((By.ID, "name"))
)
name.send_keys("Yukti Sahu")
sleep(2)
email = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@id='email']"))
)
email.send_keys("yuktisahu021@gmail.com")
sleep(2)
phone = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@id='phone']"))
)
phone.send_keys("8709500657")

textarea = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//textarea[@id='textarea']"))
)
textarea.send_keys("Vijay Nagar,Indore")
sleep(2)
female = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@id='female']"))
)
female.click()
sleep(2)
checkboxes = driver.find_elements(
    By.XPATH, "//div[@class='form-group']"
)
for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()
sleep(2)
country = Select(driver.find_element(By.XPATH,"//select[@id='country']"))
country.select_by_visible_text("India")
sleep(2)
colors = Select(driver.find_element(By.XPATH,"//select[@id='colors']"))
colors.select_by_visible_text("Red")
sleep(2)
animal = Select(driver.find_element(By.XPATH,"//select[@id='animals']"))
animal.select_by_visible_text("Dog")
sleep(2)
DOB1 = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@id='datepicker']"))
)
DOB1.send_keys("08/02/2026")

sleep(2)
DOB2 = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//input[@id='txtDate']"))
)
DOB2.send_keys("08/07/2026")
female.click()
sleep(2)
driver.quit()