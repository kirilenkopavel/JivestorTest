import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.login_page import LoginPage
from mgr.pages.moderation_page import Moderation
from mgr.pages.navigation_user import NavigationUser
from mgr.pages.wl_stats_page import WlStats
from mgr.test.chromedriver import ChromeDriver


class TestWlStats(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_add_note(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WL_STATS_TAB)
        page = WlStats(self.driver)
        text = page.add_note()
        description = wait.until(EC.presence_of_element_located(WlStats.DESCRIPTION)).text
        self.assertEqual(text, description)

    def test_edit_note(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WL_STATS_TAB)
        page = WlStats(self.driver)
        text = page.edit_note()
        description = wait.until(EC.presence_of_element_located(WlStats.DESCRIPTION)).text
        self.assertEqual(text, description)

    def test_delete_note(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WL_STATS_TAB)
        page = WlStats(self.driver)
        note = page.get_value(WlStats.DESCRIPTION)
        page.delete_note()
        new_note = page.get_value(WlStats.DESCRIPTION)
        self.assertNotEqual(note, new_note)

    def test_sorting_date(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WL_STATS_TAB)
        page = WlStats(self.driver)
        table = page.collect_table(WlStats.DATE)
        page.sort_by(WlStats.SORING_DATE)
        new_table = page.collect_table(WlStats.DATE)
        self.assertNotEqual(table, new_table)


if __name__ == '__main__':
    unittest.main()
