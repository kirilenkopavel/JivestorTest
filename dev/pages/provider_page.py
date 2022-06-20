from selenium.webdriver.common.by import By

from dev.pages.page import BasePage


class ProviderPage(BasePage):

    COMMENT_TAB = "//*[contains(text(), 'Комментарии')]"
    ACTIV_STRATEGIES_TAB = "//*[contains(text(), 'Активные торговые стратегии')]"
    DELETE_STRATEGIES_TAB = "//*[contains(text(), 'Удаленные торговые стратегии')]"
    COMMENTS = (By.XPATH, '//div[@class="profile-review-text black ng-binding"]')
    COUNTER_COMMENTS = (By.XPATH, '//a[@ui-sref="menuLayout.profile.reviews({userId: user.hash_id})"]//span[2]')
    COUNTER_ACTIV_STRATEGIES = (By.XPATH, '//a[@ui-sref="menuLayout.profile.activeSystems({userId: user.hash_id})"]'
                                          '//span[2]')
    COUNTER_DELETE_STRATEGIES = (By.XPATH, '//a[@ui-sref="menuLayout.profile.deletedSystems({userId: user.hash_id})"]'
                                           '//span[2]')
    RATING = (By.XPATH, '//ul[@class="profile-rating-list"]')
    TABLE_ACTIV_STRATEGIES = (By.XPATH, "//*[contains(text(), 'Возраст')]")
    TABLE_DELETE_STRATEGIES = (By.XPATH, "//*[contains(text(), 'Удалено')]")
    FOLLOWERS = (By.XPATH, '//img[@class="wl-max-size ng-scope"]')
    NAME_PROVIDER = (By.XPATH, '//ul[@class="main-info-list"]/li[1]/strong[1]')
    NAME_FOLLOWER = (By.XPATH, '//ul[@class="main-info-list"]/li[1]/strong')
    STRATEGY = (By.XPATH, '//a[@class="wl-user-profile-system-link ng-binding"]')
    DELETE_STRATEGY = (By.XPATH, '//h1[@ng-if="tradeSystem.deleted"]')

    def selected_tab(self, tab):
        element = self.driver.find_element(By.XPATH, tab) \
            .click()


