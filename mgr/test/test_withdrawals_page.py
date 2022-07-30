import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.login_page import LoginPage
from mgr.pages.navigation_user import NavigationUser
from mgr.pages.withdrawals_page import Withdrawals
from mgr.test.chromedriver import ChromeDriver


class TestWithdrawals(unittest.TestCase):

    tabs = {Withdrawals.PENDING_TAB,
            Withdrawals.PROCESSED_TAB,
            Withdrawals.REJECTED_TAB
            }

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_filtration_date(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WITHDRAWALS_TAB)
        page = Withdrawals(self.driver)
        for tab in TestWithdrawals.tabs:
            page.switch_tab(tab)
            table = page.collect_table(Withdrawals.DATE)
            page.filtration('01012015')
            new_table = page.collect_table(Withdrawals.DATE)
            self.assertNotEqual(table, new_table)

    def test_sorting_date(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WITHDRAWALS_TAB)
        page = Withdrawals(self.driver)
        for tab in TestWithdrawals.tabs:
            page.switch_tab(tab)
            table = page.collect_table(Withdrawals.DATE)
            page.sort_by(Withdrawals.SORTING_DATE)
            new_table = page.collect_table(Withdrawals.DATE)
            self.assertNotEqual(table, new_table)

    def test_paid(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WITHDRAWALS_TAB)
        page = Withdrawals(self.driver)
        page.switch_tab(Withdrawals.PENDING_TAB)
        invoice_number = page.get_value(Withdrawals.INVOICE)
        page.paid()
        new_invoice_number = page.get_value(Withdrawals.INVOICE)
        self.assertNotEqual(invoice_number, new_invoice_number)

    def test_reject(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WITHDRAWALS_TAB)
        page = Withdrawals(self.driver)
        page.switch_tab(Withdrawals.REJECTED_TAB)
        invoice_number = page.get_value(Withdrawals.INVOICE)
        page.reject()
        new_invoice_number = page.get_value(Withdrawals.INVOICE)
        self.assertNotEqual(invoice_number, new_invoice_number)

    def test_review_payment_details(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WITHDRAWALS_TAB)
        page = Withdrawals(self.driver)
        for tab in TestWithdrawals.tabs:
            page.switch_tab(tab)
            page.review_payment_details()
            header = wait.until(EC.presence_of_element_located(Withdrawals.HEADER)).text
            self.assertEqual(header, 'Payment Details')

    def test_remove_verification(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WITHDRAWALS_TAB)
        page = Withdrawals(self.driver)
        for tab in TestWithdrawals.tabs:
            page.switch_tab(tab)
            page.remove_verification()


if __name__ == '__main__':
    unittest.main()
