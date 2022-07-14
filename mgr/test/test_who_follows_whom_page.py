import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from mgr.pages.login_page import LoginPage
from mgr.pages.navigation_user import NavigationUser
from mgr.pages.who_follows_whom_page import WhoFollowsWhom
from mgr.test.chromedriver import ChromeDriver


class TimeiutExeption:
    pass


class TestWhoFollowsWhom(unittest.TestCase):

    tabs = {WhoFollowsWhom.LIVE_ACCOUNTS_TAB,
            WhoFollowsWhom.DEMO_ACCOUNTS_TAB
            }

    statuses = {WhoFollowsWhom.ACTIV_STATUS,
                WhoFollowsWhom.INACTIV_STATUS
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
        NavigationUser(self.driver).open_page(NavigationUser.WHO_FOLLOWS_WHOM_TAB)
        NavigationUser(self.driver).choice_wl(NavigationUser.DEV_PY)
        page = WhoFollowsWhom(self.driver)
        for tab in TestWhoFollowsWhom.tabs:
            for status in TestWhoFollowsWhom.statuses:
                page.switch(tab)
                page.switch(status)
                account = page.get_value(WhoFollowsWhom.ACCOUNT)
                page.search_filter(WhoFollowsWhom.ACCOUNT_FILTER, account)
                result = page.get_value(WhoFollowsWhom.ACCOUNT)
                self.assertNotEqual(account, result)
                try:
                    page.switch_page(WhoFollowsWhom.NUMBERS_PAGE)
                    self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
                    account = page.get_value(WhoFollowsWhom.ACCOUNT)
                    page.search_filter(WhoFollowsWhom.ACCOUNT_FILTER, account)
                    result = page.get_value(WhoFollowsWhom.ACCOUNT)
                    self.assertEqual(account, result)
                except TimeiutExeption:
                    pass

    def test_search_display_name(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHO_FOLLOWS_WHOM_TAB)
        NavigationUser(self.driver).choice_wl(NavigationUser.DEV_PY)
        page = WhoFollowsWhom(self.driver)
        for tab in TestWhoFollowsWhom.tabs:
            for status in TestWhoFollowsWhom.statuses:
                page.switch(tab)
                page.switch(status)
                name = page.get_value(WhoFollowsWhom.DISPLAY_NAME)
                page.search_filter(WhoFollowsWhom.DISPLAY_NAME_FILTER, name)
                result = page.get_value(WhoFollowsWhom.DISPLAY_NAME)
                self.assertNotEqual(name, result)
                try:
                    page.switch_page(WhoFollowsWhom.NUMBERS_PAGE)
                    self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
                    name = page.get_value(WhoFollowsWhom.DISPLAY_NAME)
                    page.search_filter(WhoFollowsWhom.DISPLAY_NAME_FILTER, name)
                    result = page.get_value(WhoFollowsWhom.DISPLAY_NAME)
                    self.assertEqual(name, result)
                except TimeiutExeption:
                    pass

    def test_search_trading_strategy(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHO_FOLLOWS_WHOM_TAB)
        NavigationUser(self.driver).choice_wl(NavigationUser.DEV_PY)
        page = WhoFollowsWhom(self.driver)
        for tab in TestWhoFollowsWhom.tabs:
            for status in TestWhoFollowsWhom.statuses:
                page.switch(tab)
                page.switch(status)
                name = page.get_value(WhoFollowsWhom.TRADING_STRATEGY)
                page.search_filter(WhoFollowsWhom.TRADING_STRATEGY_FILTER, name)
                result = page.get_value(WhoFollowsWhom.TRADING_STRATEGY)
                self.assertNotEqual(name, result)
                try:
                    page.switch_page(WhoFollowsWhom.NUMBERS_PAGE)
                    self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
                    name = page.get_value(WhoFollowsWhom.TRADING_STRATEGY)
                    page.search_filter(WhoFollowsWhom.TRADING_STRATEGY_FILTER, name)
                    result = page.get_value(WhoFollowsWhom.TRADING_STRATEGY)
                    self.assertEqual(name, result)
                except TimeiutExeption:
                    pass

    def test_sorting_date(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHO_FOLLOWS_WHOM_TAB)
        NavigationUser(self.driver).choice_wl(NavigationUser.DEV_PY)
        page = WhoFollowsWhom(self.driver)
        for tab in TestWhoFollowsWhom.tabs:
            for status in TestWhoFollowsWhom.statuses:
                page.switch(tab)
                page.switch(status)
                table = page.collect_table(WhoFollowsWhom.DISPLAY_NAME)
                page.sort_by(WhoFollowsWhom.SORTING_DATE)
                new_table = page.collect_table(WhoFollowsWhom.DISPLAY_NAME)
                self.assertNotEqual(table, new_table)

    def test_sorting_display_name(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHO_FOLLOWS_WHOM_TAB)
        NavigationUser(self.driver).choice_wl(NavigationUser.DEV_PY)
        page = WhoFollowsWhom(self.driver)
        for tab in TestWhoFollowsWhom.tabs:
            for status in TestWhoFollowsWhom.statuses:
                page.switch(tab)
                page.switch(status)
                table = page.collect_table(WhoFollowsWhom.DISPLAY_NAME)
                page.sort_by(WhoFollowsWhom.SORTING_DISPLAY_NAME)
                new_table = page.collect_table(WhoFollowsWhom.DISPLAY_NAME)
                self.assertNotEqual(table, new_table)


if __name__ == '__main__':
    unittest.main()
