import time
import pytest
from pageObjects.loginPage import Login
from pageObjects.addCostumerPage import AddCustomer
from pageObjects.search_customerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.costumLogger import LogGen

class Test_SearchCustomerByName_006():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByName(self, setup):
        self.logger.info('***** Test_003_Add Customer by Name *****')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginBtn()
        self.logger.info('***** Login successful *****')

        self.logger.info('***** Starting Search Customer By Name Test *****')

        self.adjust = AddCustomer(self.driver)
        self.adjust.clickOnCustomersMenu()
        self.adjust.clickOnCustomersMenuItem()
        time.sleep(2)

        self.logger.info('***** searching customer by Name *****')
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName('James')
        searchcust.setLastName('Pan')
        searchcust.clickSearchBTN()
        time.sleep(3)
        status = searchcust.searchCustomerByName('James Pan')
        self.driver.close()
        # assert True == status
        if status == True:
            assert True
        else:
            assert False
        self.logger.info('***** Search customer by Name Test in Finished *****')


# pytest -s -v --html=/Users/davud/PycharmProjects/hybridFramework_mac/reports/report_test_findCustomerByName.html /Users/davud/PycharmProjects/hybridFramework_mac/testCases/test_searchCustomerByName.py --browser chrome
# pytest -s -v -m "regression and sanity" (-m is for mark test like regression)
# pytest -s -v -m "sanity" --html=/Users/davud/PycharmProjects/hybridFramework_mac/reports/report_sanity.html /Users/davud/PycharmProjects/hybridFramework_mac/testCases --browser chrome