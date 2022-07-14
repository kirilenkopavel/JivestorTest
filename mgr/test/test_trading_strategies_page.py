import time
import unittest

from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.login_page import LoginPage
from mgr.pages.navigation_user import NavigationUser
from mgr.pages.trading_strategies_page import TradingStrategies
from mgr.test.chromedriver import ChromeDriver
from mgr.test.test_who_follows_whom_page import TimeiutExeption


class TestTradingStrategies(unittest.TestCase):

    statuses = {TradingStrategies.ACTIV_STATUS,
                TradingStrategies.INVISIBLE_STATUS,
                TradingStrategies.DISQUALIFIED_STATUS,
                TradingStrategies.PRO_STATUS,
                TradingStrategies.HIGH_RISK_STATUS,
                TradingStrategies.DEMO_STATUS,
                TradingStrategies.DISABLED_STATUS
                }

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_search_account(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.TRADING_STRATEGIES_TAB)
        page = TradingStrategies(self.driver)
        account = page.get_value(TradingStrategies.ACCOUNT)
        page.search_filter(TradingStrategies.ACCOUNT_FILTER, account)
        result = page.get_value(TradingStrategies.ACCOUNT)
        self.assertNotEqual(account, result)
        try:
            page.switch_page(TradingStrategies.NUMBERS_PAGE)
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
            account = page.get_value(TradingStrategies.ACCOUNT)
            page.search_filter(TradingStrategies.ACCOUNT_FILTER, account)
            result = page.get_value(TradingStrategies.ACCOUNT)
            self.assertEqual(account, result)
        except TimeiutExeption:
            pass

    def test_search_trader(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.TRADING_STRATEGIES_TAB)
        page = TradingStrategies(self.driver)
        trader = page.get_value(TradingStrategies.TRADER)
        page.search_filter(TradingStrategies.TRADER_FILTER, trader)
        result = page.get_value(TradingStrategies.TRADER)
        self.assertNotEqual(trader, result)
        try:
            page.switch_page(TradingStrategies.NUMBERS_PAGE)
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
            trader = page.get_value(TradingStrategies.TRADER)
            page.search_filter(TradingStrategies.TRADER_FILTER, trader)
            result = page.get_value(TradingStrategies.TRADER)
            self.assertEqual(trader, result)
        except TimeiutExeption:
            pass

    def test_search_strategy(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.TRADING_STRATEGIES_TAB)
        page = TradingStrategies(self.driver)
        strategy = page.get_value(TradingStrategies.STRATEGY_NAME)
        page.search_filter(TradingStrategies.STRATEGY_NAME_FILTER, strategy)
        result = page.get_value(TradingStrategies.STRATEGY_NAME)
        self.assertNotEqual(strategy, result)
        try:
            page.switch_page(TradingStrategies.NUMBERS_PAGE)
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
            strategy = page.get_value(TradingStrategies.STRATEGY_NAME)
            page.search_filter(TradingStrategies.STRATEGY_NAME_FILTER, strategy)
            result = page.get_value(TradingStrategies.STRATEGY_NAME)
            self.assertEqual(strategy, result)
        except TimeiutExeption:
            pass

    def test_filtration_role(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.TRADING_STRATEGIES_TAB)
        page = TradingStrategies(self.driver)
        for status in TestTradingStrategies.statuses:
            table = page.collect_table(TradingStrategies.STRATEGY_NAME)
            name_status = page.selection_status(status)
            new_table = page.collect_table(TradingStrategies.STRATEGY_NAME)
            button = self.driver.find_element(*TradingStrategies.STATUSES).text
            self.assertNotEqual(table, new_table)
            self.assertEqual(button, name_status)

    def test_sorting_creation_date(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.TRADING_STRATEGIES_TAB)
        page = TradingStrategies(self.driver)
        table = page.collect_table(TradingStrategies.DATE)
        page.sort_by(TradingStrategies.SORTING_DATE)
        new_table = page.collect_table(TradingStrategies.DATE)
        self.assertNotEqual(table, new_table)

    def test_sorting_strategy_name(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.TRADING_STRATEGIES_TAB)
        page = TradingStrategies(self.driver)
        table = page.collect_table(TradingStrategies.STRATEGY_NAME)
        page.sort_by(TradingStrategies.SORTING_STRATEGY_NAME)
        new_table = page.collect_table(TradingStrategies.STRATEGY_NAME)
        self.assertNotEqual(table, new_table)

    def test_sorting_account(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.TRADING_STRATEGIES_TAB)
        page = TradingStrategies(self.driver)
        table = page.collect_table(TradingStrategies.ACCOUNT)
        page.sort_by(TradingStrategies.SORTING_ACCOUNT)
        new_table = page.collect_table(TradingStrategies.ACCOUNT)
        self.assertNotEqual(table, new_table)

    def test_review_live_followers(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.TRADING_STRATEGIES_TAB)
        page = TradingStrategies(self.driver)
        size_followers = page.review_followers(TradingStrategies.LIVE_FOLLOWERS)
        time.sleep(5)
        counter_followers = wait.until(EC.presence_of_element_located(TradingStrategies.COUNTER_TOTAL)).text.find(" ")
        self.assertEqual(size_followers, counter_followers)
        followers = str(len(wait.until(EC.presence_of_all_elements_located(TradingStrategies.DATE_FOLLOWERS))))
        self.assertEqual(size_followers, followers)

    def test_review_demo_followers(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.TRADING_STRATEGIES_TAB)
        page = TradingStrategies(self.driver)
        size_followers = page.review_followers(TradingStrategies.DEMO_FOLLOWERS)
        time.sleep(5)
        counter_followers = wait.until(EC.presence_of_element_located(TradingStrategies.COUNTER_TOTAL)).text.find(" ")
        self.assertEqual(size_followers, counter_followers)
        followers = str(len(wait.until(EC.presence_of_all_elements_located(TradingStrategies.DATE_FOLLOWERS))))
        self.assertEqual(size_followers, followers)

    def test_sorting_followers(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.TRADING_STRATEGIES_TAB)
        page = TradingStrategies(self.driver)
        page.review_followers(TradingStrategies.LIVE_FOLLOWERS)
        time.sleep(5)
        table = page.collect_table(TradingStrategies.DATE_FOLLOWERS)
        page.sort_by(TradingStrategies.SORTING_DATE_FOLLOWERS)
        new_table = page.collect_table(TradingStrategies.DATE_FOLLOWERS)
        self.assertNotEqual(table, new_table)

    def test_change_visibility(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.TRADING_STRATEGIES_TAB)
        page = TradingStrategies(self.driver)
        page.search_filter(TradingStrategies.STRATEGY_NAME_FILTER, "Autotest")
        status = page.change_visibility()
        wait.until(EC.presence_of_element_located(TradingStrategies.SETTINGS_BUTTON)).click()
        new_status = wait.until(EC.presence_of_element_located(TradingStrategies.MAKE_STATUS)).text
        if status == 'Make Visible':
            self.assertEqual(new_status, 'Make Invisible')
        else:
            self.assertEqual(new_status, 'Make Visible')


if __name__ == '__main__':
    unittest.main()
