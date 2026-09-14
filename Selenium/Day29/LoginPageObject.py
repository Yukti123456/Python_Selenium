from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    #Locators  --->>> contain one page element
    username= "//input[@id='username']"
    password= "//input[@id='password']"
    button=   "//button[@id='submit']"

    #Constructor
    def __init__(self, driver):
        self.driver=driver

    #Actions methods
    def setUserName(self,username1):
        self.driver.find_element(By.XPATH, self.username).send_keys(username1)

    def setPassword(self,password1):
        self.driver.find_element(By.XPATH, self.password).send_keys(password1)

    def clickBtn(self):
        self.driver.find_element(By.XPATH, self.button).click()


