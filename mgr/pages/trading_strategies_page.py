import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.page import BasePage


class TradingStrategies(BasePage):

    FILTERS = (By.XPATH, '//div[@class="main-content-block__row"]/div[1]//button')
    STRATEGY_NAME_FILTER = (By.XPATH, "//a[contains(text(), 'Search by Strategy Name')]")
    TRADER_FILTER = (By.XPATH, "//a[contains(text(), 'Search by Trader')]")
    STRATEGY_ID_FILTER = (By.XPATH, "//a[contains(text(), 'Search by Strategy ID')]")
    EMAIL_FILTER = (By.XPATH, "//a[contains(text(), 'Search by E-mail')]")
    ACCOUNT_FILTER = (By.XPATH, "//a[contains(text(), 'Search by Account')]")

    STATUSES = (By.XPATH, '//div[@class="main-content-block__row"]/div[3]//button')
    ACTIV_STATUS = (By.XPATH, "//a[contains(text(), 'Active')]")
    INVISIBLE_STATUS = (By.XPATH, "//div[@id=\"filter-roles\"]//a[contains(text(), 'Invisible')]")
    DISQUALIFIED_STATUS = (By.XPATH, "//a[contains(text(), 'Disqualified')]")
    PRO_STATUS = (By.XPATH, "//div[@id=\"filter-roles\"]//a[contains(text(), 'Pro')]")
    HIGH_RISK_STATUS = (By.XPATH, "//a[contains(text(), 'High risk')]")
    DEMO_STATUS = (By.XPATH, "//div[@id=\"filter-roles\"]//a[contains(text(), 'Demo')]")
    DISABLED_STATUS = (By.XPATH, "//a[contains(text(), 'Disabled')]")

    FILTERS_STATUSES = (By.XPATH, '//div[@class="main-content-block__row"]/div[4]//button')
    ALL_FILTER = (By.XPATH, "//div[@class=\"main-content-block__row\"]/div[4]//a[contains(text(), 'All')]")
    INACTIVE_15_FILTER = (By.XPATH, "//a[contains(text(), 'Incative 15+ days')]")
    INACTIVE_30_FILTER = (By.XPATH, "//a[contains(text(), 'Incative 30+ days')]")
    EQUITY_95_FILTER = (By.XPATH, "//a[contains(text(), 'Equity drawdown 95%+')]")
    EQUITY_100_FILTER = (By.XPATH, "//a[contains(text(), 'Equity drawdown 100%')]")

    INPUT_SEARCH = (By.XPATH, '//input[@class="search form-control form-control-sm"]')
    SEARCH_BUTTON = (By.XPATH, '//a[@class="btn-sm btn-secondary mr-2"]')

    SORTING_DATE = (By.XPATH, '//th[@aria-colindex="2"]/div')
    SORTING_STRATEGY_NAME = (By.XPATH, '//th[@aria-colindex="3"]/div')
    SORTING_ACCOUNT = (By.XPATH, '//th[@aria-colindex="4"]/div')

    DATE = (By.XPATH, '//td[@aria-colindex="2"]')
    STRATEGY_NAME = (By.XPATH, '//td[@aria-colindex="3"]')
    ACCOUNT = (By.XPATH, '//td[@aria-colindex="4"]')
    TRADER = (By.XPATH, '//td[@aria-colindex="6"]')
    LIVE_FOLLOWERS = (By.XPATH, '//td[@aria-colindex="8"]/a')
    DEMO_FOLLOWERS = (By.XPATH, '//td[@aria-colindex="9"]/a')
    SETTINGS_BUTTON = (By.XPATH, '//div[@class="dropdown b-dropdown btn-group"]/button')
    MAKE_STATUS = (By.XPATH, '//div[@class="customIcons"]//ul[@role="menu"]/li[1]/a')
    DISQUALIFY = (By.XPATH, "//a[contains(text(), 'Disqualify')]")
    SUBMIT_BUTTON = (By.XPATH, "/button[contains(text(), 'Yes')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(text(), 'Close')]")

    COUNTER_TOTAL = (By.XPATH, '//div[@id="followers-block"]/div[@class="row"]/div[1]')
    DATE_FOLLOWERS = (By.XPATH, '//td[@aria-colindex="1"]')
    SORTING_DATE_FOLLOWERS = (By.XPATH, '//th[@aria-colindex="1"]')

    def search_filter(self, type_filter, value):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(TradingStrategies.FILTERS)).click()
        wait.until(EC.presence_of_element_located(type_filter)).click()
        input_search = wait.until(EC.presence_of_element_located(TradingStrategies.INPUT_SEARCH))
        input_search.clear()
        input_search.send_keys(value)
        wait.until(EC.presence_of_element_located(TradingStrategies.SEARCH_BUTTON)).click()
        time.sleep(10)

    def selection_status(self, status):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(TradingStrategies.STATUSES)).click()
        name_status = wait.until(EC.presence_of_element_located(status)).text
        wait.until(EC.presence_of_element_located(status)).click()
        wait.until(EC.presence_of_element_located(TradingStrategies.SEARCH_BUTTON)).click()
        time.sleep(9)
        return name_status

    def review_followers(self, type_followers):
        wait = WebDriverWait(self.driver, 10)
        strategies = wait.until(EC.presence_of_all_elements_located(type_followers))
        for strategy in strategies:
            value = strategy.text
            if value > '1':
                strategy.click()
                return value
                pass

    def change_visibility(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(TradingStrategies.SETTINGS_BUTTON)).click()
        status = wait.until(EC.presence_of_element_located(TradingStrategies.MAKE_STATUS)).text
        wait.until(EC.presence_of_element_located(TradingStrategies.MAKE_STATUS)).click()
        wait.until(EC.presence_of_element_located(TradingStrategies.SUBMIT_BUTTON)).click()
        return status



