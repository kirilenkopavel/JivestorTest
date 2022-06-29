import time
import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from dev.pages.login_page import LoginPage
from dev.pages.statements_page import StatementsPage
from dev.pages.user_page import UserPage
from dev.test.chromedriver import ChromeDriver


class TestStatements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_trading_history(self):
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.STATEMENTS_TAB)
        wait = WebDriverWait(self.driver, 10)
        strategies = wait.until(EC.visibility_of_all_elements_located(StatementsPage.STRATEGIES))
        self.assertTrue(len(strategies) > 0)
        page = StatementsPage(self.driver)
        page.generate_statements(StatementsPage.STRATEGY)
        self.assertTrue(page.open_trading_history() == 0)
        page.generate_statements(StatementsPage.CUSTOM_TRADES)
        self.assertTrue(page.open_trading_history() > 0)


if __name__ == '__main__':
    unittest.main()
