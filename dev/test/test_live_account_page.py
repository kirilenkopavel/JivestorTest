import random
import time
import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from dev.pages.live_account_page import LiveAccountPage
from dev.pages.login_page import LoginPage
from dev.pages.user_page import UserPage
from dev.test.chromedriver import ChromeDriver
from mgr.pages.navigation_user import NavigationUser


class TestLiveAccountPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_open_form_add_account(self):
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.LIVE_ACCOUNTS)
        wait = WebDriverWait(self.driver, 10)
        brokers = wait.until(EC.presence_of_all_elements_located(LiveAccountPage.BROKER))
        self.assertTrue(len(brokers) > 1)
        LiveAccountPage(self.driver).open_broker_form(random.choice(brokers))
        self.assertEqual(self.driver.find_element(*LiveAccountPage.HEADER).text, 'Подключить реальный счет')

    def test_add_mt4_account(self):
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.LIVE_ACCOUNTS)
        wait = WebDriverWait(self.driver, 10)
        brokers = wait.until(EC.presence_of_all_elements_located(LiveAccountPage.BROKER))
        self.assertTrue(len(brokers) > 1)
        page = LiveAccountPage(self.driver)
        page.open_broker_form(brokers[0])
        page.input_broker_form('Autotest', '777-777', 'Test-server', 'Demo', 'Test autotest mt4')
        page.choice_platform(LiveAccountPage.MT4)
        wait.until(EC.presence_of_element_located(LiveAccountPage.SUBMIT)).click()
        self.assertEqual(wait.until(EC.visibility_of_element_located(LiveAccountPage.OK_BUTTON)).text, "ОК")

    def test_add_mt5_account(self):
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.LIVE_ACCOUNTS)
        wait = WebDriverWait(self.driver, 10)
        brokers = wait.until(EC.presence_of_all_elements_located(LiveAccountPage.BROKER))
        self.assertTrue(len(brokers) > 1)
        page = LiveAccountPage(self.driver)
        page.open_broker_form(brokers[0])
        page.input_broker_form('Autotest', '777-777', 'Test-server', 'Demo', 'Test autotest mt4')
        page.choice_platform(LiveAccountPage.MT5)
        wait.until(EC.presence_of_element_located(LiveAccountPage.SUBMIT)).click()
        self.assertEqual(wait.until(EC.visibility_of_element_located(LiveAccountPage.OK_BUTTON)).text, "ОК")


if __name__ == '__main__':
    unittest.main()
