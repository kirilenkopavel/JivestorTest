import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.page import BasePage


class WhoFollowsWhom(BasePage):

    FILTERS = (By.ID, 'filter-roles__BV_toggle_')
    ACCOUNT_FILTER = (By.XPATH, "//a[contains(text(), 'Search by Account')]")
    EMAIL_FILTER = (By.XPATH, "//a[contains(text(), 'Search by Email')]")
    DISPLAY_NAME_FILTER = (By.XPATH, "//a[contains(text(), 'Search by Display name')]")
    TRADING_STRATEGY_FILTER = (By.XPATH, "//a[contains(text(), 'Search by Trading Strategy')]")
    INPUT_SEARCH = (By.XPATH, '//input[@class="search form-control form-control-sm"]')
    SEARCH_BUTTON = (By.XPATH, '//a[@class="btn-sm btn-secondary mr-2"]')
    ACTIV_STATUS = (By.XPATH, '//div[@class="data-fields-in-row-after__field"]/div/div/div[1]')
    INACTIV_STATUS = (By.XPATH, '//div[@class="data-fields-in-row-after__field"]/div/div/div[2]')
    LIVE_ACCOUNTS_TAB = (By.XPATH, "//span[contains(text(), 'Live accounts')]")
    DEMO_ACCOUNTS_TAB = (By.XPATH, "//span[contains(text(), 'Demo accounts')]")
    SORTING_DATE = (By.XPATH, '//th[@aria-colindex="2"]/div')
    SORTING_DISPLAY_NAME = (By.XPATH, '//th[@aria-colindex="3"]/div')
    ACCOUNT = (By.XPATH, '//td[@aria-colindex="5"]')
    DISPLAY_NAME = (By.XPATH, '//td[@aria-colindex="3"]')
    TRADING_STRATEGY = (By.XPATH, '//td[@aria-colindex="4"]')

    def search_filter(self, type_filter, value):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(WhoFollowsWhom.FILTERS)).click()
        wait.until(EC.presence_of_element_located(type_filter)).click()
        input_search = wait.until(EC.presence_of_element_located(WhoFollowsWhom.INPUT_SEARCH))
        input_search.clear()
        input_search.send_keys(value)
        wait.until(EC.presence_of_element_located(WhoFollowsWhom.SEARCH_BUTTON)).click()
        time.sleep(10)

    def switch(self, tab):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(tab)).click()
        time.sleep(5)
