from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
ops = webdriver.ChromeOptions()

# Disable browser notifications
ops.add_argument("--disable-notifications")

# Block geolocation permission
prefs = {
    "profile.default_content_setting_values.geolocation": 2
}#Block locaion popups

ops.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=ops)

driver.get("https://www.where-am-i.co/track-my-location")
driver.maximize_window()
sleep(2)
driver.close()