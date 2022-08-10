import time

from selenium.webdriver.common.by import By

from mgr.pages.data_test import DataTest
from mgr.pages.page import BasePage


class LoginPage(BasePage):

    INPUT_LOGIN = (By.ID, 'login')
    INPUT_PASSWORD = (By.ID, 'password')
    SUBMIT = (By.ID, 'form-submit')
    LOGOUT = (By.ID, 'logout')
    USER_ICON = (By.XPATH, '//span[@class="fas fa-user p-button-icon"]')

    def authorization(self):
        self.driver.find_element(*LoginPage.INPUT_LOGIN).send_keys(*DataTest.EMAIL)
        self.driver.find_element(*LoginPage.INPUT_PASSWORD).send_keys(*DataTest.PASSWORD)
        self.driver.find_element(*LoginPage.SUBMIT).click()
        time.sleep(5)

