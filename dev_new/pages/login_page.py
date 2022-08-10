from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dev_new.pages.data_test import DataTest
from dev_new.pages.page import BasePage


class LoginPage(BasePage):

    INPUT_EMAIL = (By.XPATH, '//input[@name="email"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="password"]')
    LOGIN_SUBMIT = (By.XPATH, '//div[@class="jv__login__submit"]/button')
    USER_ICON = (By.XPATH, '//span[@class="fas fa-user p-button-icon"]')
    LOGOUT = (By.XPATH, "//*[contains(text(), 'Logout')]")
    LOGIN_BUTTON = (By.XPATH, '//div[@class="jv__page-header__enter"]/button[1]')

    def authorization(self):
        self.driver.find_element(*LoginPage.INPUT_EMAIL).send_keys(*DataTest.EMAIL)
        self.driver.find_element(*LoginPage.INPUT_PASSWORD).send_keys(*DataTest.PASSWORD)
        self.driver.find_element(*LoginPage.LOGIN_SUBMIT).click()

    def logout(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(LoginPage.USER_ICON)).click()
        wait.until(EC.presence_of_element_located(LoginPage.LOGOUT)).click()


