import pytest
from selenium import webdriver
from pageObjects.loginPage import Login
import os
from utilities.readProperties import ReadConfig as RF
from utilities.costumLogger import LogGen as LG
from pageObjects.addCostumerPage import AddCustomer as ADC
import string
import random


class Test_001_Login:
    baseURL = RF.getApplicationURL()
    username = RF.getUserEmail()
    password = RF.getUserPassword()

    logger = LG.loggen()

    @pytest.mark.regression
    def test_homePage(self, setup):
        self.logger.info('************* Test_001_Login *************')
        self.logger.info('************* Verifying Home Page Title *************')
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == 'Your store. Login':
            assert True
            self.driver.close()
            self.logger.info('************* Home Page title test is passed *************')
        else:
            self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                     '/Users/davud/PycharmProjects/hybridFramework_mac/screenshots/test_login',
                                                     self.addCust.random_generator_in_adp(size=4,chars=string.ascii_lowercase + string.digits) + '_title_001.png'))
            self.driver.close()
            self.logger.error('************* Home Page title test is failed *************')
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info('************* Verifying Login test *************')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginBtn()

        self.addCust = ADC(self.driver)


        act_title = self.driver.title
        if act_title == 'Dashboard / nopCommerce administration':
            assert True
            self.logger.info('************* Login Test is passed *************')
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                     '/Users/davud/PycharmProjects/hybridFramework_mac/screenshots/test_login',
                                                     self.addCust.random_generator_in_adp(size=4,chars=string.ascii_lowercase + string.digits) + '_testLogin_001_title.png'))
            self.driver.close()
            self.logger.error('************* Login Test is failed *************')
            assert False


# choosing chrome driver
# pytest -v -s /Users/davud/PycharmProjects/hybridFramework_mac/testCases/test_login.py --browser chrome


# parallel tests
# pytest -s -v n=2 /Users/davud/PycharmProjects/hybridFramework_mac/testCases/test_login.py --browser chrome
# n=2 or n=3 means on how many browser we want to run our test

# HTML report included in a full command
# pytest -s -v n=3 --html=/Users/davud/PycharmProjects/hybridFramework_mac/reports/report.html /Users/davud/PycharmProjects/hybridFramework_mac/testCases/test_login.py --browser chrome
