import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from dev_new.pages.login_page import LoginPage
from dev_new.test.chromedriver import ChromeDriver


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_authorization(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        self.assertTrue(wait.until(EC.presence_of_element_located(LoginPage.USER_ICON)))

    def test_logout(self):
        wait = WebDriverWait(self.driver, 10)
        page = LoginPage(self.driver)
        page.authorization()
        page.logout()
        self.assertTrue(wait.until(EC.presence_of_element_located(LoginPage.LOGIN_BUTTON)))


if __name__ == '__main__':
    unittest.main()
