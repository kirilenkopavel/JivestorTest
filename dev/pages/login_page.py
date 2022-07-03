import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from dev.pages.data_test import DataTest
from dev.pages.page import BasePage


class LoginPage(BasePage):

    LOGIN_BUTTON = (By.XPATH, '//a[@class="wl-login-link ng-scope"]')
    LOGIN = (By.ID, 'login_email')
    PASSWORD = (By.ID, 'login_password')
    RUN_BUTTON = (By.XPATH, '//input[@type="submit"]')
    RUN_LANGUAGE_FORM = (By.ID, 'login_register_language')
    RUN_LANGUAGE = (By.XPATH, '//span[@class="wl-flag"]')
    LANGUAGES_FORM = (By.XPATH, '//option[@class="ng-binding ng-scope"]')
    LANGUAGES = (By.XPATH, '//a[@ng-click="guestSelectLanguage(language)"]')
    BURGER_MENU = (By.XPATH, '//a[@class="open-menu-user"]')
    MEET_OUR_TRADES = (By.XPATH, '//a[@ui-sref="menuLayout.tradeRatingMain"]')
    REGISTERED_TAB = (By.XPATH, '//a[@href="/registration"]')
    LOGIN_TAB = (By.XPATH, '//a[@href="/login"]')
    REMEMBER_CHECK = (By.XPATH, '//label[@for="login_remember"]')
    FORGOT_PASSWORD = (By.XPATH, '//a[@href="/password-restore"]')
    EMAIL_RESTORE = (By.ID, 'register_email')
    CAPTCHA_INPUT = (By.ID, 'register_captcha')
    RESTORE_BUTTON = (By.XPATH, '//input[@ng-click="restorePassword(restoreForm)"]')
    BROKERS_TAB = (By.XPATH, "//*[contains(text(), 'брокеры')]")
    REGISTERED_BUTTON = (By.XPATH, '//a[@ui-sref="withoutMenuLayout.auth.registration"]')
    HOME_PAGE_TAB = (By.XPATH, "//*[contains(text(), 'главная')]")
    STRATEGIES_TAB = (By.XPATH, '//a[@ui-sref="menuLayout.tradeRatingMain"]')
    BROKER = (By.XPATH, '//a[@ui-sref="menuLayout.connectTraderView({id: broker.id})"]')
    HEADER_FORM = (By.XPATH, "//h3[contains(text(), 'Login')]")

    def login_in(self):
        self.driver.find_element(*LoginPage.LOGIN_BUTTON).click()

    def input_login_form(self):
        self.driver.find_element(*LoginPage.LOGIN).send_keys(*DataTest.EMAIL)
        self.driver.find_element(*LoginPage.PASSWORD).send_keys(*DataTest.PASSWORD)

    def submit(self):
        self.driver.find_element(*LoginPage.RUN_BUTTON).click()

    def language_switching_form(self):
        Select(self.driver.find_element(*LoginPage.RUN_LANGUAGE_FORM)).select_by_value('en')

    def language_switching(self):
        self.driver.find_element(*LoginPage.RUN_LANGUAGE).click()
        time.sleep(1)
        languages = self.driver.find_elements(*LoginPage.LANGUAGES)
        for language in languages:
            language.click()
            time.sleep(1)

    def authorization(self):
        self.driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        self.driver.find_element(*LoginPage.LOGIN).send_keys(*DataTest.EMAIL)
        self.driver.find_element(*LoginPage.PASSWORD).send_keys(*DataTest.PASSWORD)
        self.driver.find_element(*LoginPage.RUN_BUTTON).click()
        time.sleep(3)

    def meet_our_trades(self):
        self.driver.find_element(*LoginPage.MEET_OUR_TRADES).click()

    def in_registered_tab(self):
        self.driver.find_element(*LoginPage.REGISTERED_TAB).click()

    def in_login_tab(self):
        self.driver.find_element(*LoginPage.LOGIN_TAB).click()

    def forgot_password(self):
        self.driver.find_element(*LoginPage.FORGOT_PASSWORD).click()
        self.driver.find_element(*LoginPage.EMAIL_RESTORE).send_keys(*DataTest.EMAIL)
        self.driver.find_element(*LoginPage.CAPTCHA_INPUT).send_keys('123456')
        self.driver.find_element(*LoginPage.RESTORE_BUTTON).click()

    def open_brokers_page(self):
        self.driver.find_element(*LoginPage.BROKERS_TAB).click()

    def registered_in(self):
        self.driver.find_element(*LoginPage.REGISTERED_BUTTON).click()

    def open_home_page(self):
        self.driver.find_element(*LoginPage.HOME_PAGE_TAB).click()

    def open_strategies_page(self):
        self.driver.find_element(*LoginPage.STRATEGIES_TAB).click()
