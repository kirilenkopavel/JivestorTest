import unittest

from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from mgr.pages.login_page import LoginPage
from mgr.pages.navigation_user import NavigationUser
from mgr.pages.payouts_vb_page import PayoutsVB
from mgr.pages.white_list_page import WhiteList
from mgr.pages.wl_stats_page import WlStats
from mgr.test.chromedriver import ChromeDriver


class TestPayoutsVB(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_filtration(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.PAYOUTS_VB_TAB)
        page = PayoutsVB(self.driver)
        table = page.collect_table(PayoutsVB.TRADING_STRATEGY)
        page.filtration()
        new_table = page.collect_table(PayoutsVB.TRADING_STRATEGY)
        self.assertNotEqual(table, new_table)



if __name__ == '__main__':
    unittest.main()
