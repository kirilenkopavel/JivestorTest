from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from dev.pages.data_test import DataTest
from dev.pages.page import BasePage


class LoginPage(BasePage):

    LOGIN_BUTTON = (By.XPATH, '//a[@class="wl-login-link ng-scope"]')
    LOGIN = (By.ID, 'login_email')
    PASSWORD = (By.ID, 'login_password')
    RUN_BUTTON = (By.XPATH, '//input[@type="submit"]')
    RUN_LANGUAGE = (By.ID, 'login_register_language')
    LANGUAGES = (By.XPATH, '//option[@class="ng-binding ng-scope"]')
    BURGER_MENU = (By.XPATH, '//a[@class="open-menu-user"]')
    MEET_OUR_TRADES = (By.XPATH, '//a[@ui-sref="menuLayout.tradeRatingMain"]')
    REGISTERED_TAB = (By.XPATH, '//a[@href="/registration"]')
    LOGIN_TAB = (By.XPATH, '//a[@href="/login"]')
    REMEMBER_CHECK = (By.XPATH, '//label[@for="login_remember"]')
    FORGOT_PASSWORD = (By.XPATH, '//a[@href="/password-restore"]')
    EMAIL_RESTORE = (By.ID, 'register_email')
    CAPTCHA_INPUT = (By.ID, 'register_captcha')
    RESTORE_BUTTON = (By.XPATH, '//input[@ng-click="restorePassword(restoreForm)"]')

    def login_in(self):
        element = self.driver.find_element(*LoginPage.LOGIN_BUTTON) \
            .click()

    def input_login_form(self):
        element = self.driver.find_element(*LoginPage.LOGIN) \
            .send_keys(*DataTest.EMAIL)
        element = self.driver.find_element(*LoginPage.PASSWORD) \
            .send_keys(*DataTest.PASSWORD)

    def submit(self):
        element = self.driver.find_element(*LoginPage.RUN_BUTTON) \
            .click()

    def language_switching(self):
        select = Select(self.driver.find_element(*LoginPage.RUN_LANGUAGE)) \
            .select_by_value('en')

    def authorization(self):
        element = self.driver.find_element(*LoginPage.LOGIN_BUTTON) \
            .click()
        element = self.driver.find_element(*LoginPage.LOGIN) \
            .send_keys(*DataTest.EMAIL)
        element = self.driver.find_element(*LoginPage.PASSWORD) \
            .send_keys(*DataTest.PASSWORD)
        element = self.driver.find_element(*LoginPage.RUN_BUTTON) \
            .click()

    def meet_our_trades(self):
        element = self.driver.find_element(*LoginPage.MEET_OUR_TRADES) \
            .click()

    def in_registered_tab(self):
        element = self.driver.find_element(*LoginPage.REGISTERED_TAB) \
            .click()

    def in_login_tab(self):
        element = self.driver.find_element(*LoginPage.LOGIN_TAB) \
            .click()

    def forgot_password(self):
        element = self.driver.find_element(*LoginPage.FORGOT_PASSWORD) \
            .click()
        element = self.driver.find_element(*LoginPage.EMAIL_RESTORE) \
            .send_keys(*DataTest.EMAIL)
        element = self.driver.find_element(*LoginPage.CAPTCHA_INPUT) \
            .send_keys('123456')
        element = self.driver.find_element(*LoginPage.RESTORE_BUTTON) \
            .click()

