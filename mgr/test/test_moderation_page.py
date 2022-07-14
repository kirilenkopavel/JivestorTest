import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.login_page import LoginPage
from mgr.pages.moderation_page import Moderation
from mgr.pages.navigation_user import NavigationUser
from mgr.test.chromedriver import ChromeDriver


class TestModeration(unittest.TestCase):

    tabs = {Moderation.DESCRIPTION_TAB,
            Moderation.REVIEWS_TAB
            }

    statuses = {Moderation.STATUS_NEW,
                Moderation.STATUS_APPROVED
                }

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_sorting_date(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.MODERATION_TAB)
        page = Moderation(self.driver)
        for tab in TestModeration.tabs:
            for status in TestModeration.statuses:
                page.switch(tab)
                page.switch(status)
                table = page.collect_table(Moderation.DATE)
                page.sort_by(Moderation.SORTING_DATE)
                new_table = page.collect_table(Moderation.DATE)
                self.assertNotEqual(table, new_table)

    def test_approve_review(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.MODERATION_TAB)
        page = Moderation(self.driver)
        page.switch(Moderation.STATUS_NEW)
        page.switch(Moderation.REVIEWS_TAB)
        entry = wait.until(EC.presence_of_element_located(Moderation.TEXT)).text
        page.approve()
        page.switch(Moderation.STATUS_APPROVED)
        new_entry = wait.until(EC.presence_of_element_located(Moderation.TEXT)).text
        self.assertEqual(entry, new_entry)

    def test_approve_description(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.MODERATION_TAB)
        page = Moderation(self.driver)
        page.switch(Moderation.STATUS_NEW)
        page.switch(Moderation.DESCRIPTION_TAB)
        entry = wait.until(EC.presence_of_element_located(Moderation.TEXT)).text
        page.approve()
        page.switch(Moderation.STATUS_APPROVED)
        new_entry = wait.until(EC.presence_of_element_located(Moderation.TEXT)).text
        self.assertEqual(entry, new_entry)

    def test_delete_entry(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.MODERATION_TAB)
        page = Moderation(self.driver)
        for tab in TestModeration.tabs:
            for status in TestModeration.statuses:
                page.switch(tab)
                page.switch(status)
                entry = wait.until(EC.presence_of_element_located(Moderation.TEXT)).text
                page.delete()
                new_entry = wait.until(EC.presence_of_element_located(Moderation.TEXT)).text
                self.assertNotEqual(entry, new_entry)

    def test_approve_all(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.MODERATION_TAB)
        page = Moderation(self.driver)
        for tab in TestModeration.tabs:
            page.switch(tab)
            table = page.collect_table(Moderation.DATE)
            page.approve_all()
            new_table = page.collect_table(Moderation.DATE)
            self.assertNotEqual(table, new_table)

    def test_edit_entry(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.MODERATION_TAB)
        page = Moderation(self.driver)
        for tab in TestModeration.tabs:
            for status in TestModeration.statuses:
                page.switch(tab)
                page.switch(status)
                entry = wait.until(EC.presence_of_element_located(Moderation.TEXT)).text
                page.edit_entry()
                new_entry = wait.until(EC.presence_of_element_located(Moderation.TEXT)).text
                self.assertEqual(entry, new_entry)


if __name__ == '__main__':
    unittest.main()
