import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import Login
from pageObjects.addCostumerPage import AddCustomer as ADC
import os
from utilities.readProperties import ReadConfig as RF
from utilities.costumLogger import LogGen as LG
from utilities import excelUtils as EXC
import string
import random
from selenium.webdriver.common.by import By



class TestAddCustomer003:
    baseURL = RF.getApplicationURL()
    username = RF.getUserEmail()
    password = RF.getUserPassword()
    logger = LG.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info('***** Test_003_Add Customer *****')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginBtn()
        self.logger.info('***** Login successful *****')
        self.logger.info('***** Starting Add Customer test *****')

        self.addCust = ADC(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()
        self.addCust.clickOnAddNew()

        self.logger.info('***** Providing customer info *****')

        # self.email = random_generator() + "@gmail.com"
        self.email = self.addCust.random_generator_in_adp(size=8, chars=string.ascii_lowercase + string.digits) + "@live.com"
        # self.email = self.addCust.email_generator()

        self.addCust.setEmail(self.email)
        self.addCust.setPassword(self.password)
        self.addCust.setFirstName('Davud')
        self.addCust.setLastName('Gobeljic')
        self.addCust.setGender('Male')
        self.addCust.setDateOfBirth('8/24/1990')
        self.addCust.setCompanyName('Herbakus')
        self.addCust.clickTaxSubmit()
        self.addCust.setCustomersRoles('guest')
        # self.addCust.setVendorsManager('1')
        self.addCust.setVendorsManagerPartTwo('Vendor 1')
        self.addCust.clickOnSave()


        self.logger.info('***** Saving customer info *****')

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        # print(self.msg)

        if 'The new customer has been added successfully.' in self.msg:
            assert True
            # assert True == True
            self.logger.info('***** Add customer test PASSED *****')
        else:
            self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                     '/Users/davud/PycharmProjects/hybridFramework_mac/screenshots/test_addCustomer',
                                                     self.addCust.random_generator_in_adp(size=4, chars=string.ascii_lowercase + string.digits) + "_TestAddCustomer003.png"))
            self.logger.error('***** Add customer test FAILED *****')
            assert False
            # assert True == False

        self.driver.close()
        self.logger.info('***** ENDING ADD CUSTOMER TEST *****')
        





    #  pytest -v -s --html=/Users/davud/PycharmProjects/hybridFramework_mac/reports/report_test_addCustomer.html /Users/davud/PycharmProjects/hybridFramework_mac/testCases/test_addCustomer.py --browser chrome