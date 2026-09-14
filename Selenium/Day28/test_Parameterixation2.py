import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestClass:
    @pytest.mark.parametrize('user,pwd',
                             [("Admin","admin123"),
                              ("student","Password123"),
                              ("Abc","Password123"),
                              ("student","123@123")]
                             )
    def test_Login(self,user,pwd):
        try:
           self.driver = webdriver.Chrome()
           self.driver.get("https://practicetestautomation.com/practice-test-login/")
           self.driver.maximize_window()
           self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(user)
           self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(pwd)
           self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
           sleep(2)
           logout = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//a[normalize-space()='Log out']")
                )
           )

           assert logout.is_displayed()
        finally:
            self.driver.quit()
