import unittest

from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from mgr.pages.login_page import LoginPage
from mgr.pages.navigation_user import NavigationUser
from mgr.pages.white_list_page import WhiteList
from mgr.pages.wl_stats_page import WlStats
from mgr.test.chromedriver import ChromeDriver


class TestWhiteList(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_add_to_white_list(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LIST_TAB)
        page = WlStats(self.driver)
        account = page.add_note()
        new_account = page.get_value(WhiteList.ACCOUNT)
        self.assertEqual(account, new_account)

    def test_soring_date(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LIST_TAB)
        page = WlStats(self.driver)
        table = page.collect_table(WhiteList.DATE)
        page.sort_by(WhiteList.SORTING_DATE)
        new_table = page.collect_table(WhiteList.DATE)
        self.assertNotEqual(table, new_table)

    def test_delete_account(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LIST_TAB)
        page = WlStats(self.driver)
        account = page.get_value(WhiteList.ACCOUNT)
        page.delete_note()
        new_account = page.get_value(WhiteList.ACCOUNT)
        self.assertNotEqual(account, new_account)

    def test_filtration_date(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LIST_TAB)
        page = WlStats(self.driver)
        table = page.collect_table(WlStats.TOTAL_USD)
        page.filtration_date()
        new_table = page.collect_table(WlStats.TOTAL_USD)
        self.assertNotEqual(table, new_table)


if __name__ == '__main__':
    unittest.main()
