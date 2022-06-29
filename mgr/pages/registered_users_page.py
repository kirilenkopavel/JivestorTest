import random
import time

from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.page import BasePage


class RegisteredUsers(BasePage):

    REGISTERED_USERS_TAB = (By.ID, 'li-registered_users')
    FILTER_ROLES = (By.ID, 'filter-roles__BV_toggle_')
    ROLES = (By.XPATH, '//div[@id="filter-roles"]//a[@role="menuitem"]')
    FULL_NAME = (By.XPATH, '//tr[@role="row"]/td[@aria-colindex="4"]')
    EMAIL = (By.XPATH, '//tr[@role="row"]/td[@aria-colindex="5"]')
    ALL_ROLES = '//a[contains(text(), \'Show all roles\')]'
    ADMINISTRATOR = '//a[contains(text(), \'Administrator\')]'
    REGISTERED = '//a[contains(text(), \'Registered\')]'
    PUBLIC = '//a[contains(text(), \'Public\')]'
    WL_MANAGER = '//a[contains(text(), \'WhiteLabelManager\')]'
    BUSINESS_DEVELOPER = '//a[contains(text(), \'BusinessDeveloper\')]'
    PRODUCT_MANAGER = '//a[contains(text(), \'ProductManager\')]'
    ACCOUNTANT = '//a[contains(text(), \'Accountant\')]'
    FILTER_SEARCH = (By.XPATH, '//div[@class="data-filters__field"]/div[2]/button')
    SEARCH_NAME = (By.XPATH, '//a[@value="display_name"]')
    SEARCH_EMAIL = (By.XPATH, '//a[@value="email"]')
    INPUT_SEARCH = (By.XPATH, '//input[@class="search form-control form-control-sm"]')
    SEARCH_BUTTON = (By.XPATH, '//a[@class="btn-sm btn-secondary mr-2"]')
    NUMBERS_PAGE = (By.XPATH, '//button[@role="menuitemradio"]')
    BLOCKED = (By.XPATH, '//label[@for="checkbox-1"]')
    EDIT_USER = (By.XPATH, '//a[@class="btn-sm btn-success"]')
    BLOCKED_BUTTON = (By.XPATH, '//a[@class="btn-sm btn-dark ml-1"]')
    VERIFIED_BUTTON = (By.XPATH, "//a[contains(text(), 'Verified')]")
    UNVERIFIED_BUTTON = (By.XPATH, "//a[contains(text(), 'Unverified')]")
    SORTING_DATE = (By.XPATH, '//th[@aria-colindex="3"]/div')
    SORTING_LAST_ACCESS = (By.XPATH, '//th[@aria-colindex="10"]/div')

    USERNAME_INPUT = (By.ID, 'username')
    FIRST_NAME_INPUT = (By.ID, 'firstname')
    LAST_NAME_INPUT = (By.ID, 'lastname')
    REGION_INPUT = (By.ID, 'region')
    PHONE_INPUT = (By.ID, 'phone')
    ZIP_CODE_INPUT = (By.ID, 'zipcode')
    ADDRESS_INPUT = (By.ID, 'address')
    CITY_INPUT = (By.ID, 'city')
    COMPANY_INPUT = (By.ID, 'company-name')

    COUNTRY_LIST = (By.ID, 'country')
    UPDATE_SETTINGS = (By.ID, 'update-user-submit')

    def selection_role(self, role):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(RegisteredUsers.FILTER_ROLES)).click()
        name_role = wait.until(EC.presence_of_element_located((By.XPATH, role))).text
        wait.until(EC.presence_of_element_located((By.XPATH, role))).click()
        time.sleep(9)
        return name_role

    def collect_table(self, element):
        wait = WebDriverWait(self.driver, 5)
        names = list()
        try:
            elements = wait.until(EC.presence_of_all_elements_located(element))
            for name in elements:
                names.append(name.text)
                return names
        except TimeoutException:
            return names

    def search_filter(self, filter_type, value):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(RegisteredUsers.FILTER_SEARCH)).click()
        wait.until(EC.presence_of_element_located(filter_type)).click()
        input_search = wait.until(EC.presence_of_element_located(RegisteredUsers.INPUT_SEARCH))
        input_search.clear()
        input_search.send_keys(value)
        wait.until(EC.presence_of_element_located(RegisteredUsers.SEARCH_BUTTON)).click()
        time.sleep(9)

    def show_blocked(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(RegisteredUsers.BLOCKED)).click()
        time.sleep(5)

    def open_edit_user(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(RegisteredUsers.EDIT_USER)).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        time.sleep(5)

    def edit_input(self, input_type, value):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(input_type))
        element.clear()
        element.send_keys(value)
        return self

    def edit_user_input(self):
        i = ''
        value = list()
        for x in range(6):
            value.append(i + str(random.randrange(9)))
        RegisteredUsers(self.driver).edit_input(RegisteredUsers.USERNAME_INPUT, value) \
            .edit_input(RegisteredUsers.FIRST_NAME_INPUT, value) \
            .edit_input(RegisteredUsers.LAST_NAME_INPUT, value) \
            .edit_input(RegisteredUsers.REGION_INPUT, value) \
            .edit_input(RegisteredUsers.PHONE_INPUT, value) \
            .edit_input(RegisteredUsers.ZIP_CODE_INPUT, value) \
            .edit_input(RegisteredUsers.ADDRESS_INPUT, value) \
            .edit_input(RegisteredUsers.CITY_INPUT, value) \
            .edit_input(RegisteredUsers.COMPANY_INPUT, value)
        return value

    def update_settings(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(RegisteredUsers.UPDATE_SETTINGS)).click()







