import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.page import BasePage


class WhiteList(BasePage):

    INPUT = (By.XPATH, '//input[@class="search form-control form-control-sm"]')
    ADD_TO_BUTTON = (By.XPATH, "//a[contains(text(), 'Add to white list')]")
    CREATE_BUTTON = (By.XPATH, '//div[@id="modal-window-add-account___BV_modal_body_"]/button[1]')

    ACCOUNT = (By.XPATH, '//td[@aria-colindex="1"]')
    DATE = (By.XPATH, '//td[@aria-colindex="2"]')
    DELETE_ICON = (By.XPATH, '//td[@aria-colindex="3"]')
    DELETE_BUTTON = (By.XPATH, '//div[@id="modal-window-delete-account___BV_modal_body_"]/button[1]')

    SORTING_DATE = (By.XPATH, '//th[@aria-colindex="2"]/div')

    def add_to(self):
        wait = WebDriverWait(self.driver, 10)
        i = ''
        account = list()
        for x in range(6):
            account.append(i + str(random.randrange(9)))
        wait.until(EC.presence_of_element_located(WhiteList.INPUT)).send_keys(account)
        wait.until(EC.presence_of_element_located(WhiteList.ADD_TO_BUTTON)).click()
        wait.until(EC.presence_of_element_located(WhiteList.CREATE_BUTTON)).click()
        return account

    def delete_account(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(WhiteList.DELETE_ICON)).click()
        wait.until(EC.presence_of_element_located(WhiteList.DELETE_BUTTON)).click()
        time.sleep(3)
