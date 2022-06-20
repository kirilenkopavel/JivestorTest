from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dev.pages.page import BasePage


class UserPage(BasePage):

    PORTFOLIO_TAB = '//a[@ui-sref="menuLayout.platform.portfolio"]'
    STRATEGIES_TAB = '//a[@ui-sref="menuLayout.tradeRatingMain"]'
    TRADING_TERMINAL_TAB = '//a[@ui-sref="menuLayout.platform.terminal"]'
    STATEMENTS_TAB = '//a[@ui-sref="menuLayout.platform.statements"]'
    LIVE_ACCOUNTS = '//a[@ui-sref="menuLayout.connectTraders"]'

    def open_page(self, tab):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, tab))).click()
