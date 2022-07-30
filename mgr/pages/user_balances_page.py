import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.page import BasePage


class UserBalances(BasePage):

    FILTERS = (By.ID, 'id="filter-roles__BV_toggle_"')
    EMAIL_FILTER = (By.XPATH, '//a[@value="email"]')
    NAME_FILTER = (By.XPATH, '//a[@value="display_name"]')
    INPUT_SEARCH = (By.XPATH, '//input[@class="search form-control form-control-sm"]')
    SEARCH_BUTTON = (By.XPATH, '//a[@class="btn-sm btn-secondary mr-2"]')

    EMAIL = (By.XPATH, '//td[@aria-colindex="1"]')
    NAME = (By.XPATH, '//td[@aria-colindex="2"]')
    BALANCE = (By.XPATH, '//td[@aria-colindex="4"]')

    SORTING_DISPLAY_NAME = (By.XPATH, '//th[@aria-colindex="2"]')
    SORTING_BALANCE = (By.XPATH, '//th[@aria-colindex="4"]')

    def search_filter(self, type_filter, value):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(UserBalances.FILTERS)).click()
        wait.until(EC.presence_of_element_located(type_filter)).click()
        input_search = wait.until(EC.presence_of_element_located(UserBalances.INPUT_SEARCH))
        input_search.clear()
        input_search.send_keys(value)
        wait.until(EC.presence_of_element_located(UserBalances.SEARCH_BUTTON)).click()
        time.sleep(10)

