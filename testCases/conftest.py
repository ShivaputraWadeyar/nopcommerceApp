import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver =webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['Project Name'] = "nop Commerce"
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Shiva'
