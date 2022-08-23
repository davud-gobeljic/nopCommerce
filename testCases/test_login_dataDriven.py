import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import Login
import os
from utilities.readProperties import ReadConfig as RF
from utilities.costumLogger import LogGen as LG
from utilities import excelUtils as EXC


class Test_002_dataDriven_Login:
    baseURL = RF.getApplicationURL()
    path = "/Users/davud/PycharmProjects/hybridFramework_mac/testData/dataDriven.xlsx"
    logger = LG.loggen()

    def test_login_dataDriven(self, setup):
        self.logger.info('************* Test_002 Data Driven Login *************')
        self.logger.info('************* Verifying Data Driven Login test *************')
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)

        self.rows = EXC.getRowCount(self.path, 'sh1')
        print("Number of rows in a Excel", self.rows)

        lst_status = []   # Empty list variable

        for r in range(3, self.rows + 1):
            self.userName = EXC.readData(self.path, 'sh1', r, 1)
            self.password = EXC.readData(self.path, 'sh1', r, 2)
            self.exp = EXC.readData(self.path, 'sh1', r ,3)

            self.lp.setUserName(self.userName)
            self.lp.setPassword(self.password)
            self.lp.clickLoginBtn()
            time.sleep(2)

            act_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info('***** Pass *****')
                    self.lp.clickLogoutBtn()
                    lst_status.append('Pass')
                elif self.exp == 'Fail':
                    self.logger.info('***** Fail *****')
                    self.lp.clickLogoutBtn()
                    lst_status.append('Fail')
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info('***** Fail *****')
                    lst_status.append('Fail')
                elif self.exp == 'Fail':
                    self.logger.info('***** Pass *****')
                    lst_status.append('Pass')



        # if "Fail" not in lst_status:
        #     self.logger.info('********* Login Data Driven test is Pass **********')
        #     self.driver.close()
        #     assert True
        # else:
        #     self.logger.info('********* Login Data Driven test is Pass **********')
        #     self.driver.close()
        #     assert False
        #
        #
        # self.logger.info('***** End of Login Data Driven test *****')
        # self.logger.info('********** Completed Test_002_dataDriven_Login **********')




# choosing chrome driver
# pytest -v -s /Users/davud/PycharmProjects/hybridFramework_mac/testCases/test_login.py --browser chrome


# parallel tests
# pytest -s -v n=2 /Users/davud/PycharmProjects/hybridFramework_mac/testCases/test_login.py --browser chrome
# n=2 or n=3 means on how many browser we want to run our test

# HTML report included in a full command
# pytest -s -v n=3 --html=/Users/davud/PycharmProjects/hybridFramework_mac/reports/report.html /Users/davud/PycharmProjects/hybridFramework_mac/testCases/test_login.py --browser chrome
