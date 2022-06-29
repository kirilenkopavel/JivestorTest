import random
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v101.indexed_db import Key

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.page import BasePage


class AccountsManager(BasePage):

    NEW_ACCOUNT_TAB = (By.XPATH, '//span[contains(text(), \'New accounts\')]')
    EXISTING_ACCOUNT_TAB = (By.XPATH, '//span[contains(text(), \'Existing accounts\')]')
    APPROVED_ACCOUNT_TAB = (By.XPATH, '//span[contains(text(), \'Approved accounts\')]')
    REJECTED_ACCOUNT_TAB = (By.XPATH, '//span[contains(text(), \'Rejected accounts\')]')
    DISCONNECTED_ACCOUNT_TAB = (By.XPATH, '//span[contains(text(), \'Disconnected accounts\')]')
    NOT_FUNDED_ACCOUNT_TAB = (By.XPATH, '//span[contains(text(), \'Not funded accounts\')]')
    EMAIL = (By.XPATH, '//tr[@class="table-output-colornull"]/td[4]')
    ACCOUNT = (By.XPATH, '//tr[@class="table-output-colornull"]/td[8]')
    TRADING_SERVER = (By.XPATH, '//tr[@class="table-output-colornull"]/td[9]')
    BROKER = (By.XPATH, '//tr[@class="table-output-colornull"]/td[7]')
    FILTERS = (By.ID, 'filter-roles__BV_toggle_')
    ACCOUNT_FILTER = (By.XPATH, "//a[contains(text(), 'Search by Account')]")
    EMAIL_FILTER = (By.XPATH, "//a[contains(text(), 'Search by Email')]")
    TRADING_SERVER_FILTER = (By.XPATH, "//a[contains(text(), 'Search by Trading Server')]")
    BROKER_FILTER = (By.XPATH, "//a[contains(text(), 'Search by Broker')]")
    INPUT_SEARCH = (By.XPATH, '//input[@class="search form-control form-control-sm"]')
    SEARCH_BUTTON = (By.XPATH, '//a[@class="btn-sm btn-secondary mr-2"]')
    NUMBERS_PAGE = (By.XPATH, '//button[@role="menuitemradio"]')
    SORTING_DATE = (By.XPATH, '//th[@aria-colindex="2"]/div')
    ADD_NEW_ACCOUNT = (By.XPATH, '//a[@class="btn-sm btn-success mr-2"]')
    HEADER = (By.XPATH, '//h4[@class="mb-0 font-size-18"]')
    APPROVE_ICON = (By.XPATH, '//a[@title="Approve"]')
    APPROVE_BUTTON = (By.XPATH, "//button[contains(text(), ' Approve')]")
    REJECT_ICON = (By.XPATH, '//a[@title="Reject"]')
    REJECT_BUTTON = (By.XPATH, "//button[contains(text(), ' Reject')]")
    TRADING_SERVER_BUTTON = (By.XPATH, '//div[@id="modal-window-account-approve___BV_modal_body_"]'
                                       '//button[@aria-haspopup="menu"]')
    SERVER_NAME = (By.XPATH, '//div[@id="modal-window-account-approve___BV_modal_content_"]'
                             '//li[@role="presentation"]/a')
    NOTES_BUTTON = (By.XPATH, '//td[@aria-colindex="13"]/button')
    COMMENT_INPUT = (By.ID, 'commentmessage-input')
    ADD_NOTE = (By.XPATH, "//button[contains(text(), 'Add note')]")
    COMMENTS = (By.ID, 'current_user_notes')
    CLOSE_ICON = (By.XPATH, '//div[@class="close-btn"]')

    ACCOUNT_NUMBER_INPUT = (By.XPATH, '//form[@id="create-an-account-manager"]//input[1]')
    EMAIL_INPUT = (By.XPATH, '//form[@id="create-an-account-manager"]//input[@type="email"]')
    WL_INPUT = (By.XPATH, '//*[@id="create-an-account-manager"]//input[@placeholder="Choose a WL"]')
    WL_DEV_PY = (By.XPATH, "//span[contains(text(), 'DEV-PY')]")


    def switching_tabs(self, tab):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(tab)).click()
        time.sleep(9)

    def search_filter(self, type_filter, value):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(AccountsManager.FILTERS)).click()
        wait.until(EC.presence_of_element_located(type_filter)).click()
        input_search = wait.until(EC.presence_of_element_located(AccountsManager.INPUT_SEARCH))
        input_search.clear()
        input_search.send_keys(value)
        wait.until(EC.presence_of_element_located(AccountsManager.SEARCH_BUTTON)).click()
        time.sleep(15)

    def open_add_account_page(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(AccountsManager.ADD_NEW_ACCOUNT)).click()
        time.sleep(5)

    def input_form_add_account(self):
        i = ''
        number = list()
        for x in range(7):
            number.append(i + str(random.randrange(9)))
        wait = WebDriverWait(self.driver, 10)
        account_number = wait.until(EC.presence_of_element_located(AccountsManager.ACCOUNT_NUMBER_INPUT))
        account_number.send_keys(number)
        wait.until(EC.presence_of_element_located(AccountsManager.EMAIL_INPUT)).send_keys('test05/06/@test.ru')
        time.sleep(5)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="create-an-account-manager"]'
                                                             '/div[3]/div/div/div[1]'))).click()
        element = wait.until(EC.presence_of_element_located(AccountsManager.WL_INPUT))
        element.send_keys('DEV-PY')
        element.send_keys(Keys.RETURN)
        # wait.until(EC.presence_of_element_located(AccountsManager.WL_DEV_PY)).click()
        return number

    def approved_account(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(AccountsManager.APPROVE_ICON)).click()
        try:
            wait.until(EC.presence_of_element_located(AccountsManager.TRADING_SERVER_BUTTON)).click()
            wait.until(EC.presence_of_element_located(AccountsManager.SERVER_NAME)).click()
            time.sleep(2)
        except TimeoutException:
            pass
        finally:
            wait.until(EC.presence_of_element_located(AccountsManager.APPROVE_BUTTON)).click()
            time.sleep(2)

    def rejected_account(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(AccountsManager.REJECT_ICON)).click()
        wait.until(EC.presence_of_element_located(AccountsManager.REJECT_BUTTON)).click()
        time.sleep(2)

    def add_comment(self):
        global comments
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(AccountsManager.NOTES_BUTTON)).click()
        try:
            comments = len(wait.until(EC.presence_of_all_elements_located(AccountsManager.COMMENTS)))
        except TimeoutException:
            comments = 0
        finally:
            wait.until(EC.presence_of_element_located(AccountsManager.COMMENT_INPUT)).send_keys("Autotest")
            wait.until(EC.presence_of_element_located(AccountsManager.ADD_NOTE)).click()
            time.sleep(3)
            return comments


