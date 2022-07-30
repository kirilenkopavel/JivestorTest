import random
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    NUMBERS_PAGE = (By.XPATH, '//button[@role="menuitemradio"]')

    def __init__(self, driver):
        self.driver = driver

    def collect_table(self, element):
        wait = WebDriverWait(self.driver, 5)
        names = list()
        try:
            elements = wait.until(EC.presence_of_all_elements_located(element))
            for name in elements:
                names.append(name.text)
                return names
        except TimeoutException:
            return names

    def get_value(self, web_element):
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.presence_of_all_elements_located(web_element))
        while 1:
            element = random.choice(elements).text
            if element != '':
                break
        return element.partition('\n')[0] \
            .lower()

    def switch_page(self, web_element):
        wait = WebDriverWait(self.driver, 10)
        pages = wait.until(EC.presence_of_all_elements_located(web_element))
        for page in pages:
            if page != pages[0]:
                random.choice(pages).click()
                time.sleep(9)
                break

    def sort_by(self, sorting_type):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(sorting_type)).click()
        time.sleep(12)

    def switch_tab(self, tab):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(tab)).click()
        time.sleep(5)

