import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dev.pages.page import BasePage
from dev.pages.portfolio_page import PortfolioPage
from dev.pages.strategies_page import StrategiesPage
from dev.pages.user_page import UserPage


class StrategyPage(BasePage):
    ADD_TO_NOT = (By.XPATH, '//a[@ng-click="addPortfolioNotAutorized()"]')
    ADD_TO = (By.XPATH, '//a[@class="btn-green float-left performance-add-to-portfolio tour-step-3"]')
    LOGIN_BUTTON = (By.XPATH, '//a[@ng-click="close(\'withoutMenuLayout.auth.login\')"]')
    REGISTER_BUTTON = (By.XPATH, '//a[@ng-click="close(\'withoutMenuLayout.auth.registration\')"]')
    TRADING_ACCOUNTS_SELECT = (By.ID, 'ex_select_accounts')
    TRADING_ACCOUNTS = (By.XPATH, '//div[@class="portfolio-form-top additional-info"]//span[2]')
    SIDEBAR = (By.XPATH, '//div[@class="sidebar-portfolio-block ng-scope"]')
    CHECK_COPY = (By.XPATH, '//label[@for="portfolio_copy_orders_auto"]')
    COPY_OPTIONS = (By.ID, 'copy_open_trades_type')
    SUBMIT = (By.XPATH, '//input[@ng-disabled="portfolioCheckboxes.agree !== true"]')
    COPY_RECOMMENDED = '0'
    COPY_AS_IS = '1'
    TEXT_DESCRIPTION = (By.XPATH, '//div[@class="form-desc ng-isolate-scope"]//span[1]')
    AUTO_TYPE = '//label[@for="portfolio_type_1"]'
    PERCENT_OF_BALANCE_TYPE = '//label[@for="portfolio_type_2"]'
    FIX_SIZE_TYPE = '//label[@for="portfolio_type_3"]'
    PROPORTIONAL_LOT_TYPE = '//label[@for="portfolio_type_4"]'
    IN_PORTFOLIO = (By.XPATH, '//a[@ng-click="go(\'menuLayout.platform.portfolio\')"]')
    INPUT_LOT = (By.XPATH, '//input[@name="lot"]')
    INPUT_LOT_MIN = (By.XPATH, '//input[@name="lot_min"]')
    INPUT_LOT_MAX = (By.XPATH, '//input[@name="lot_max"]')
    INPUT_FIXED_STOP = (By.XPATH, '//input[@name="fixed_sl"]')
    INPUT_FIXED_TAKE = (By.XPATH, '//input[@name="fixed_tp"]')
    INPUT_STOP_OUT = (By.ID, 'portfolio_stop_out')
    INPUT_WORST_DEV = (By.ID, 'portfolio_worst_dev')
    LIMIT_TRADE_CHECK = (By.XPATH, '//label[@for="portfolio_limit_num"]')
    INPUT_LIMIT_TRADE = (By.ID, 'portfolio_by_num')
    INPUT_EQUITY = (By.ID, 'portfolio_by_equity')
    CHECK_FLIPPED_TRADING = (By.XPATH, '//label[@for="portfolio_invest"]')
    ICON_FAVORITES = (By.XPATH, '//span[@ng-click="toggleFavorites()"]')
    SHARE_BUTTON = (By.XPATH, '//span[@class="call-popup-inner"]')
    WEB_ADDRESS_INPUT = (By.XPATH, '//input[@class="web-address"]')
    PROVIDER_NAME = (By.XPATH, '//a[@class="performance-user-name ng-binding"]')
    ALL_PERIOD = '//a[@ng-click="setActiveTab(1)"]'
    WEEK_PERIOD = '//a[@ng-click="setActiveTab(2)"]'
    ONE_MONTH_PERIOD = '//a[@ng-click="setActiveTab(3)"]'
    THREE_MONTH_PERIOD = '//a[@ng-click="setActiveTab(4)"]'
    SIX_MONTH_PERIOD = '//a[@ng-click="setActiveTab(5)"]'
    ONE_YEAR_PERIOD = '//a[@ng-click="setActiveTab(6)"]'
    FROM_DATE = (By.ID, 'fromDateFilter')
    RELOAD_BUTTON = (By.XPATH, '//span[@class="icon-reload-white"]')
    MONTHLY_VALUES = (By.XPATH, '//span[@data-ng-if="monthValue != null"]')
    FOLLOWERS_BUTTON = (By.XPATH, '//a[@class="btn-gray open-followers-sidebar"]')
    FOLLOWERS = (By.XPATH, '//span[@class="follower-name ng-binding"]')

    def view_followers(self):
        element = self.driver.find_element(*StrategyPage.FOLLOWERS_BUTTON) \
            .click()

    def selection_period(self, period):
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.presence_of_element_located((By.XPATH, period))) \
            .click()
        element = wait.until(EC.presence_of_element_located(StrategyPage.RELOAD_BUTTON)) \
            .click()
        time.sleep(2)

    def open_provider_page(self):
        element = self.driver.find_element(*StrategyPage.PROVIDER_NAME) \
            .click()

    def share_strategy(self):
        element = self.driver.find_element(*StrategyPage.SHARE_BUTTON) \
            .click()

    def add_strategy(self):
        element = self.driver.find_element(*StrategyPage.ADD_TO_NOT) \
            .click()

    def add_strategy_user(self):
        element = self.driver.find_element(*StrategyPage.ADD_TO) \
            .click()

    def in_login(self):
        element = self.driver.find_element(*StrategyPage.LOGIN_BUTTON) \
            .click()

    def in_register(self):
        element = self.driver.find_element(*StrategyPage.REGISTER_BUTTON) \
            .click()

    def select_account(self, account):
        select = Select(self.driver.find_element(*StrategyPage.TRADING_ACCOUNTS_SELECT)) \
            .select_by_value(account)

    def toggle_settings(self, type_settings):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, type_settings))) \
            .click()
        time.sleep(3)

    def check_copy(self, value):
        element = self.driver.find_element(*StrategyPage.CHECK_COPY) \
            .click()
        time.sleep(3)
        """time.sleep(5)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(StrategyPage.COPY_OPTIONS)) \
            .click()
        element = self.driver.find_element(By.XPATH, value) \
            .click()"""
        select = Select(self.driver.find_element(*StrategyPage.COPY_OPTIONS)) \
            .select_by_value(value)

    def save(self):
        element = self.driver.find_element(*StrategyPage.SUBMIT) \
            .click()

    def in_portfolio(self):
        element = self.driver.find_element(*StrategyPage.IN_PORTFOLIO) \
            .click()

    def input_lot(self, value):
        element = self.driver.find_element(*StrategyPage.INPUT_LOT) \
            .send_keys(value)

    def input_lot_min(self, value):
        element = self.driver.find_element(*StrategyPage.INPUT_LOT_MIN) \
            .send_keys(value)

    def input_lot_max(self, value):
        element = self.driver.find_element(*StrategyPage.INPUT_LOT_MAX) \
            .send_keys(value)

    def input_fixed_stop(self, value):
        element = self.driver.find_element(*StrategyPage.INPUT_FIXED_STOP) \
            .send_keys(value)

    def input_fixed_take(self, value):
        element = self.driver.find_element(*StrategyPage.INPUT_FIXED_TAKE) \
            .send_keys(value)

    def input_stop_out(self, value):
        element = self.driver.find_element(*StrategyPage.INPUT_STOP_OUT) \
            .send_keys(value)

    def input_worst_dev(self, value):
        element = self.driver.find_element(*StrategyPage.INPUT_WORST_DEV) \
            .send_keys(value)

    def check_limit_trade(self, value1, value2):
        element = self.driver.find_element(*StrategyPage.LIMIT_TRADE_CHECK) \
            .click()
        element = self.driver.find_element(*StrategyPage.INPUT_LIMIT_TRADE) \
            .send_keys(value1)
        element = self.driver.find_element(*StrategyPage.INPUT_EQUITY) \
            .send_keys(value2)

    def check_flipped_trading(self):
        element = self.driver.find_element(*StrategyPage.CHECK_FLIPPED_TRADING) \
            .click()

    def in_favorites(self):
        element = self.driver.find_element(*StrategyPage.ICON_FAVORITES) \
            .click()

    def open_strategy(self):
        element = self.driver.find_element(*StrategiesPage.STRATEGY_NAME) \
            .click()

