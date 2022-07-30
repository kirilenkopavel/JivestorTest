import unittest

from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from mgr.pages.login_page import LoginPage
from mgr.pages.navigation_user import NavigationUser
from mgr.pages.user_balances_page import UserBalances
from mgr.test.chromedriver import ChromeDriver


class TestUserBalances(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_search_email(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.USER_BALANCES_TAB)
        page = UserBalances(self.driver)
        email = page.get_value(UserBalances.EMAIL)
        page.search_filter(UserBalances.EMAIL_FILTER, email)
        result = page.get_value(UserBalances.EMAIL)
        self.assertEqual(email, result)
        page.search_filter(UserBalances.EMAIL_FILTER, '')
        page.switch_page(UserBalances.NUMBERS_PAGE)
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        new_email = page.get_value(UserBalances.EMAIL)
        page.search_filter(UserBalances.EMAIL_FILTER, new_email)
        new_result = page.get_value(UserBalances.EMAIL)
        self.assertEqual(new_email, new_result)

    def test_search_display_name(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.USER_BALANCES_TAB)
        page = UserBalances(self.driver)
        name = page.get_value(UserBalances.NAME)
        page.search_filter(UserBalances.NAME_FILTER, name)
        result = page.get_value(UserBalances.NAME)
        self.assertEqual(name, result)
        page.search_filter(UserBalances.NAME_FILTER, '')
        page.switch_page(UserBalances.NUMBERS_PAGE)
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        new_name = page.get_value(UserBalances.NAME)
        page.search_filter(UserBalances.NAME_FILTER, new_name)
        new_result = page.get_value(UserBalances.EMAIL)
        self.assertEqual(new_name, new_result)

    def test_sorting_display_name(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.USER_BALANCES_TAB)
        page = UserBalances(self.driver)
        table = page.collect_table(UserBalances.NAME)
        page.sort_by(UserBalances.SORTING_DISPLAY_NAME)
        new_table = page.collect_table(UserBalances.NAME)
        self.assertNotEqual(table, new_table)

    def test_sorting_balances(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.USER_BALANCES_TAB)
        page = UserBalances(self.driver)
        table = page.collect_table(UserBalances.BALANCE)
        page.sort_by(UserBalances.SORTING_BALANCE)
        new_table = page.collect_table(UserBalances.BALANCE)
        self.assertNotEqual(table, new_table)


if __name__ == '__main__':
    unittest.main()
