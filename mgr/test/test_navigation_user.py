import random
import time
import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.login_page import LoginPage
from mgr.pages.navigation_user import NavigationUser
from mgr.pages.registered_users_page import RegisteredUsers
from mgr.test.chromedriver import ChromeDriver


class TestNavigationUser(unittest.TestCase):

    tabs = {NavigationUser.DASHBOARD_TAB,
            NavigationUser.REGISTERED_USERS_TAB,
            NavigationUser.ACCOUNTS_MANAGER_TAB,
            NavigationUser.DEMO_ACCOUNTS_TAB,
            NavigationUser.WHO_FOLLOWS_WHOM_TAB,
            NavigationUser.TRADING_STRATEGIES_TAB,
            NavigationUser.MODERATION_TAB,
            NavigationUser.FILTER_STRATEGIES_TAB,
            NavigationUser.WHITE_LIST_TAB,
            NavigationUser.WL_STATS_TAB,
            NavigationUser.PAYOUTS_VB_TAB,
            NavigationUser.PAYOUTS_PB_TAB,
            NavigationUser.WITHDRAWALS_TAB,
            NavigationUser.USER_BALANCES_TAB,
            NavigationUser.WHITE_LABELS_TAB,
            NavigationUser.KNOWLEDGE_BASE_TAB,
            NavigationUser.MATCH_TRADE_TAB,
            NavigationUser.PORTFOLIO_CHANGES_TAB,
            NavigationUser.ACCOUNT_CREDENTIALS_TAB,
            NavigationUser.FIND_LOG_RECORDS_TAB,
            NavigationUser.SERVERS_MANAGER_TAB,
            NavigationUser.CREATE_TICKET_TAB,
            NavigationUser.ROLES_AND_PERMISSIONS_TAB,
            NavigationUser.CACHE_MANAGER_TAB,
            NavigationUser.MAINTENANCE_TAB,
            NavigationUser.TRANSLATIONS_TAB,
            NavigationUser.LOGS_TAB,
            # NavigationUser.PAYMENT_SERVICES_TAB
            }

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_hide_sidebar(self):
        LoginPage(self.driver).authorization()
        page = NavigationUser(self.driver)
        page.hide_sidebar()
        wait = WebDriverWait(self.driver, 10)
        self.assertTrue(wait.until(EC.visibility_of_element_located(NavigationUser.ICON_REGISTERED_USERS)))
        page.hide_sidebar()
        self.assertTrue(wait.until(EC.visibility_of_element_located(NavigationUser.REGISTERED_USERS_TAB)))

    def test_open_tab_menu(self):
        LoginPage(self.driver).authorization()
        wait = WebDriverWait(self.driver, 10)
        for tab in TestNavigationUser.tabs:
            NavigationUser(self.driver).open_page(tab)
            if tab == NavigationUser.REGISTERED_USERS_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'REGISTERED USERS')
            elif tab == NavigationUser.DASHBOARD_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'DASHBOARD')
            elif tab == NavigationUser.ACCOUNTS_MANAGER_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'ACCOUNTS MANAGER')
            elif tab == NavigationUser.DEMO_ACCOUNTS_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'DEMO ACCOUNTS')
            elif tab == NavigationUser.WHO_FOLLOWS_WHOM_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'WHO FOLLOWS WHOM')
            elif tab == NavigationUser.TRADING_STRATEGIES_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'TRADING STRATEGIES')
            elif tab == NavigationUser.MODERATION_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'MODERATION')
            elif tab == NavigationUser.FILTER_STRATEGIES_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'FILTER STRATEGIES')
            elif tab == NavigationUser.WHITE_LIST_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'WHITE LIST')
            elif tab == NavigationUser.WL_STATS_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'WL STATS')
            elif tab == NavigationUser.PAYOUTS_VB_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'PAYOUTS VB')
            elif tab == NavigationUser.PAYOUTS_PB_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'PAYOUTS PB')
            elif tab == NavigationUser.WITHDRAWALS_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'WITHDRAWALS')
            elif tab == NavigationUser.ACCOUNTS_MANAGER_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'ACCOUNTS MANAGER')
            elif tab == NavigationUser.USER_BALANCES_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'USER BALANCES')
            elif tab == NavigationUser.WHITE_LABELS_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'WHITE LABELS')
            elif tab == NavigationUser.KNOWLEDGE_BASE_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'KNOWLEDGE_BASE')
            elif tab == NavigationUser.MATCH_TRADE_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'MATCH TRADE')
            elif tab == NavigationUser.PORTFOLIO_CHANGES_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'PORTFOLIO CHANGES')
            elif tab == NavigationUser.ACCOUNT_CREDENTIALS_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'ACCOUNT CREDENTIALS')
            elif tab == NavigationUser.FIND_LOG_RECORDS_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'FIND LOG RECORDS')
            elif tab == NavigationUser.SERVERS_MANAGER_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'SERVERS MANAGER')
            elif tab == NavigationUser.CREATE_TICKET_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'CREATE A TICKET')
            elif tab == NavigationUser.WHITE_LABELS_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'WHITE LABELS')
            elif tab == NavigationUser.ROLES_AND_PERMISSIONS_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'ROLES AND PERMISSIONS')
            elif tab == NavigationUser.CACHE_MANAGER_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'CACHE MANAGER')
            elif tab == NavigationUser.WHITE_LABELS_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'WHITE LABELS')
            elif tab == NavigationUser.MAINTENANCE_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'MAINTENANCE')
            elif tab == NavigationUser.TRANSLATIONS_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'TRANSLATIONS')
            elif tab == NavigationUser.WHITE_LABELS_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'WHITE LABELS')
            elif tab == NavigationUser.LOGS_TAB:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'LOGS')
            else:
                self.assertEqual(wait.until(EC.visibility_of_element_located(NavigationUser.HEADER)).text,
                                 'PAYMENT SERVICES')

    def test_switching_wl(self):
        LoginPage(self.driver).authorization()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(NavigationUser.SELECT_WL)).click()
        list_wl = wait.until(EC.presence_of_all_elements_located(NavigationUser.WL))
        wl = random.choice(list_wl)
        name_wl = wl.text
        wl.click()
        name_button = wait.until(EC.visibility_of_element_located(NavigationUser.SELECT_WL)).text
        if name_wl == 'All':
            self.assertTrue(name_button == 'All White Labels')
        else:
            self.assertEqual(name_button, name_wl)


if __name__ == '__main__':
    unittest.main()
