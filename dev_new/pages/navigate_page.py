from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dev_new.pages.data_test import DataTest
from dev_new.pages.page import BasePage


class NavigatePage(BasePage):

    STRATEGIES_TAB = (By.XPATH, '//a[@href="/traders"]')
    TRADING_TERMINAL_TAB = (By.XPATH, '//a[@href="/sf/terminal"]')
    BURGER_MENU = (By.XPATH, '//span[@class="fas fa-bars p-button-icon"]')
    STRATEGIES_MENU_BUTTON = (By.XPATH, '//span[@class="p-menuitem-icon fas fa-arrow-trend-up"]')
    TRADING_TERMINAL_MENU_BUTTON = (By.XPATH, '//span[@class="p-menuitem-icon fas fa-chart-line"]')
    PROFILE_MENU_BUTTON = (By.XPATH, '//span[@class="p-menuitem-icon fas fa-user"]')
    SETTING_MENU_BUTTON = (By.XPATH, '//span[@class="p-menuitem-icon fas fa-cog"]')
    LOGOUT_MENU_BUTTON = (By.XPATH, '//span[@class="p-menuitem-icon fas fa-sign-out-alt"]')
    CLOSE_MENU_ICON = (By.XPATH, '//span[@class="p-sidebar-close-icon pi pi-times"]')
    SELECT_ROLE_BUTTON = (By.XPATH, '//span[@class="p-dropdown-trigger-icon pi pi-chevron-down"]')
    FOLLOWER_ROLE = (By.XPATH, '//li[@aria-label="Follower"]')
    PROVIDER_ROLE = (By.XPATH, '//li[@aria-label="Provider"]')

    def selection_role(self, role):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(NavigatePage.SELECT_ROLE_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(role)).click()

    def open_page(self, tab):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(tab)).click()
