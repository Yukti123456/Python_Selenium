from selenium import webdriver
from selenium.webdriver.common.by import By
import os
loc = os.path.abspath(os.getcwd()) #get current location
from time import sleep

# Chrome driver settings to download files in default location
def chrome_setup():
    #download files in desired locations
    preferences={"download.default_directory":loc,"plugins.always_open_pdf_externally":True}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(options=ops)
    return driver

# Edge driver settings to download files in default location
def edge_setup():
    #download files in desired locations
    preferences={"download.default_directory":loc,"plugins.always_open_pdf_externally":True} #additional setting for PDF
    ops=webdriver.EdgeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Edge(options=ops)
    return driver

#Firefox driver settings to download files in default location
def firefox_setup():
    #download files in desired locations
    op = webdriver.FirefoxOptions()
    op.set_preference("browser.helprApps;neverAsk:saveToDisk","application/pdf")#MIME Type website
    op.set_preference("browser.download.manger,showWhenStarting", False)
    op.set_preference("browser.download.folderList",2)#0-desktop 1-downloads 2-Desired loaction
    op.set_preference("browser.download.dir", loc)# for desired location only
    op.set_preference("pdfjs.disabled", True) # for pdf download
    driver = webdriver.Firefox()
    return driver

driver = chrome_setup()
#driver = edge_setup()
driver.get("https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf")
driver.maximize_window()
driver.close()


