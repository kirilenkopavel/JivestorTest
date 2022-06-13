import unittest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from dev.pages.login_page import LoginPage
from dev.test.chromedriver import ChromeDriver


class TestAuthorization(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_language_switching_form(self):
        page = LoginPage(self.driver)
        page.login_in()
        page.language_switching_form()
        self.assertTrue(self.driver.find_element(By.XPATH, "//*[contains(text(), 'Login')]"))

    def test_authorization(self):
        page = LoginPage(self.driver)
        page.login_in()
        page.input_login_form()
        page.submit()
        self.assertTrue(self.driver.find_element(*LoginPage.BURGER_MENU))

    def test_meet_our_traders(self):
        page = LoginPage(self.driver)
        page.login_in()
        page.meet_our_trades()
        self.assertTrue(self.driver.find_element(*LoginPage.LOGIN_BUTTON))

    def test_tab_switching(self):
        page = LoginPage(self.driver)
        page.login_in()
        page.in_registered_tab()
        self.assertTrue(self.driver.find_element(By.XPATH, '//div[@class="captcha-img"]'))
        page.in_login_tab()
        self.assertTrue(self.driver.find_element(*LoginPage.REMEMBER_CHECK))

    def test_forgot_password(self):
        page = LoginPage(self.driver)
        page.login_in()
        page.forgot_password()
        self.assertEquals('https://dev-py.jivestor.com/password-restore', self.driver.current_url)


if __name__ == "__main__":
    unittest.main()
