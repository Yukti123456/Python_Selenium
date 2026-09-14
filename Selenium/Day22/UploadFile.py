from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/FileUpload.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='input-4']").send_keys(r"C:\Users\yukti\PycharmProjects\PythonProject3\Selenium\Day22\sample-local-pdf.pdf")
sleep(2)
driver.close()