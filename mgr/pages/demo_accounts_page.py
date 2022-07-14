import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.page import BasePage


class DemoAccounts(BasePage):

    FILTERS = (By.ID, 'filter-roles__BV_toggle_')
    EMAIL_FILTER = (By.XPATH, "//a[contains(text(), 'Search by Email')]")
    ACCOUNT_FILTER = (By.XPATH, "//a[contains(text(), 'Search by Account')]")
    FULL_NAME_FILTER = (By.XPATH, "//a[contains(text(), 'Search by Full name')]")
    DISPLAY_NAME_FILTER = (By.XPATH, "//a[contains(text(), 'Search by Display name')]")
    INPUT_SEARCH = (By.XPATH, '//input[@class="search form-control form-control-sm"]')
    SEARCH_BUTTON = (By.XPATH, '//a[@class="btn-sm btn-secondary mr-2"]')
    FULL_NAME = (By.XPATH, '//td[@aria-colindex="3"]')
    DISPLAY_NAME = (By.XPATH, '//td[@aria-colindex="4"]')
    EMAIL = (By.XPATH, '//td[@aria-colindex="5"]')
    ACCOUNT = (By.XPATH, '//td[@aria-colindex="6"]')
    EXPIRATION = (By.XPATH, '//td[@aria-colindex="7"]')
    EXTEND_BUTTON = (By.XPATH, '//a[@title="Extend demo account"]')
    SORTING_DATE = (By.XPATH, '//th[@aria-colindex="2"]')
    SORTING_FULL_NAME = (By.XPATH, '//th[@aria-colindex="3"]')
    SORTING_DISPLAY_NAME = (By.XPATH, '//th[@aria-colindex="4"]')
    SORTING_EMAIL = (By.XPATH, '//th[@aria-colindex="5"]')
    SORTING_ACCOUNT = (By.XPATH, '//th[@aria-colindex="6"]')
    CLOSE_BUTTON = (By.XPATH, '//div[@id="modal-window-success-extend___BV_modal_body_"]/button')

    def search_filter(self, type_filter, value):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(DemoAccounts.FILTERS)).click()
        wait.until(EC.presence_of_element_located(type_filter)).click()
        input_search = wait.until(EC.presence_of_element_located(DemoAccounts.INPUT_SEARCH))
        input_search.clear()
        input_search.send_keys(value)
        wait.until(EC.presence_of_element_located(DemoAccounts.SEARCH_BUTTON)).click()
        time.sleep(10)

    def extend_account(self):
        wait = WebDriverWait(self.driver, 10)
        accounts = wait.until(EC.presence_of_all_elements_located(DemoAccounts.EXPIRATION))
        for account in accounts:
            value = account.text
            if value != '30':
                wait.until(EC.presence_of_element_located(DemoAccounts.EXTEND_BUTTON)).click()
                time.sleep(3)
                wait.until(EC.presence_of_element_located(DemoAccounts.CLOSE_BUTTON)).click()
                return account.text
                pass
