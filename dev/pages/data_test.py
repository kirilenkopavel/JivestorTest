from selenium.webdriver.common.by import By


class DataTest(object):

    EMAIL = 'test.follover@gmail.com'
    PASSWORD = '12345678'
    STRATEGY = 'Rodax'
    DEMO_ACCOUNT = (By.XPATH, "//span[contains(text(), 'DEMO375740')]")
    DEMO_ACCOUNT_SELECT = '375740'
