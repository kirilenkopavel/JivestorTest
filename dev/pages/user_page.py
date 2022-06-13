from selenium.webdriver.common.by import By

from dev.pages.page import BasePage


class UserPage(BasePage):

    PORTFOLIO_TAB = (By.XPATH, '//ul[@ng-if="isAuthUser"]//a[@ui-sref="menuLayout.platform.portfolio"]')
    STRATEGIES_TAB = (By.XPATH, '//a[@ui-sref="menuLayout.tradeRatingMain"]')
