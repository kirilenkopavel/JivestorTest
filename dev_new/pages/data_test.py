from selenium.webdriver.common.by import By


class DataTest(object):

    EMAIL = 'autotest@test.ru'
    PASSWORD = '12345678'
    STRATEGY = 'Rodax'
    DEMO_ACCOUNT = (By.XPATH, "//span[contains(text(), 'DEMO335631')]")
    DEMO_ACCOUNT_SELECT = '335631'
