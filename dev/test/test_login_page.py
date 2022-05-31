import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from dev.pages.login_page import LoginPage
from dev.test.chromedriver import ChromeDriver
from selenium.webdriver.support import expected_conditions as EC


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_open_brokers_page(self):
        page = LoginPage(self.driver)
        page.open_brokers_page()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, 'register_captcha')))
        self.assertTrue(element)

    def test_registered_button(self):
        page = LoginPage(self.driver)
        page.registered_in()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '//a[@ui-sref="menuLayout.connectTraderView({id: broker.id})"]')))
        self.assertTrue(len(element) > 0)

    def test_open_home_page(self):
        page = LoginPage(self.driver)
        page.open_home_page()
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        self.assertEqual('https://www.jivestor.com/', self.driver.current_url)


if __name__ == '__main__':
    unittest.main()