import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Service Object Created instead of mentioning Chrome Path
#service = Service()
#driver = webdriver.Chrome(service=service)
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
wait = WebDriverWait(driver, 10)

username = wait.until(
    EC.visibility_of_element_located((By.NAME, "username"))
)
#driver.find_element(By.NAME,"username")
time.sleep(3)
username.send_keys("Admin")
password = wait.until(
    EC.visibility_of_element_located((By.NAME, "password"))
)
time.sleep(3)
password.send_keys("admin123")
Button = wait.until(
      EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))
)
time.sleep(3)
Button.click()
time.sleep(3)
t = driver.title
at = "OrangeHRM"
if at == t:
    print("Login test passed")
else:
    print("Login Test failed")
driver.close()