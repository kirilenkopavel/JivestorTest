import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.page import BasePage


class PayoutsVB(BasePage):

    YARS_FILTER = (By.XPATH, '//div[@class="main-content-block__row"]/div[1]//button')
    YARS = (By.XPATH, '//div[@class="main-content-block__row"]/div[1]//a')
    MONTH_FILTER = (By.XPATH, '//div[@class="main-content-block__row"]/div[2]//button')
    MONTHS = (By.XPATH, '//div[@class="main-content-block__row"]/div[2]//a')
    BROKER_FILTER = (By.XPATH, '//div[@class="main-content-block__row"]/div[3]//button')
    BROKERS = (By.XPATH, '//div[@class="main-content-block__row"]/div[3]//a')
    TYPE_FILTER = (By.XPATH, '//div[@class="main-content-block__row"]/div[4]//button')
    TYPES = (By.XPATH, '//div[@class="main-content-block__row"]/div[4]//a')
    MODE_FILTER = (By.XPATH, '//div[@class="main-content-block__row"]/div[5]//button')
    MODES = (By.XPATH, '//div[@class="main-content-block__row"]/div[5]//a')
    SEARCH_BUTTON = (By.XPATH, '//div[@class="main-content-block__row"]//a[@type="button"]')

    TRADING_STRATEGY = (By.XPATH, '//td[@aria-colindex="2"]')

    def filtration(self):
        wait = WebDriverWait(self.driver, 10)
        yars = wait.until(EC.presence_of_all_elements_located(PayoutsVB.YARS))
        months = wait.until(EC.presence_of_all_elements_located(PayoutsVB.MONTHS))
        brokers = wait.until(EC.presence_of_all_elements_located(PayoutsVB.BROKERS))
        types = wait.until(EC.presence_of_all_elements_located(PayoutsVB.TYPES))
        modes = wait.until(EC.presence_of_all_elements_located(PayoutsVB.MODES))

        wait.until(EC.presence_of_element_located(PayoutsVB.YARS_FILTER)).click()
        yar = random.choice(yars)
        wait.until(EC.presence_of_element_located(yar)).click()

        wait.until(EC.presence_of_element_located(PayoutsVB.MONTH_FILTER)).click()
        month = random.choice(months)
        wait.until(EC.presence_of_element_located(month)).click()

        wait.until(EC.presence_of_element_located(PayoutsVB.BROKER_FILTER)).click()
        broker = random.choice(brokers)
        wait.until(EC.presence_of_element_located(broker)).click()

        wait.until(EC.presence_of_element_located(PayoutsVB.TYPE_FILTER)).click()
        type_ = random.choice(types)
        wait.until(EC.presence_of_element_located(type_)).click()

        wait.until(EC.presence_of_element_located(PayoutsVB.MODE_FILTER)).click()
        mode = random.choice(modes)
        wait.until(EC.presence_of_element_located(mode)).click()

        wait.until(EC.presence_of_element_located(PayoutsVB.SEARCH_BUTTON)).click()
        time.sleep(5)

