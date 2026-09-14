from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def headless_chrome():
     ops = webdriver.ChromeOptions()
     ops.add_argument("--headless")
     driver = webdriver.Chrome(options=ops)
     return driver

def headless_edge():
    ops = webdriver.EdgeOptions()
    ops.add_argument("--headless")
    driver = webdriver.Edge(options=ops)
    return driver

def headless_firefox():
    ops = webdriver.FirefoxOptions()
    ops.add_argument("--headless")
    driver = webdriver.Firefox(options=ops)
    return driver

#driver1 = headless_chrome()
driver1 = headless_edge()

driver1.get("https://www.hotstar.com/in/home")
print(driver1.title)
print(driver1.current_url)