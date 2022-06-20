import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.page import BasePage


class RegisteredUsers(BasePage):

    REGISTERED_USERS_TAB = (By.ID, 'li-registered_users')
    FILTER_ROLES = (By.ID, 'filter-roles__BV_toggle_')
    ROLES = (By.XPATH, '//div[@id="filter-roles"]//a[@role="menuitem"]')
    FULL_NAME = (By.XPATH, '//tr[@role="row"]/td[@aria-colindex="4"]')
    ALL_ROLES = '//a[contains(text(), \'Show all roles\')]'
    ADMINISTRATOR = '//a[contains(text(), \'Administrator\')]'
    REGISTERED = '//a[contains(text(), \'Registered\')]'
    PUBLIC = '//a[contains(text(), \'Public\')]'
    WL_MANAGER = '//a[contains(text(), \'WhiteLabelManager\')]'
    BUSINESS_DEVELOPER = '//a[contains(text(), \'BusinessDeveloper\')]'
    PRODUCT_MANAGER = '//a[contains(text(), \'ProductManager\')]'
    ACCOUNTANT = '//a[contains(text(), \'Accountant\')]'

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
