import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from dev.pages.provider_page import ProviderPage
from dev.test.chromedriver import ChromeDriver


class TestProviderPage(unittest.TestCase):

    tabs = {ProviderPage.COMMENT_TAB,
            ProviderPage.ACTIV_STRATEGIES_TAB,
            ProviderPage.DELETE_STRATEGIES_TAB
            }

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL_PROVIDER)

    def tearDown(self):
        self.driver.close()

    def test_switching_tabs(self):
        wait = WebDriverWait(self.driver, 10)
        for tab in TestProviderPage.tabs:
            ProviderPage(self.driver).selected_tab(tab)
            if tab == ProviderPage.COMMENT_TAB:
                self.assertTrue(wait.until(EC.visibility_of_all_elements_located(ProviderPage.RATING)))
            elif tab == ProviderPage.ACTIV_STRATEGIES_TAB:
                self.assertTrue(wait.until(EC.visibility_of_all_elements_located(ProviderPage.TABLE_ACTIV_STRATEGIES)))
            else:
                self.assertTrue(wait.until(EC.visibility_of_all_elements_located(ProviderPage.TABLE_DELETE_STRATEGIES)))

    def test_open_follower_page(self):
        ProviderPage(self.driver).selected_tab(ProviderPage.COMMENT_TAB)
        wait = WebDriverWait(self.driver, 10)
        followers = wait.until(EC.visibility_of_all_elements_located(ProviderPage.FOLLOWERS))
        follower = followers[1] \
            .click()
        self.assertTrue()


if __name__ == '__main__':
    unittest.main()
