from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import os

loc = os.path.abspath(os.getcwd()) #get current location
from time import sleep

# Chrome driver settings to download files in default location
'''def chrome_setup():
    #download files in desired locations
    preferences={"download.default_directory":loc}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(options=ops)
    return driver'''

# Edge driver settings to download files in default location
def edge_setup():
    #download files in desired locations
    preferences={"download.default_directory":loc}
    ops=webdriver.EdgeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Edge(options=ops)
    return driver

#Firefox driver settings to download files in default location
def firefox_setup():
    #download files in desired locations
    op = webdriver.FirefoxOptions()
    op.set_preference("browser.helprApps;neverAsk:saveToDisk","application/msword")#MIME Type website
    op.set_preference("browser.download.manger,showWhenStarting", False)
    op.set_preference("browser.download.folderList",2)#0-desktop 1-downloads 2-Desired loaction
    op.set_preference("browser.download.dir", loc)# for desired location only
    driver = webdriver.Firefox()
    return driver

#driver1=chrome_setup()
driver1=edge_setup()
driver1.get("https://demo.automationtesting.in/FileUpload.html")
driver1.maximize_window()
driver1.find_element(By.XPATH,"//a[@type='button']").click()
sleep(2)
driver1.close()