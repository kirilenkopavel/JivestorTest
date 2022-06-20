import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.login_page import LoginPage
from mgr.test.chromedriver import ChromeDriver


class TestAuthorization(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_authorization(self):
        LoginPage(self.driver).authorization()
        wait = WebDriverWait(self.driver, 10)
        self.assertTrue(wait.until(EC.visibility_of_element_located(LoginPage.LOGOUT)))


if __name__ == '__main__':
    unittest.main()
