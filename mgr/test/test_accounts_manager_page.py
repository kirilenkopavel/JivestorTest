import time
import unittest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.accounts_manager_page import AccountsManager
from mgr.pages.login_page import LoginPage
from mgr.pages.navigation_user import NavigationUser
from mgr.pages.page import BasePage
from mgr.test.chromedriver import ChromeDriver


class TestAccountsManager(unittest.TestCase):

    tabs = {AccountsManager.NEW_ACCOUNT_TAB,
            AccountsManager.EXISTING_ACCOUNT_TAB,
            AccountsManager.APPROVED_ACCOUNT_TAB,
            AccountsManager.REJECTED_ACCOUNT_TAB,
            AccountsManager.DISCONNECTED_ACCOUNT_TAB,
            AccountsManager.NOT_FUNDED_ACCOUNT_TAB
            }

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_switching_tabs(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.ACCOUNTS_MANAGER_TAB)
        page = AccountsManager(self.driver)
        for tab in TestAccountsManager.tabs:
            if tab != AccountsManager.NEW_ACCOUNT_TAB:
                table = page.collect_table(AccountsManager.EMAIL)
                page.switching_tabs(tab)
                new_table = page.collect_table(AccountsManager.EMAIL)
                self.assertNotEqual(table, new_table)

    def test_search_email(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.ACCOUNTS_MANAGER_TAB)
        for tab in TestAccountsManager.tabs:
            page = AccountsManager(self.driver)
            page.switching_tabs(tab)
            email = page.get_value(AccountsManager.EMAIL)
            page.search_filter(AccountsManager.EMAIL_FILTER, email)
            result = page.get_value(AccountsManager.EMAIL)
            self.assertEqual(email, result)
            self.driver.refresh()
            page.search_filter(AccountsManager.EMAIL_FILTER, '')
            try:
                page.switch_page(AccountsManager.NUMBERS_PAGE)
                self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
                new_email = page.get_value(AccountsManager.EMAIL)
                page.search_filter(AccountsManager.EMAIL_FILTER, new_email)
                new_result = page.get_value(AccountsManager.EMAIL)
                self.assertEqual(new_email, new_result)
                page.search_filter(AccountsManager.EMAIL_FILTER, '')
            except TimeoutException:
                pass

    def test_search_account(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.ACCOUNTS_MANAGER_TAB)
        for tab in TestAccountsManager.tabs:
            page = AccountsManager(self.driver)
            page.switching_tabs(tab)
            account = page.get_value(AccountsManager.ACCOUNT)
            page.search_filter(AccountsManager.ACCOUNT_FILTER, account)
            result = page.get_value(AccountsManager.ACCOUNT)
            self.assertEqual(account, result)
            self.driver.refresh()
            page.search_filter(AccountsManager.ACCOUNT_FILTER, '')
            try:
                page.switch_page(AccountsManager.NUMBERS_PAGE)
                self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
                new_account = page.get_value(AccountsManager.ACCOUNT)
                page.search_filter(AccountsManager.ACCOUNT_FILTER, new_account)
                new_result = page.get_value(AccountsManager.ACCOUNT)
                self.assertEqual(new_account, new_result)
                page.search_filter(AccountsManager.ACCOUNT_FILTER, '')
            except TimeoutException:
                pass

    def test_search_trading_server(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.ACCOUNTS_MANAGER_TAB)
        for tab in TestAccountsManager.tabs:
            print(tab)
            page = AccountsManager(self.driver)
            page.switching_tabs(tab)
            trading_server = page.get_value(AccountsManager.TRADING_SERVER)
            page.search_filter(AccountsManager.TRADING_SERVER_FILTER, trading_server)
            result = page.get_value(AccountsManager.TRADING_SERVER)
            self.assertEqual(trading_server, result)
            page.search_filter(AccountsManager.TRADING_SERVER_FILTER, '')
            try:
                page.switch_page(AccountsManager.NUMBERS_PAGE)
                self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
                new_trading_server = page.get_value(AccountsManager.TRADING_SERVER)
                page.search_filter(AccountsManager.TRADING_SERVER_FILTER, new_trading_server)
                new_result = page.get_value(AccountsManager.TRADING_SERVER)
                self.assertEqual(new_trading_server, new_result)
                page.search_filter(AccountsManager.TRADING_SERVER_FILTER, '')
            except TimeoutException:
                pass

    def test_search_broker(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.ACCOUNTS_MANAGER_TAB)
        for tab in TestAccountsManager.tabs:
            if tab == AccountsManager.APPROVED_ACCOUNT_TAB or tab == AccountsManager.DISCONNECTED_ACCOUNT_TAB or \
                    tab == AccountsManager.NOT_FUNDED_ACCOUNT_TAB:
                print(tab)
                page = AccountsManager(self.driver)
                page.switching_tabs(tab)
                broker = page.get_value(AccountsManager.BROKER)
                page.search_filter(AccountsManager.BROKER_FILTER, broker)
                result = page.get_value(AccountsManager.BROKER)
                self.assertEqual(broker, result)
                page.search_filter(AccountsManager.BROKER_FILTER, '')
                try:
                    page.switch_page(AccountsManager.NUMBERS_PAGE)
                    self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
                    new_broker = page.get_value(AccountsManager.BROKER)
                    page.search_filter(AccountsManager.BROKER_FILTER, new_broker)
                    new_result = page.get_value(AccountsManager.BROKER)
                    self.assertEqual(new_broker, new_result)
                    page.search_filter(AccountsManager.BROKER_FILTER, '')
                except TimeoutException:
                    pass

    def test_sorting_date(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.ACCOUNTS_MANAGER_TAB)
        for tab in TestAccountsManager.tabs:
            print(tab)
            page = AccountsManager(self.driver)
            page.switching_tabs(tab)
            email = page.get_value(AccountsManager.EMAIL)
            page.sort_by(AccountsManager.SORTING_DATE)
            page.sort_by(AccountsManager.SORTING_DATE)
            result = page.get_value(AccountsManager.EMAIL)
            self.assertNotEqual(email, result)
            page.sort_by(AccountsManager.SORTING_DATE)

    def test_open_add_account_page(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.ACCOUNTS_MANAGER_TAB)
        AccountsManager(self.driver).open_add_account_page()
        self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                         'ADD ACCOUNT')

    """def test_add_new_account(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.ACCOUNTS_MANAGER_TAB)
        page = AccountsManager(self.driver)
        page.open_add_account_page()
        page.input_form_add_account()"""

    def test_approved_account(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.ACCOUNTS_MANAGER_TAB)
        NavigationUser(self.driver).choice_wl(NavigationUser.DEV_PY)
        for tab in TestAccountsManager.tabs:
            if tab == AccountsManager.NEW_ACCOUNT_TAB or tab == AccountsManager.EXISTING_ACCOUNT_TAB or \
                    tab == AccountsManager.REJECTED_ACCOUNT_TAB:
                print(tab)
                page = AccountsManager(self.driver)
                page.switching_tabs(tab)
                account = page.get_value(AccountsManager.ACCOUNT)
                page.search_filter(AccountsManager.ACCOUNT_FILTER, account)
                page.approved_account()
                page.switching_tabs(AccountsManager.APPROVED_ACCOUNT_TAB)
                page.search_filter(AccountsManager.ACCOUNT_FILTER, account)
                new_account = page.get_value(AccountsManager.ACCOUNT)
                self.assertEqual(account, new_account)
                self.driver.refresh()

    def test_rejected_account(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.ACCOUNTS_MANAGER_TAB)
        NavigationUser(self.driver).choice_wl(NavigationUser.DEV_PY)
        for tab in TestAccountsManager.tabs:
            if tab == AccountsManager.NEW_ACCOUNT_TAB or tab == AccountsManager.EXISTING_ACCOUNT_TAB or \
                    tab == AccountsManager.APPROVED_ACCOUNT_TAB:
                print(tab)
                page = AccountsManager(self.driver)
                page.switching_tabs(tab)
                account = page.get_value(AccountsManager.ACCOUNT)
                page.search_filter(AccountsManager.ACCOUNT_FILTER, account)
                page.rejected_account()
                page.switching_tabs(AccountsManager.REJECTED_ACCOUNT_TAB)
                page.search_filter(AccountsManager.ACCOUNT_FILTER, account)
                new_account = page.get_value(AccountsManager.ACCOUNT)
                self.assertEqual(account, new_account)
                self.driver.refresh()

    def test_add_comment(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.ACCOUNTS_MANAGER_TAB)
        for tab in TestAccountsManager.tabs:
            page = AccountsManager(self.driver)
            page.switching_tabs(tab)
            comments = page.add_comment()
            new_comments = len(wait.until(EC.presence_of_all_elements_located(AccountsManager.COMMENTS)))
            wait.until(EC.presence_of_element_located(AccountsManager.CLOSE_ICON)).click()
            self.assertTrue(new_comments > comments)
            counter = wait.until(EC.presence_of_element_located(AccountsManager.NOTES_BUTTON)).text
            self.assertEqual(str(new_comments), counter)



if __name__ == '__main__':
    unittest.main()
