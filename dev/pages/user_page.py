import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dev.pages.page import BasePage


class UserPage(BasePage):

    PORTFOLIO_TAB = (By.XPATH, '//a[@ui-sref="menuLayout.platform.portfolio"]')
    STRATEGIES_TAB = (By.XPATH, '//a[@ui-sref="menuLayout.tradeRatingMain"]')
    TRADING_TERMINAL_TAB = (By.XPATH, '//a[@ui-sref="menuLayout.platform.terminal"]')
    STATEMENTS_TAB = (By.XPATH, '//a[@ui-sref="menuLayout.platform.statements"]')
    LIVE_ACCOUNTS = (By.XPATH, '//a[@ui-sref="menuLayout.connectTraders"]')
    ROLES = (By.ID, 'select_role')
    FOLLOWER_ROLE = '1'
    PROVIDER_ROLE = '2'
    CREATE_STRATEGY = (By.XPATH, '//a[@ui-sref="menuLayout.accountAddStrategy"]')

    def open_page(self, tab):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(tab)).click()

    def role_selection(self, role):
        Select(self.driver.find_element(*UserPage.ROLES)).select_by_value(role)
        time.sleep(5)
