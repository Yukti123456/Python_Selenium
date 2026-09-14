import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
    elif browser == 'edge':
        driver = webdriver.Edge()
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
    return driver
#from pytest docs---this will get the value from cLI
def pytest_addoption(parser):
    parser.addoption("--browser")
# will return the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#Customised HTML Report
def pytest_metadata(metadata):
    metadata["Project"] = "E-Commerce Application"
    metadata["Tester"] = "Yukti"
    metadata["Environment"] = "QA"
    metadata["Browser"] = "Chrome"




