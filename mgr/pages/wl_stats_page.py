import random
import time
from datetime import date

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.page import BasePage


class WlStats(BasePage):

    ADD_NOTE = (By.XPATH, '//div[@class="page-title-box d-flex align-items-center justify-content-between"]//button')
    CHOOSE_WL = (By.ID, 'id="filter-strategies-wl__BV_toggle_"')
    DEV_PY = (By.XPATH, '//div[@id="filter-strategies-wl"]//a[contains(text(), \'DEV-PY\')]')
    INPUT_NOTE = (By.ID, 'id="new-note"')
    ADD_SUBMIT = (By.XPATH, "//button[contains(text(), 'Add note')]")

    DESCRIPTION = (By.XPATH, '//td[@aria-colindex="3"]')
    EDIT_ICON = (By.XPATH, '//td[@aria-colindex="4"]//div[@class="customIcons"]/div[1]')
    EDIT_INPUT = (By.XPATH, 'id="edit-note"')
    UPDATE_BUTTON = (By.XPATH, "//button[contains(text(), 'Update note')]")
    DELETE_ICON = (By.XPATH, '//td[@aria-colindex="4"]//div[@class="customIcons"]/div[2]')
    DELETE_BUTTON = (By.XPATH, "//button[contains(text(), 'Delete it')]")
    DATE = (By.XPATH, '//td[@aria-colindex="5"]')
    SORING_DATE = (By.XPATH, '//th[@aria-colindex="5"]')

    YARS_FILTER = (By.XPATH, '//div[@class="main-content-block__row"]/div[1]//button')
    YARS = (By.XPATH, '//div[@class="main-content-block__row"]/div[1]//a')
    MONTH_FILTER = (By.XPATH, '//div[@class="main-content-block__row"]/div[2]//button')
    MONTHS = (By.XPATH, '//div[@class="main-content-block__row"]/div[2]//a')
    SEARCH_BUTTON = (By.XPATH, '//div[@class="main-content-block__row"]//a[@type="button"]')
    TOTAL_USD = (By.XPATH, '//td[@aria-colindex="6"]')

    def add_note(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(WlStats.ADD_NOTE)).click()
        wait.until(EC.presence_of_element_located(WlStats.CHOOSE_WL)).click()
        wait.until(EC.presence_of_element_located(WlStats.DEV_PY)).click()
        text = wait.until(EC.presence_of_element_located(WlStats.INPUT_NOTE)).send_keys('Autotest' + str(date.today()))
        wait.until(EC.presence_of_element_located(WlStats.ADD_SUBMIT)).click()
        return text

    def edit_note(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(WlStats.EDIT_ICON)).click()
        wait.until(EC.presence_of_element_located(WlStats.EDIT_INPUT)).clear()
        text = wait.until(EC.presence_of_element_located(WlStats.EDIT_INPUT))\
            .send_keys('Autotest edit' + str(date.today()))
        wait.until(EC.presence_of_element_located(WlStats.UPDATE_BUTTON)).click()
        return text

    def delete_note(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(WlStats.DELETE_ICON)).click()
        wait.until(EC.presence_of_element_located(WlStats.DELETE_BUTTON)).click()

    def filtration_date(self):
        wait = WebDriverWait(self.driver, 10)
        yars = wait.until(EC.presence_of_all_elements_located(WlStats.YARS))
        months = wait.until(EC.presence_of_all_elements_located(WlStats.MONTHS))
        wait.until(EC.presence_of_element_located(WlStats.YARS_FILTER)).click()
        yar = random.choice(yars)
        wait.until(EC.presence_of_element_located(yar)).click()
        wait.until(EC.presence_of_element_located(WlStats.MONTH_FILTER)).click()
        month = random.choice(months)
        wait.until(EC.presence_of_element_located(month)).click()
        wait.until(EC.presence_of_element_located(WlStats.SEARCH_BUTTON)).click()
        time.sleep(5)
