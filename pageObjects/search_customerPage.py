from selenium.webdriver.common.by import By


class SearchCustomer():
    # Add customer page

    email_input_id = 'SearchEmail'
    firstName_input_id = 'SearchFirstName'
    lastName_input_id = 'SearchLastName'
    btn_search_customers_id = 'search-customers'

    tblSearchResults = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    table_row = "//table[@id='customers-grid']//tbody/tr"
    table_col = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.email_input_id).clear()
        self.driver.find_element(By.ID, self.email_input_id).send_keys(email)

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.firstName_input_id).clear()
        self.driver.find_element(By.ID, self.firstName_input_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.lastName_input_id).clear()
        self.driver.find_element(By.ID, self.lastName_input_id).send_keys(lastname)

    def clickSearchBTN(self):
        self.driver.find_element(By.ID, self.btn_search_customers_id).click()

    def getRowNum(self):
        return len(self.driver.find_elements(By.XPATH, self.table_row))

    def getColNum(self):
        return len(self.driver.find_elements(By.XPATH, self.table_col))

    def searchCustomerByEmail(self, Email):
        flag = False
        for r in range(1, self.getRowNum() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            email_id = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if email_id == Email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getRowNum() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag





