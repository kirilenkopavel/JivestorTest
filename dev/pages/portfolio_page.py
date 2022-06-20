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
    ADD_STRATEGIES = (By.XPATH, '//p[@class="wl-add-strategies-button"]/a')
    PAUSE = (By.XPATH, '//a[@ng-click="pauseDialog(portfolio)"]')
    SUSPEND = (By.XPATH, '//a[@ng-click="changeMode(ngDialogData.portfolio,PortfolioCommands.pause_portfolio_request);'
                         ' closeThisDialog()"]')
    PLAY = (By.XPATH, '//a[@ng-click="changeMode(portfolio, PortfolioCommands.start_portfolio_request)"]')
    STATUS_PLAY = (By.XPATH, '//span[@ng-if="portfolio.status == PortfolioStatus.running_portfolio"]')
    STATUS_PAUSE = (By.XPATH, '//span[@ng-if="portfolio.status == PortfolioStatus.paused_portfolio"]')
    STOP = (By.XPATH, '//a[@ng-click="stopDialog(portfolio)"]')
    STATUS_STOP = (By.XPATH, '//span[@ng-if="portfolio.status == PortfolioStatus.stopped_portfolio"]')
    SETTINGS = (By.XPATH, '//a[@ng-click="setSettingPortfolio(portfolio)"]')

    def open_settings(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(PortfolioPage.SETTINGS)).click()

    def select_account(self, account):
        Select(self.driver.find_element(*PortfolioPage.SELECT_ACCOUNT)).select_by_value(account)

    def delete_strategy(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(PortfolioPage.DELETE_ICON)).click()

    def portfolio_review(self):
        wait = WebDriverWait(self.driver, 5)
        UserPage(self.driver).open_page(UserPage.PORTFOLIO_TAB)
        PortfolioPage.select_account(self, DataTest.DEMO_ACCOUNT_SELECT)
        try:
            elements = wait.until(EC.presence_of_all_elements_located(PortfolioPage.DELETE_ICON))
            for element in elements:
                element.click()
                try:
                    wait.until(EC.presence_of_element_located(PortfolioPage.DELETE_PORTFOLIO)).click()
                except InvalidArgumentException:
                    pass
        except TimeoutException:
            pass

    def add_strategies(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(PortfolioPage.ADD_STRATEGIES)).click()

    def open_strategy(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(PortfolioPage.STRATEGY)).click()

    def pause_strategy(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(PortfolioPage.PAUSE)).click()
        wait.until(EC.presence_of_element_located(PortfolioPage.SUSPEND)).click()

    def play_strategy(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(PortfolioPage.PLAY)).click()

    def stop_strategy(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(PortfolioPage.STOP)).click()

    def review_status_strategy(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.visibility_of_element_located(PortfolioPage.STATUS_PLAY))
        except TimeoutException:
            PortfolioPage(self.driver).play_strategy()

