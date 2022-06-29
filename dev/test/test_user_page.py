import time
import unittest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from dev.pages.login_page import LoginPage
from dev.pages.user_page import UserPage
from dev.test.chromedriver import ChromeDriver


class TestUserPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_role_selection_provider(self):
        LoginPage(self.driver).authorization()
        wait = WebDriverWait(self.driver, 10)
        page = UserPage(self.driver)
        page.role_selection(UserPage.PROVIDER_ROLE)
        self.assertTrue(wait.until(EC.visibility_of_element_located(UserPage.CREATE_STRATEGY)))

    def test_role_selection_follower(self):
        LoginPage(self.driver).authorization()
        wait = WebDriverWait(self.driver, 10)
        page = UserPage(self.driver)
        page.role_selection(UserPage.FOLLOWER_ROLE)
        self.assertTrue(wait.until(EC.visibility_of_element_located(UserPage.PORTFOLIO_TAB)))



if __name__ == '__main__':
    unittest.main()
