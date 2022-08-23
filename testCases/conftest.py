import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        service_obj = Service("/Users/davud/selenium/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
    elif browser == 'firefox':
        service_obj = Service("/Users/davud/selenium/geckodriver")
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
    elif browser == 'opera':
        service_obj = Service("/Users/davud/selenium/opera")
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
    elif browser == 'safari':
        service_obj = Service("/Users/davud/selenium/safari")
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
    elif browser == 'edge':
        service_obj = Service("/Users/davud/selenium/edge")
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
    else:
        service_obj = Service("/Users/davud/selenium/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
    return driver

def pytest_addoption(parser): # this will get value from CLI / hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the browser value to setup method
    return request.config.getoption("--browser")


# **************** HTML report ******************

# It is hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nopCommerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['QA Engineer'] = 'Davud Gobeljic'

# It is hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
