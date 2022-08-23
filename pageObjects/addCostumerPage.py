from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select as SEOLD
from selenium.webdriver.support.select import Select as SENEW
import random
import string
import secrets


class AddCustomer:
    customers_menu = "//a[@href='#']//p[contains(text(),'Customers')]"
    costumers_menu_item = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    customers_addNew_BTN = "//a[@class='btn btn-primary']"
    email_input_id = 'Email'
    password_input_id = 'Password'
    firstName_input_id = 'FirstName'
    lastName_input_id = 'LastName'
    maleGender_id = 'Gender_Male'
    femaleGender_id = 'Gender_Female'
    date_of_birth_input_id = 'DateOfBirth'
    companyName_id = 'Company'
    is_tax_exempt_id = 'IsTaxExempt'
    customers_roles_picker_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    customers_picker_admin = "//li[normalize-space()='Administrators']"
    customers_picker_forumModerators = "//li[normalize-space()='Forum Moderators']"
    customers_picker_guests = "//li[normalize-space()='Guests']"
    customers_picker_registered = "//li[@id='9f700c5b-f748-48fd-a491-101275503782']"
    customers_picker_vendors = "//li[contains(text(),'Vendors')]"
    customers_picker_delete = "//span[@title='delete']"
    manager_of_vendor_id = 'VendorId'
    active_input_id = "//input[@id='Active']"
    adminComment_id = "AdminComment"
    save_button_xpath = "//button[@name='save']"

    size = 8
    chars = string.ascii_lowercase + string.digits

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.customers_menu).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.costumers_menu_item).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.customers_addNew_BTN).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.email_input_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_input_id).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.firstName_input_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.lastName_input_id).send_keys(lastname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.maleGender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.femaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.maleGender_id).click()

    def setDateOfBirth(self, date):
        self.driver.find_element(By.ID, self.date_of_birth_input_id).send_keys(date)

    def setCompanyName(self, companyName):
        self.driver.find_element(By.ID, self.companyName_id).send_keys(companyName)

    def clickTaxSubmit(self):
        self.driver.find_element(By.ID, self.is_tax_exempt_id).click()

    def setCustomersRoles(self, role):
        self.driver.find_element(By.XPATH, self.customers_roles_picker_xpath).click()
        # time.sleep(3)
        if role == 'admin':
            self.listItem = self.driver.find_element(By.XPATH, self.customers_picker_admin)
        elif role == 'forum moderator':
            self.listItem = self.driver.find_element(By.XPATH, self.customers_picker_forumModerators)
        elif role == 'guest':
            # Here user can be Registered or Guest // ONLY one choice
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.customers_picker_delete).click()
            self.listItem = self.driver.find_element(By.XPATH, self.customers_picker_guests)
        elif role == 'register':
            self.listItem = self.driver.find_element(By.XPATH, self.customers_picker_registered)
        elif role == 'vendor' or 'vendors':
            self.listItem = self.driver.find_element(By.XPATH, self.customers_picker_vendors)
        else:
            self.listItem = self.driver.find_element(By.XPATH, self.customers_picker_guests)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.listItem)

    def setVendorsManager(self, value):
        drp = SEOLD(self.driver.find_element(By.ID, self.manager_of_vendor_id))
        # drp.select_by_visible_text(value)
        drp.select_by_index(value)

    def setVendorsManagerPartTwo(self, value):
        drp = SENEW(self.driver.find_element(By.ID, self.manager_of_vendor_id))
        drp.select_by_visible_text(value)


    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def random_generator_in_adp(self, size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    # import secrets
    # def email_generator():
    #     return f"{secrets.token_hex(8)}@gmail.com"

    def email_generator(self):
        return f"{secrets.token_hex(9)}@hotmail.com"

