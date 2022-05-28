import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dev.pages.page import BasePage


class StrategiesPage(BasePage):

    INPUT_SEARCH = (By.XPATH, '//input[@ng-change="setSearchVarible(userFilter.viewFields.name)"]')
    COUNTER_TOP_RANK = (By.XPATH, '//ul[@class="main-tabs-list no-tabs"]/li[1]//span[2]')
    SHOW_MORE_BUTTON = (By.XPATH, '//a[@ng-click="loadMore()"]')
    STRATEGY = (By.XPATH, '//div[@class="rating-rank-data-wrap"]')
    TOP_RANK = (By.XPATH, "//*[contains(text(), 'Top rank')]")
    TOP_GROWTH = (By.XPATH, '//a[@href="/traders/growth"]')
    MY_FAVORITES = (By.XPATH, '//a[@href="/traders/favorites"]')
    RISING_STARS = (By.XPATH, '//a[@href="/traders/rising-stars"]')
    TOP_POPULAR = (By.XPATH, '//a[@href="/traders/top-popular"]')
    ICON_FAVORITES = (By.XPATH, '//span[@ng-click="toggleFavorites()"]')
    COUNTER_MY_FAVORITES = (By.XPATH, '//ul[@class="main-tabs-list no-tabs"]/li[3]//span[2]')
    ICON_FILTRATION = (By.XPATH,  '//span[@class="icon-filter"]')
    INPUT_AGE = '//input[@ng-model="userFilter.viewFields.age.value"]'
    INPUT_GROWTH = (By.XPATH, '//input[@ng-model="userFilter.viewFields.growth.value"]')
    INPUT_AVG = (By.XPATH, '//input[@ng-model="userFilter.viewFields.avgPerMonth.value"]')
    INPUT_TOTAL = (By.XPATH, '//input[@ng-model="userFilter.viewFields.totalPips.value"]')
    INPUT_MAX = (By.XPATH, '//input[@ng-model="userFilter.viewFields.maxDrawDown.value"]')
    INPUT_DD = (By.XPATH, '//input[@ng-model="userFilter.viewFields.drawDownDuration.value"]')
    INPUT_RECOMMEN = (By.XPATH, '//input[@ng-model="userFilter.viewFields.recommendedMinimum.value"]')
    INPUT_PROFITABILITY = (By.XPATH, '//input[@ng-model="userFilter.viewFields.profitability.value"]')
    CLOSE_INPUT = (By.XPATH, '//span[@class="icon-close-sm"]')
    LANGUAGES = (By.XPATH, '//div[@class="header-language ng-scope"]')

    def search_strategy(self, strategy_name):
        element = self.driver.find_element(*StrategiesPage.INPUT_SEARCH)
        element.send_keys(strategy_name)
        element.send_keys(Keys.RETURN)

    def show_more(self):
        element = self.driver.find_element(*StrategiesPage.SHOW_MORE_BUTTON) \
            .click()
        time.sleep(7)

    def switching_tab(self, tab):
        element = self.driver.find_element(By.XPATH, tab) \
            .click()
        time.sleep(2)

    def in_favorites(self):
        elements = self.driver.find_elements(*StrategiesPage.ICON_FAVORITES)
        element = elements[0] \
            .click()
        element = self.driver.find_element(*StrategiesPage.MY_FAVORITES) \
            .click()
        time.sleep(2)

    def out_favorites(self):
        element = self.driver.find_element(*StrategiesPage.ICON_FAVORITES) \
            .click()

    def input(self, input_column, value):
        element = self.driver.find_element(By.XPATH, input_column)
        element.send_keys(value)
        element.send_keys(Keys.RETURN)
        time.sleep(5)

    def close_input(self, column):
        elements = self.driver.find_elements(*StrategiesPage.CLOSE_INPUT)
        if column == "//*[contains(text(), 'Возраст')]":
            element = elements[0] \
                .click()
        elif column == "//*[contains(text(), 'Прирост')]":
            element = elements[1] \
                .click()
        elif column == "//*[contains(text(), 'Средний за месяц')]":
            element = elements[2] \
                .click()
        elif column == "//*[contains(text(), 'Всего пунктов')]":
            element = elements[3] \
                .click()
        elif column == "//*[contains(text(), 'Макс. просадка')]":
            element = elements[4] \
                .click()
        elif column == "//*[contains(text(), 'Период просадки')]":
            element = elements[5] \
                .click()
        elif column == "//*[contains(text(), 'Реком. минимум')]":
            element = elements[6] \
                .click()
        else:
            element = elements[7] \
                .click()

    def filtration_columns(self, column):
        element = self.driver.find_element(By.XPATH, column) \
            .click()
        elements = self.driver.find_elements(*StrategiesPage.ICON_FILTRATION)
        if column == "//*[contains(text(), 'Возраст')]":
            element = elements[0] \
                .click()
            StrategiesPage.input(self, '//input[@ng-model="userFilter.viewFields.age.value"]', 3250)
        elif column == "//*[contains(text(), 'Прирост')]":
            element = elements[1] \
                .click()
            StrategiesPage.input(self, '//input[@ng-model="userFilter.viewFields.growth.value"]', 14000)
        elif column == "//*[contains(text(), 'Средний за месяц')]":
            element = elements[2] \
                .click()
            StrategiesPage.input(self, '//input[@ng-model="userFilter.viewFields.avgPerMonth.value"]', 140)
        elif column == "//*[contains(text(), 'Всего пунктов')]":
            element = elements[3] \
                .click()
            StrategiesPage.input(self, '//input[@ng-model="userFilter.viewFields.totalPips.value"]', 144000)
        elif column == "//*[contains(text(), 'Макс. просадка')]":
            element = elements[4] \
                .click()
            StrategiesPage.input(self, '//input[@ng-model="userFilter.viewFields.maxDrawDown.value"]', 79)
        elif column == "//*[contains(text(), 'Период просадки')]":
            element = elements[5] \
                .click()
            StrategiesPage.input(self, '//input[@ng-model="userFilter.viewFields.drawDownDuration.value"]', 630)
        elif column == "//*[contains(text(), 'Реком. минимум')]":
            element = elements[6] \
                .click()
            StrategiesPage.input(self, '//input[@ng-model="userFilter.viewFields.recommendedMinimum.value"]', 26500)
        else:
            element = elements[7] \
                .click()
            StrategiesPage.input(self, '//input[@ng-model="userFilter.viewFields.profitability.value"]', 99)

