import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dev.pages.page import BasePage


class StatementsPage(BasePage):

    STRATEGY = (By.XPATH, '//label[@for="provider19613"]')
    CUSTOM_TRADES = (By.XPATH, '//label[@for="provider0"]')
    TRADING_HISTORY = (By.XPATH, '//a[@ng-click="changeChartsOrdersTab(2)"]')
    ORDERS = (By.XPATH, '//tr[@ng-repeat="order in orders"]')
    STRATEGIES = (By.XPATH, '//tr[@ng-repeat="system in systemsList"]')
    GENERATE = (By.XPATH, '//a[@ng-click="generateStatements()"]')

    def generate_statements(self, strategy):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(strategy)).click()
        self.driver.find_element(*StatementsPage.GENERATE).click()

    def open_trading_history(self):
        self.driver.find_element(*StatementsPage.TRADING_HISTORY).click()
        wait = WebDriverWait(self.driver, 10)
        try:
            orders = wait.until(EC.visibility_of_all_elements_located(StatementsPage.ORDERS))
            return len(orders)
        except TimeoutException:
            return 0
