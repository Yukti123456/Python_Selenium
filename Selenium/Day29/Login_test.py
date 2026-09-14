from selenium import webdriver
from LoginPageObject import LoginPage

from Selenium.Day29.LoginPageObject import LoginPage


class TestLogin:
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.maximize_window()

        self.l1=LoginPage(self.driver)
        self.l1.setUserName("student")
        self.l1.setPassword(" Password123")
        self.l1.clickBtn()
        self.act_tittle = self.driver.title
        self.driver.close()
        assert self.act_tittle == "Test Login | Practice Test Automation"
