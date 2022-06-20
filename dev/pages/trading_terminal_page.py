import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from dev.pages.page import BasePage


class TradingTerminalPage(BasePage):

    TIME_FRAME = (By.XPATH, '//a[@ng-click="changeTimeFrame(timeFrame)"]')
    M1 = (By.XPATH, "//a[contains(text(), 'M1')]")
    M5 = (By.XPATH, "//a[contains(text(), 'M5')]")
    M15 = (By.XPATH, "//a[contains(text(), 'M15')]")
    H1 = (By.XPATH, "//a[contains(text(), 'H1')]")
    H4 = (By.XPATH, "//a[contains(text(), 'H4')]")
    D1 = (By.XPATH, "//a[contains(text(), 'D1')]")
    W1 = (By.XPATH, "//a[contains(text(), 'W1')]")
    WN = (By.XPATH, "//a[contains(text(), 'WN')]")
    ACTIV_TIME_FRAME = (By.XPATH, '//div[@class="chart-tabs"]//li[@class="ng-scope active"]/a')
    ORDER = (By.XPATH, '//a[@ng-click="openNewOrderPopup()"]')
    ORDER_SUBMIT = (By.XPATH, '//form[@ng-submit="placeOrder()"]//input[@type="submit"]')

    def selection_time_frame(self, element):
        time_frame = self.driver.find_element(*element)\
            .click()
        time.sleep(2)
        return time_frame.text

