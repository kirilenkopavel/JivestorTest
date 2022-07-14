import time
from datetime import date

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.page import BasePage


class Moderation(BasePage):

    STATUS_NEW = (By.XPATH, '//div[@style="display: flex;"]/div[1]/button')
    STATUS_APPROVED = (By.XPATH, '//div[@style="display: flex;"]/div[2]/button')

    DESCRIPTION_TAB = (By.XPATH, "//span[contains(text(), 'Description')]")
    REVIEWS_TAB = (By.XPATH, "//span[contains(text(), 'Reviews')]")

    SORTING_DATE = (By.XPATH, '//th[@aria-colindex="2"]')
    DATE = (By.XPATH, '//td[@aria-colindex="2"]')
    EDIT_ICON = (By.XPATH, '//td[@aria-colindex="3"]//*[@class="bi-pencil-square b-icon bi"]')
    SUBMIT_DELETE = (By.XPATH, "//button[contains(text(), 'Delete')]")
    TEXT = (By.XPATH, '//td[@aria-colindex="3"]/div[4]')
    INPUT_TEXT = (By.XPATH, '//div[@class="inline-buttons__textarea-description"]/textarea ')
    APPROVED_ICON = (By.XPATH, '//div[@class="customIcons"]//a[@title="Approve"]')
    DELETE_ICON = (By.XPATH, '//div[@class="customIcons"]//a[@title="Delete"]')
    APPROVE_ALL = (By.XPATH, '//div[@class="approve-all__row"]//a')

    def switch(self, tab):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(tab)).click()
        time.sleep(5)

    def approve(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(Moderation.APPROVED_ICON)).click()
        time.sleep(5)

    def delete(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(Moderation.DELETE_ICON)).click()
        time.sleep(5)

    def approve_all(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(Moderation.APPROVE_ALL)).click()
        time.sleep(5)

    def edit_entry(self):
        wait = WebDriverWait(self.driver, 10)
        ActionChains(self.driver).move_to_element(Moderation.TEXT).perform()
        wait.until(EC.presence_of_element_located(Moderation.EDIT_ICON)).click()
        text = wait.until(EC.presence_of_element_located(Moderation.INPUT_TEXT))
        text.clear()
        text.send_keys('Autotest' + str(date.today()))
        wait.until(EC.presence_of_element_located(Moderation.EDIT_ICON)).click()
        time.sleep(5)

