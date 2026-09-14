from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCLI:
    def test_Logo(self,setup):
        self.driver = setup
        try:
           self.status = self.driver.find_element(By.XPATH,"//img[@alt='Practice Test Automation']").is_displayed()
           self.driver.close()
           assert self.status == True
        except:
            self.driver.close()
            assert False

    def test_Login(self,setup):
            try:
                self.driver=setup
                self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys("student")
                self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Password123")
                self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
                sleep(2)
                logout = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//a[normalize-space()='Log out']")
                    )
                )
            finally:
                self.driver.quit()