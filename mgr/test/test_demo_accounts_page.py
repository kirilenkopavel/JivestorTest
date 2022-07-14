import unittest

from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from mgr.pages.demo_accounts_page import DemoAccounts
from mgr.pages.login_page import LoginPage
from mgr.pages.navigation_user import NavigationUser
from mgr.test.chromedriver import ChromeDriver


class TestDemoAccounts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_search_email(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.DEMO_ACCOUNTS_TAB)
        page = DemoAccounts(self.driver)
        email = page.get_value(DemoAccounts.EMAIL)
        page.search_filter(DemoAccounts.EMAIL_FILTER, email)
        result = page.get_value(DemoAccounts.EMAIL)
        self.assertEqual(email, result)
        page.search_filter(DemoAccounts.EMAIL_FILTER, '')
        page.switch_page(DemoAccounts.NUMBERS_PAGE)
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        new_email = page.get_value(DemoAccounts.EMAIL)
        page.search_filter(DemoAccounts.EMAIL_FILTER, new_email)
        new_result = page.get_value(DemoAccounts.EMAIL)
        self.assertEqual(new_email, new_result)

    def test_search_account(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.DEMO_ACCOUNTS_TAB)
        page = DemoAccounts(self.driver)
        account = page.get_value(DemoAccounts.ACCOUNT)
        page.search_filter(DemoAccounts.ACCOUNT_FILTER, account)
        result = page.get_value(DemoAccounts.ACCOUNT)
        self.assertEqual(account, result)
        page.search_filter(DemoAccounts.ACCOUNT_FILTER, '')
        page.switch_page(DemoAccounts.NUMBERS_PAGE)
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        new_account = page.get_value(DemoAccounts.ACCOUNT)
        page.search_filter(DemoAccounts.ACCOUNT_FILTER, new_account)
        new_result = page.get_value(DemoAccounts.ACCOUNT)
        self.assertEqual(new_account, new_result)

    def test_search_full_name(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.DEMO_ACCOUNTS_TAB)
        page = DemoAccounts(self.driver)
        name = page.get_value(DemoAccounts.FULL_NAME)
        page.search_filter(DemoAccounts.FULL_NAME_FILTER, name)
        result = page.get_value(DemoAccounts.FULL_NAME)
        self.assertEqual(name, result)
        page.search_filter(DemoAccounts.FULL_NAME_FILTER, '')
        page.switch_page(DemoAccounts.NUMBERS_PAGE)
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        new_name = page.get_value(DemoAccounts.FULL_NAME)
        page.search_filter(DemoAccounts.FULL_NAME_FILTER, new_name)
        new_result = page.get_value(DemoAccounts.FULL_NAME)
        self.assertEqual(new_name, new_result)

    def test_search_display_name(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.DEMO_ACCOUNTS_TAB)
        page = DemoAccounts(self.driver)
        name = page.get_value(DemoAccounts.DISPLAY_NAME)
        page.search_filter(DemoAccounts.DISPLAY_NAME_FILTER, name)
        result = page.get_value(DemoAccounts.DISPLAY_NAME)
        self.assertEqual(name, result)
        page.search_filter(DemoAccounts.DISPLAY_NAME_FILTER, '')
        page.switch_page(DemoAccounts.NUMBERS_PAGE)
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        new_name = page.get_value(DemoAccounts.DISPLAY_NAME)
        page.search_filter(DemoAccounts.DISPLAY_NAME_FILTER, new_name)
        new_result = page.get_value(DemoAccounts.DISPLAY_NAME)
        self.assertEqual(new_name, new_result)

    def test_sorting_date(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.DEMO_ACCOUNTS_TAB)
        page = DemoAccounts(self.driver)
        table = page.collect_table(DemoAccounts.EMAIL)
        page.sort_by(DemoAccounts.SORTING_DATE)
        new_table = page.collect_table(DemoAccounts.EMAIL)
        self.assertNotEqual(table, new_table)
        page.sort_by(DemoAccounts.SORTING_DATE)
        new_table = page.collect_table(DemoAccounts.EMAIL)
        self.assertEqual(table, new_table)

    def test_sorting_full_name(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.DEMO_ACCOUNTS_TAB)
        page = DemoAccounts(self.driver)
        page.sort_by(DemoAccounts.SORTING_FULL_NAME)
        table = page.collect_table(DemoAccounts.EMAIL)
        page.sort_by(DemoAccounts.SORTING_FULL_NAME)
        result = page.collect_table(DemoAccounts.EMAIL)
        self.assertNotEqual(table, result)
        page.sort_by(DemoAccounts.SORTING_FULL_NAME)
        new_result = page.collect_table(DemoAccounts.EMAIL)
        self.assertEqual(table, new_result)

    def test_sorting_display_name(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.DEMO_ACCOUNTS_TAB)
        NavigationUser(self.driver).choice_wl(NavigationUser.DEV_PY)
        page = DemoAccounts(self.driver)
        page.sort_by(DemoAccounts.SORTING_DISPLAY_NAME)
        table = page.collect_table(DemoAccounts.EMAIL)
        page.sort_by(DemoAccounts.SORTING_DISPLAY_NAME)
        result = page.collect_table(DemoAccounts.EMAIL)
        self.assertNotEqual(table, result)
        page.sort_by(DemoAccounts.SORTING_DISPLAY_NAME)
        new_result = page.collect_table(DemoAccounts.EMAIL)
        self.assertEqual(table, new_result)

    def test_sorting_email(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.DEMO_ACCOUNTS_TAB)
        NavigationUser(self.driver).choice_wl(NavigationUser.DEV_PY)
        page = DemoAccounts(self.driver)
        page.sort_by(DemoAccounts.SORTING_EMAIL)
        table = page.collect_table(DemoAccounts.EMAIL)
        page.sort_by(DemoAccounts.SORTING_EMAIL)
        result = page.collect_table(DemoAccounts.EMAIL)
        self.assertNotEqual(table, result)
        page.sort_by(DemoAccounts.SORTING_EMAIL)
        new_result = page.collect_table(DemoAccounts.EMAIL)
        self.assertEqual(table, new_result)

    def test_sorting_account(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.DEMO_ACCOUNTS_TAB)
        NavigationUser(self.driver).choice_wl(NavigationUser.DEV_PY)
        page = DemoAccounts(self.driver)
        page.sort_by(DemoAccounts.SORTING_ACCOUNT)
        table = page.collect_table(DemoAccounts.ACCOUNT)
        page.sort_by(DemoAccounts.SORTING_ACCOUNT)
        result = page.collect_table(DemoAccounts.ACCOUNT)
        self.assertNotEqual(table, result)
        page.sort_by(DemoAccounts.SORTING_ACCOUNT)
        new_result = page.collect_table(DemoAccounts.ACCOUNT)
        self.assertEqual(table, new_result)

    def test_expiration_account(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.DEMO_ACCOUNTS_TAB)
        NavigationUser(self.driver).choice_wl(NavigationUser.DEV_PY)
        page = DemoAccounts(self.driver)
        result = page.extend_account()
        self.assertTrue(result == '30')


if __name__ == '__main__':
    unittest.main()
