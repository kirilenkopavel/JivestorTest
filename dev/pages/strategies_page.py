import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from dev.pages.page import BasePage
from dev.pages.user_page import UserPage


class StrategiesPage(BasePage):

    INPUT_SEARCH = (By.XPATH, '//input[@ng-change="setSearchVarible(userFilter.viewFields.name)"]')
    COUNTER_TOP_RANK = (By.XPATH, '//ul[@class="main-tabs-list no-tabs"]/li[1]//span[2]')
    SHOW_MORE_BUTTON = (By.XPATH, '//a[@ng-click="loadMore()"]')
    STRATEGY = (By.XPATH, '//div[@class="rating-rank-data-wrap"]')
    TOP_RANK = "//*[contains(text(), 'Top rank')]"
    TOP_GROWTH = '//a[@href="/traders/growth"]'
    MY_FAVORITES = '//a[@href="/traders/favorites"]'
    RISING_STARS = '//a[@href="/traders/rising-stars"]'
    TOP_POPULAR = '//a[@href="/traders/top-popular"]'
    ICON_FAVORITES = (By.XPATH, '//span[@ng-click="toggleFavorites()"]')
    COUNTER_MY_FAVORITES = (By.XPATH, '//ul[@class="main-tabs-list no-tabs"]/li[3]//span[2]')
    ICON_FILTRATION = (By.XPATH,  '//span[@class="icon-filter"]')
    INPUT_AGE = '//input[@ng-model="userFilter.viewFields.age.value"]'
    INPUT_GROWTH = '//input[@ng-model="userFilter.viewFields.growth.value"]'
    INPUT_AVG = '//input[@ng-model="userFilter.viewFields.avgPerMonth.value"]'
    INPUT_TOTAL = '//input[@ng-model="userFilter.viewFields.totalPips.value"]'
    INPUT_MAX = '//input[@ng-model="userFilter.viewFields.maxDrawDown.value"]'
    INPUT_DD = '//input[@ng-model="userFilter.viewFields.drawDownDuration.value"]'
    INPUT_RECOMMEN = '//input[@ng-model="userFilter.viewFields.recommendedMinimum.value"]'
    INPUT_PROFITABILITY = '//input[@ng-model="userFilter.viewFields.profitability.value"]'
    CLOSE_INPUT = (By.XPATH, '//span[@class="icon-close-sm"]')
    LANGUAGES = (By.XPATH, '//div[@class="header-language ng-scope"]')
    FILTER_OPERATOR = (By.XPATH, '//span[@class="main-filter-oper wl-change ng-binding"]')
    SORTING_UP = (By.XPATH, '//span[@class="rating-age-arrow-prev"]')
    STRATEGY_NAME = (By.XPATH, '//a[@ui-sref="menuLayout.performance({id: rating.tradeSystem})"]')
    COLUMN_AGE = "//*[contains(text(), 'Возраст')]"
    COLUMN_GROWTH = "//*[contains(text(), 'Прирост')]"
    COLUMN_AVG = "//*[contains(text(), 'Средний за месяц')]"
    COLUMN_TOTAL = "//*[contains(text(), 'Всего пунктов')]"
    COLUMN_MAX = "//*[contains(text(), 'Макс. просадка')]"
    COLUMN_DD = "//*[contains(text(), 'Период просадки')]"
    COLUMN_RECOMMEN = "//*[contains(text(), 'Реком. минимум')]"
    COLUMN_PROFITABILITY = "//*[contains(text(), 'Сделки в прибыли')]"
    DOWN_ICON = (By.XPATH, '//span[@class="rating-age-arrow-prev"]')
    UP_ICON = (By.XPATH, '//span[@class="rating-age-arrow-next"]')
    AGE = (By.XPATH, '//tr[@class="row-top ng-scope"]/td[2]')
    GROWTH = (By.XPATH, '//tr[@class="row-top ng-scope"]/td[3]')
    AVG = (By.XPATH, '//tr[@class="row-top ng-scope"]/td[4]')
    TOTAL = (By.XPATH, '//tr[@class="row-top ng-scope"]/td[5]')
    MAX = (By.XPATH, '//tr[@class="row-top ng-scope"]/td[6]')
    DD = (By.XPATH, '//tr[@class="row-top ng-scope"]/td[7]')
    RECOMMEN = (By.XPATH, '//tr[@class="row-top ng-scope"]/td[8]')
    PROFITABILITY = (By.XPATH, '//tr[@class="row-top ng-scope"]/td[9]')

    def search_strategy(self, strategy_name):
        element = self.driver.find_element(*StrategiesPage.INPUT_SEARCH)
        element.send_keys(strategy_name)
        element.send_keys(Keys.RETURN)
        time.sleep(3)

    def show_more(self):
        self.driver.find_element(*StrategiesPage.SHOW_MORE_BUTTON).click()
        time.sleep(7)

    def switching_tab(self, tab):
        self.driver.find_element(By.XPATH, tab).click()
        time.sleep(2)

    def in_favorites(self):
        elements = self.driver.find_elements(*StrategiesPage.ICON_FAVORITES)
        elements[0].click()
        self.driver.find_element(By.XPATH, StrategiesPage.MY_FAVORITES).click()
        time.sleep(2)

    def out_favorites(self):
        self.driver.find_element(*StrategiesPage.ICON_FAVORITES).click()

    def input(self, input_column, value):
        element = self.driver.find_element(By.XPATH, input_column)
        element.send_keys(value)
        element.send_keys(Keys.RETURN)
        time.sleep(5)

    def close_input(self, column):
        elements = self.driver.find_elements(*StrategiesPage.CLOSE_INPUT)
        if column == StrategiesPage.COLUMN_AGE:
            elements[0].click()
        elif column == StrategiesPage.COLUMN_GROWTH:
            elements[1].click()
        elif column == StrategiesPage.COLUMN_AVG:
            elements[2].click()
        elif column == StrategiesPage.COLUMN_TOTAL:
            elements[3].click()
        elif column == StrategiesPage.COLUMN_MAX:
            elements[4].click()
        elif column == StrategiesPage.COLUMN_DD:
            elements[5].click()
        elif column == StrategiesPage.COLUMN_RECOMMEN:
            elements[6].click()
        else:
            elements[7].click()

    def filtration_columns(self, column):
        self.driver.find_element(By.XPATH, column).click()
        wait = WebDriverWait(self.driver, 10)
        filters = wait.until(EC.presence_of_all_elements_located(StrategiesPage.ICON_FILTRATION))
        if column == StrategiesPage.COLUMN_AGE:
            filters[0].click()
            StrategiesPage.input(self, StrategiesPage.INPUT_AGE, 3250)
        elif column == StrategiesPage.COLUMN_GROWTH:
            filters[1].click()
            StrategiesPage.input(self, StrategiesPage.INPUT_GROWTH, 14000)
        elif column == StrategiesPage.COLUMN_AVG:
            filters[2].click()
            StrategiesPage.input(self, StrategiesPage.INPUT_AVG, 140)
        elif column == StrategiesPage.COLUMN_TOTAL:
            filters[3].click()
            StrategiesPage.input(self, StrategiesPage.INPUT_TOTAL, 144000)
        elif column == StrategiesPage.COLUMN_MAX:
            filters[4].click()
            StrategiesPage.input(self, StrategiesPage.INPUT_MAX, 79)
        elif column == StrategiesPage.COLUMN_DD:
            filters[5].click()
            StrategiesPage.input(self, StrategiesPage.INPUT_DD, 630)
        elif column == StrategiesPage.COLUMN_RECOMMEN:
            filters[6].click()
            StrategiesPage.input(self, StrategiesPage.INPUT_RECOMMEN, 26500)
        else:
            filters[7].click()
            StrategiesPage.input(self, StrategiesPage.INPUT_PROFITABILITY, 99)

    def sorting_columns(self, column, direction):
        self.driver.find_element(By.XPATH, column).click()
        wait = WebDriverWait(self.driver, 10)
        sorting_up = wait.until(EC.presence_of_all_elements_located(direction))
        try:
            if column == StrategiesPage.COLUMN_AGE:
                sorting_up[0].click()
            elif column == StrategiesPage.COLUMN_GROWTH:
                sorting_up[1].click()
            elif column == StrategiesPage.COLUMN_AVG:
                sorting_up[2].click()
            elif column == StrategiesPage.COLUMN_TOTAL:
                sorting_up[3].click()
            elif column == StrategiesPage.COLUMN_MAX:
                sorting_up[4].click()
            elif column == StrategiesPage.COLUMN_DD:
                sorting_up[5].click()
            elif column == StrategiesPage.COLUMN_RECOMMEN:
                sorting_up[6].click()
            else:
                sorting_up[7].click()
        finally:
            time.sleep(3)

    def open_strategy_page(self):
        UserPage(self.driver).open_page(UserPage.STRATEGIES_TAB)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(StrategiesPage.STRATEGY_NAME)).click()
