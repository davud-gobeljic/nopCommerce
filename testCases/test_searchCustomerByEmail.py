import time
import pytest
from pageObjects.loginPage import Login
from pageObjects.addCostumerPage import AddCustomer
from pageObjects.search_customerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.costumLogger import LogGen

class Test_SearchCustomerByEmail_005():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByEmail(self, setup):
        self.logger.info('***** Test_003_Add Customer *****')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginBtn()
        self.logger.info('***** Login successful *****')

        self.logger.info('***** Starting Search Customer By Email Test *****')

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(2)

        self.logger.info('***** searching customer by emailID *****')
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail('james_pan@nopCommerce.com')
        searchcust.clickSearchBTN()
        time.sleep(2)
        status = searchcust.searchCustomerByEmail('james_pan@nopCommerce.com')
        assert True == status
        self.logger.info('***** Search customer by Email Test in Finished *****')

        self.driver.close()







