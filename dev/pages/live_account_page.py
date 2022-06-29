import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dev.pages.page import BasePage


class LiveAccountPage(BasePage):

    BROKER = (By.XPATH, '//a[@ui-sref="menuLayout.connectTraderView({id: broker.id})"]')
    ADD_EXISTING_ACCOUNT = (By.XPATH, '//a[contains(text(), \'У меня уже есть счет\')]')
    HEADER = (By.TAG_NAME, 'h1')
    FULL_NAME = (By.ID, 'open_account_full_name')
    PHONE_NUMBER = (By.ID, 'open_account_phone')
    ACCOUNT_NUMBER = (By.ID, 'open_account_account_number')
    TRADING_SERVER = (By.ID, 'open_account_server')
    ACCOUNT_TYPE = (By.ID, 'open_account_account_type')
    MESSAGE = (By.ID, 'open_account_message')
    PLATFORM = (By.XPATH, '//span[contains(text(), \'MetaTrader 4\')]')
    MT5 = (By.XPATH, '//label[@for="ui-multiselect-is_mt5-option-2"]')
    MT4 = (By.XPATH, '//label[@for="ui-multiselect-is_mt5-option-1"]')
    SUBMIT = (By.XPATH, '//a[@ng-click="submitForm(accountForm)"]')
    OK_BUTTON = (By.XPATH, '//*[@ng-click="closeSuccessMessage()"]')

    def open_broker_form(self, broker):
        broker.click()
        time.sleep(5)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(LiveAccountPage.ADD_EXISTING_ACCOUNT)).click()

    def input_broker_form(self, full_name, phone, server, account_type, message):
        wait = WebDriverWait(self.driver, 10)
        input_full_name = wait.until(EC.presence_of_element_located(LiveAccountPage.FULL_NAME))
        input_full_name.clear()
        input_full_name.send_keys(full_name)
        wait.until(EC.presence_of_element_located(LiveAccountPage.PHONE_NUMBER)).send_keys(phone)
        i = ''
        account = list()
        for x in range(6):
            account.append(i + str(random.randrange(9)))

        wait.until(EC.presence_of_element_located(LiveAccountPage.ACCOUNT_NUMBER)).send_keys(account)
        wait.until(EC.presence_of_element_located(LiveAccountPage.TRADING_SERVER)).send_keys(server)
        wait.until(EC.presence_of_element_located(LiveAccountPage.ACCOUNT_TYPE)).send_keys(account_type)
        wait.until(EC.presence_of_element_located(LiveAccountPage.MESSAGE)).send_keys(message)

    def choice_platform(self, platform):
        self.driver.find_element(*LiveAccountPage.PLATFORM).click()
        self.driver.find_element(*platform).click()


