from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
country_list = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(country_list))

for country in country_list:
    if country.text == "India":
        country.click()
        break
sleep(2)
driver.close()