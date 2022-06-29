import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.page import BasePage


class NavigationUser(BasePage):

    BURGER = (By.ID, 'vertical-menu-btn')
    SIDEBAR = (By.ID, 'my-element')
    J_LOGO = (By.XPATH, '//span[@class="logo-sm"]')
    JIVESTOR_LOGO = (By.XPATH, '//span[@class="logo-sm"]')
    SUBMENU = (By.XPATH, '//a[@class="is-parent has-arrow"]')
    REGISTERED_USERS_TAB = "//span[contains(text(), 'Registered users')]"
    DASHBOARD_TAB = "//span[contains(text(), 'Dashboard')]"
    ACCOUNTS_MANAGER_TAB = "//a[contains(text(), 'Accounts manager')]"
    DEMO_ACCOUNTS_TAB = "//a[contains(text(), 'Demo accounts')]"
    WHO_FOLLOWS_WHOM_TAB = "//a[contains(text(), 'Who follows whom')]"
    TRADING_STRATEGIES_TAB = "//a[contains(text(), 'Trading strategies')]"
    MODERATION_TAB = "//a[contains(text(), 'Moderation')]"
    FILTER_STRATEGIES_TAB = "//a[contains(text(), 'Filter strategies')]"
    WHITE_LIST_TAB = "//a[contains(text(), 'White list')]"
    WL_STATS_TAB = "//a[contains(text(), 'WL stats')]"
    PAYOUTS_VB_TAB = "//a[contains(text(), 'Payouts VB')]"
    PAYOUTS_PB_TAB = "//a[contains(text(), 'Payouts PB')]"
    WITHDRAWALS_TAB = "//a[contains(text(), 'Withdrawals')]"
    USER_BALANCES_TAB = "//a[contains(text(), 'User balances')]"
    WHITE_LABELS_TAB = "//span[contains(text(), 'White Labels')]"
    KNOWLEDGE_BASE_TAB = "//a[contains(text(), 'Knowledge base')]"
    MATCH_TRADE_TAB = "//a[contains(text(), 'Match trade')]"
    PORTFOLIO_CHANGES_TAB = "//a[contains(text(), 'Portfolio changes')]"
    ACCOUNT_CREDENTIALS_TAB = "//a[contains(text(), 'Account credentials')]"
    SERVERS_MANAGER_TAB = "//a[contains(text(), 'Servers manager')]"
    CREATE_TICKET_TAB = "//a[contains(text(), 'Create a ticket')]"
    FIND_LOG_RECORDS_TAB = "//a[contains(text(), 'Find log records')]"
    ROLES_AND_PERMISSIONS_TAB = "//a[contains(text(), 'Roles and permissions')]"
    CACHE_MANAGER_TAB = "//a[contains(text(), 'Cache manager')]"
    MAINTENANCE_TAB = "//a[contains(text(), 'Maintenance')]"
    TRANSLATIONS_TAB = "//a[contains(text(), 'Translations')]"
    LOGS_TAB = "//a[contains(text(), 'Logs')]"
    PAYMENT_SERVICES_TAB = "//a[contains(text(), 'Payment services')]"

    REGISTERED_USERS = (By.XPATH, "//span[contains(text(), 'Registered users')]")
    ICON_REGISTERED_USERS = (By.XPATH, '//i[@class="bx bx-key"]')
    HEADER = (By.XPATH, '//h4[@class="mb-0 font-size-18"]')
    SELECT_WL = (By.ID, 'current-user-wl__BV_toggle_')
    WL = (By.XPATH, '//ul[@aria-labelledby="current-user-wl__BV_toggle_"]//a')
    DEV_PY = (By.ID, 'white-label-46')

    def hide_sidebar(self):
        self.driver.find_element(*NavigationUser.BURGER).click()

    def open_page(self, tab):
        wait = WebDriverWait(self.driver, 3)
        while 1:
            try:
                wait.until(EC.visibility_of_element_located((By.XPATH, tab))).click()
                time.sleep(3)
                break
            except TimeoutException:
                elements = self.driver.find_elements(*NavigationUser.SUBMENU)
                for element in elements:
                    element.click()

    def choice_wl(self, wl):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(NavigationUser.SELECT_WL)).click()
        self.driver.find_element(*wl).click()
        time.sleep(9)

