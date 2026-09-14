import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_Login:

    def test_login_chrome(self):
         #from selenium.webdriver.chrome import webdriver
         self.driver = webdriver.Chrome()
         self.driver.get("https://practicetestautomation.com/practice-test-login/")
         self.driver.maximize_window()
         self.driver.find_element(By.XPATH,"//input[@id='username']").send_keys("student")
         self.driver.find_element(By.XPATH,"//input[@id='password']").send_keys(" Password123")
         self.driver.find_element(By.XPATH,"//button[@id='submit']").click()
         assert self.driver.title == "Test Login | Practice Test Automation"
         self.driver.quit()

    def test_login_edge(self):
        #from selenium.webdriver.edge import webdriver
        self.driver = webdriver.Edge()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.find_element(By.XPATH,"//input[@id='username']").send_keys("student ")
        self.driver.find_element(By.XPATH,"//input[@id='password']").send_keys(" Password123")
        self.driver.find_element(By.XPATH,"//button[@id='submit']").click()
        assert self.driver.title == "Test Login | Practice Test Automation"
        self.driver.quit()


