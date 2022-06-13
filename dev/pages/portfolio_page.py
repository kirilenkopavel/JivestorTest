from selenium.common.exceptions import TimeoutException, InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dev.pages.data_test import DataTest
from dev.pages.page import BasePage
from dev.pages.user_page import UserPage


class PortfolioPage(BasePage):

    DELETE_ICON = (By.XPATH, '//a[@ng-click="deleteDialog(portfolio)"]')
    SELECT_ACCOUNT = (By.ID, 'ex_select_accounts')
    DELETE_PORTFOLIO = (By.XPATH, '//a[@ng-click="changeMode(portfolio, PortfolioCommands.delete_portfolio_request); '
                                  'closeThisDialog()"]')
    STRATEGY = (By.XPATH, '//a[@ui-sref="menuLayout.performance({id: portfolio.system_id})"]')

    def select_account(self, account):
        select = Select(self.driver.find_element(*PortfolioPage.SELECT_ACCOUNT)) \
            .select_by_value(account)

    def portfolio_review(self):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located(UserPage.PORTFOLIO_TAB)) \
            .click()
        PortfolioPage.select_account(self, DataTest.DEMO_ACCOUNT_SELECT)
        try:
            elements = wait.until(EC.presence_of_all_elements_located(PortfolioPage.DELETE_ICON))
            if len(elements) > 0:
                for element in elements:
                    element.click()
                    try:
                        element = self.driver.find_element(PortfolioPage.DELETE_PORTFOLIO) \
                            .click()
                    except InvalidArgumentException:
                        pass
        except TimeoutException:
            pass
