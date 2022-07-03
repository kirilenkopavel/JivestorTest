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


if __name__ == '__main__':
    unittest.main()
