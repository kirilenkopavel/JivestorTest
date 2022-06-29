import random
import time
import unittest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from mgr.pages.page import BasePage
from mgr.pages.login_page import LoginPage
from mgr.pages.navigation_user import NavigationUser
from mgr.pages.registered_users_page import RegisteredUsers
from mgr.test.chromedriver import ChromeDriver
from selenium.webdriver.support import expected_conditions as EC


class TestRegisteredUsers(unittest.TestCase):

    roles = {RegisteredUsers.ADMINISTRATOR,
             RegisteredUsers.REGISTERED,
             RegisteredUsers.PUBLIC,
             RegisteredUsers.WL_MANAGER,
             RegisteredUsers.BUSINESS_DEVELOPER,
             RegisteredUsers.PRODUCT_MANAGER,
             RegisteredUsers.ACCOUNTANT
             }

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_filtration_role(self):
        LoginPage(self.driver).authorization()
        page = NavigationUser(self.driver)
        page.open_page(NavigationUser.REGISTERED_USERS_TAB)
        page.choice_wl(NavigationUser.DEV_PY)
        for role in TestRegisteredUsers.roles:
            table = page.collect_table(RegisteredUsers.FULL_NAME)
            name_role = RegisteredUsers(self.driver).selection_role(role)
            new_table = page.collect_table(RegisteredUsers.FULL_NAME)
            button = self.driver.find_element(*RegisteredUsers.FILTER_ROLES).text
            self.assertNotEqual(table, new_table)
            self.assertEqual(button, name_role)

    def test_search_name(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.REGISTERED_USERS_TAB)
        NavigationUser(self.driver).choice_wl(NavigationUser.DEV_PY)
        page = RegisteredUsers(self.driver)
        name = page.get_value(RegisteredUsers.FULL_NAME)
        page.search_filter(RegisteredUsers.SEARCH_NAME, name)
        result = page.get_value(RegisteredUsers.FULL_NAME)
        self.assertEqual(name, result)
        page.search_filter(RegisteredUsers.SEARCH_NAME, '')
        page.switch_page(RegisteredUsers.NUMBERS_PAGE)
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        new_name = page.get_value(RegisteredUsers.FULL_NAME)
        page.search_filter(RegisteredUsers.SEARCH_NAME, new_name)
        new_result = page.get_value(RegisteredUsers.FULL_NAME)
        self.assertEqual(new_name, new_result)

    def test_search_email(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.REGISTERED_USERS_TAB)
        NavigationUser(self.driver).choice_wl(NavigationUser.DEV_PY)
        page = RegisteredUsers(self.driver)
        email = page.get_value(RegisteredUsers.EMAIL)
        page.search_filter(RegisteredUsers.SEARCH_EMAIL, email)
        result = page.get_value(RegisteredUsers.EMAIL)
        self.assertEqual(email, result)
        page.search_filter(RegisteredUsers.SEARCH_EMAIL, '')
        page.switch_page(RegisteredUsers.NUMBERS_PAGE)
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        new_email = page.get_value(RegisteredUsers.EMAIL)
        page.search_filter(RegisteredUsers.SEARCH_EMAIL, new_email)
        new_result = page.get_value(RegisteredUsers.EMAIL)
        self.assertEqual(new_email, new_result)

    def test_open_blocked(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.REGISTERED_USERS_TAB)
        NavigationUser(self.driver).choice_wl(NavigationUser.DEV_PY)
        table = BasePage(self.driver).collect_table(RegisteredUsers.FULL_NAME)
        RegisteredUsers(self.driver).show_blocked()
        new_table = BasePage(self.driver).collect_table(RegisteredUsers.FULL_NAME)
        self.assertNotEqual(table, new_table)

    def test_search_name_in_blocked(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.REGISTERED_USERS_TAB)
        page = RegisteredUsers(self.driver)
        table = page.collect_table(RegisteredUsers.FULL_NAME)
        page.show_blocked()
        new_table = page.collect_table(RegisteredUsers.FULL_NAME)
        self.assertNotEqual(table, new_table)
        name = page.get_value(RegisteredUsers.FULL_NAME)
        page.search_filter(RegisteredUsers.SEARCH_NAME, name)
        result = page.get_value(RegisteredUsers.FULL_NAME)
        self.assertEqual(name, result)
        page.search_filter(RegisteredUsers.SEARCH_NAME, '')
        page.switch_page(RegisteredUsers.NUMBERS_PAGE)
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        new_name = page.get_value(RegisteredUsers.FULL_NAME)
        page.search_filter(RegisteredUsers.SEARCH_NAME, new_name)
        new_result = page.get_value(RegisteredUsers.FULL_NAME)
        self.assertEqual(new_name, new_result)

    def test_search_email_in_blocked(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.REGISTERED_USERS_TAB)
        page = RegisteredUsers(self.driver)
        table = page.collect_table(RegisteredUsers.FULL_NAME)
        page.show_blocked()
        new_table = page.collect_table(RegisteredUsers.FULL_NAME)
        self.assertNotEqual(table, new_table)
        email = page.get_value(RegisteredUsers.EMAIL)
        page.search_filter(RegisteredUsers.SEARCH_EMAIL, email)
        result = page.get_value(RegisteredUsers.EMAIL)
        self.assertEqual(email, result)
        page.search_filter(RegisteredUsers.SEARCH_EMAIL, '')
        page.switch_page(RegisteredUsers.NUMBERS_PAGE)
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
        new_email = page.get_value(RegisteredUsers.EMAIL)
        page.search_filter(RegisteredUsers.SEARCH_EMAIL, new_email)
        new_result = page.get_value(RegisteredUsers.EMAIL)
        self.assertEqual(new_email, new_result)

    def test_search_and_filter_by_role(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.REGISTERED_USERS_TAB)
        for role in TestRegisteredUsers.roles:
            page = RegisteredUsers(self.driver)
            page.selection_role(role)
            name = page.get_value(RegisteredUsers.FULL_NAME)
            page.search_filter(RegisteredUsers.SEARCH_NAME, name)
            result = page.get_value(RegisteredUsers.FULL_NAME)
            self.assertEqual(name, result)
            page.search_filter(RegisteredUsers.SEARCH_NAME, '')
            page.switch_page(RegisteredUsers.NUMBERS_PAGE)
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
            new_name = page.get_value(RegisteredUsers.FULL_NAME)
            page.search_filter(RegisteredUsers.SEARCH_NAME, new_name)
            new_result = page.get_value(RegisteredUsers.FULL_NAME)
            self.assertEqual(new_name, new_result)

    def test_open_edit_user(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.REGISTERED_USERS_TAB)
        RegisteredUsers(self.driver).open_edit_user()
        wait = WebDriverWait(self.driver, 10)
        self.assertTrue(wait.until(EC.visibility_of_element_located(RegisteredUsers.BLOCKED_BUTTON)))

    def test_edit_input_user(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.REGISTERED_USERS_TAB)
        page = RegisteredUsers(self.driver)
        page.search_filter(RegisteredUsers.SEARCH_EMAIL, 'test.follover@gmail.ru')
        page.open_edit_user()
        full_name = page.edit_user_input()
        page.update_settings()
        page.search_filter(RegisteredUsers.SEARCH_NAME, full_name)
        result = page.get_value(RegisteredUsers.EMAIL)
        self.assertEqual(result, 'test.follover@gmail.ru')

    def test_sorting_date(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.REGISTERED_USERS_TAB)
        page = RegisteredUsers(self.driver)
        table = page.collect_table(RegisteredUsers.EMAIL)
        page.sort_by(RegisteredUsers.SORTING_DATE)
        new_table = page.collect_table(RegisteredUsers.EMAIL)
        self.assertNotEqual(table, new_table)
        page.sort_by(RegisteredUsers.SORTING_DATE)
        new_table = page.collect_table(RegisteredUsers.EMAIL)
        self.assertEqual(table, new_table)

    def test_sorting_last_access(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.REGISTERED_USERS_TAB)
        page = RegisteredUsers(self.driver)
        table = page.collect_table(RegisteredUsers.EMAIL)
        page.sort_by(RegisteredUsers.SORTING_LAST_ACCESS)
        new_table = page.collect_table(RegisteredUsers.EMAIL)
        self.assertNotEqual(table, new_table)


if __name__ == '__main__':
    unittest.main()
