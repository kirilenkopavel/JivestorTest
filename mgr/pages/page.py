from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

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
