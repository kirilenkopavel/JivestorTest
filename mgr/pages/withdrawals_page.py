import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.page import BasePage


class Withdrawals(BasePage):

    DATE_START = (By.ID, 'id="dateStart"')
    SEARCH_BUTTON = (By.XPATH, '//div[@class="main-content-block__row"]//a[@type="button"]')

    PENDING_TAB = (By.XPATH, '//ul[@role="tablist"]//a[@aria-posinset="1"]')
    PROCESSED_TAB = (By.XPATH, '//ul[@role="tablist"]//a[@aria-posinset="2"]')
    REJECTED_TAB = (By.XPATH, '//ul[@role="tablist"]//a[@aria-posinset="3"]')

    DATE = (By.XPATH, '//td[@aria-colindex="2"]')
    INVOICE = (By.XPATH, '//td[@aria-colindex="3"]')
    SORTING_DATE = (By.XPATH, '//th[@aria-colindex="2"]')
    PAID_ICON = (By.XPATH, '//td[@aria-colindex="9"]//a[@title="Paid"]')
    REJECT_ICON = (By.XPATH, '//td[@aria-colindex="9"]//a[@title="Reject"]')
    RESTORE_ICON = (By.XPATH, '/td[@aria-colindex="9"]//a[@title="Restore"]')
    PAYMENT_DETAILS = (By.XPATH, '//td[@aria-colindex="8"]')
    REMOVE_ICON = (By.XPATH, '//td[@aria-colindex="4"]//*[@class="bi-check-circle-fill b-icon bi text-success"]')
    REMOVE_SUBMIT = (By.XPATH, '//div[@id="modal-window-verified___BV_modal_body_"]/button[1]')

    HEADER = (By.ID, 'id="modal-window-payment-details___BV_modal_title_"')

    def filtration(self, date):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(Withdrawals.DATE_START)).click()
        ActionChains(self.driver).key_down(Keys.LEFT).key_down(Keys.LEFT).key_down(Keys.LEFT)
        wait.until(EC.presence_of_element_located(Withdrawals.DATE_START)).send_keys(date)
        wait.until(EC.presence_of_element_located(Withdrawals.SEARCH_BUTTON)).click()
        time.sleep(5)

    def paid(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(Withdrawals.PAID_ICON)).click()
        time.sleep(5)

    def reject(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(Withdrawals.REJECT_ICON)).click()
        time.sleep(5)

    def review_payment_details(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(Withdrawals.PAYMENT_DETAILS)).click()

    def remove_verification(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(Withdrawals.REMOVE_ICON)).click()
        wait.until(EC.presence_of_element_located(Withdrawals.REMOVE_SUBMIT)).click()

