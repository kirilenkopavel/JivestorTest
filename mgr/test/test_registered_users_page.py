import time
import unittest

from selenium.common.exceptions import TimeoutException
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
        page = BasePage(self.driver)
        for role in TestRegisteredUsers.roles:
            table = page.collect_table(RegisteredUsers.FULL_NAME)
            name_role = RegisteredUsers(self.driver).selection_role(role)
            new_table = page.collect_table(RegisteredUsers.FULL_NAME)
            button = self.driver.find_element(*RegisteredUsers.FILTER_ROLES).text
            self.assertNotEqual(table, new_table)
            self.assertEqual(button, name_role)


if __name__ == '__main__':
    unittest.main()
