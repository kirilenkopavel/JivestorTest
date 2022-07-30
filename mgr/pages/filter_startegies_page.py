import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.page import BasePage


class FilterStrategies(BasePage):

    ADVANCED_TAB = (By.XPATH, "//button[contains(text(), 'Advanced TAB settings')]")

