import unittest

from selenium.webdriver.chrome import webdriver
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
        LoginPage(self.driver).open_brokers_page()
        wait = WebDriverWait(self.driver, 10)
        broker = wait.until(EC.presence_of_all_elements_located(LoginPage.BROKER))
        self.assertTrue(len(broker) > 0)

    def test_registered_button(self):
        LoginPage(self.driver).registered_in()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_all_elements_located(LoginPage.CAPTCHA_INPUT))
        self.assertTrue(element)

    def test_open_home_page(self):
        LoginPage(self.driver).open_home_page()
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        self.assertEqual('https://www.jivestor.com/', self.driver.current_url)

    def test_language_switching(self):
        LoginPage(self.driver).language_switching()
        self.assertTrue(len(self.driver.find_elements(*LoginPage.LANGUAGES)) == 15)


if __name__ == '__main__':
    unittest.main()
