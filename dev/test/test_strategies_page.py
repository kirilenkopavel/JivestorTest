import time
import unittest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from dev.pages.strategies_page import StrategiesPage
from dev.test.chromedriver import ChromeDriver


class TestStrategiesPage(unittest.TestCase):

    columns = {"//*[contains(text(), 'Возраст')]",
               "//*[contains(text(), 'Прирост')]",
               "//*[contains(text(), 'Средний за месяц')]",
               "//*[contains(text(), 'Всего пунктов')]",
               "//*[contains(text(), 'Макс. просадка')]",
               "//*[contains(text(), 'Период просадки')]",
               "//*[contains(text(), 'Реком. минимум')]",
               "//*[contains(text(), 'Сделки в прибыли')]"
               }

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_show_more(self):
        page = StrategiesPage(self.driver)
        page.show_more()
        element = self.driver.find_elements(*StrategiesPage.STRATEGY)
        self.assertEquals(20, len(element))

    def test_search_strategy(self):
        page = StrategiesPage(self.driver)
        page.search_strategy('Rodax')
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="rating-rank-data-wrap"]')))
        self.assertTrue(1 == len(elements))
        counter = self.driver.find_element(*StrategiesPage.COUNTER_TOP_RANK).text
        self.assertEquals('1', counter)

    def test_switching_tab(self):
        tabs = {'//a[@href="/traders/growth"]',
                '//a[@href="/traders/favorites"]',
                '//a[@href="/traders/rising-stars"]',
                '//a[@href="/traders/top-popular"]',
                "//*[contains(text(), 'Топ рейтинг')]"
                }
        for tab in tabs:
            page = StrategiesPage(self.driver)
            page.switching_tab(self, tab)
            if tab == '//a[@href="/traders/growth"]':
                self.assertEquals('https://dev-py.jivestor.com/traders/growth', self.driver.current_url)
            elif tab == '//a[@href="/traders/favorites"]':
                self.assertEquals('https://dev-py.jivestor.com/traders/favorites', self.driver.current_url)
            elif tab == '//a[@href="/traders/rising-stars"]':
                self.assertEquals('https://dev-py.jivestor.com/traders/rising-stars', self.driver.current_url)
            elif tab == '//a[@href="/traders/top-popular"]':
                self.assertEquals('https://dev-py.jivestor.com/traders/top-popular', self.driver.current_url)
            else:
                self.assertEquals('https://dev-py.jivestor.com/traders', self.driver.current_url)

    def test_in_favorites(self):
        page = StrategiesPage(self.driver)
        page.in_favorites()
        page.driver.refresh()
        wait = WebDriverWait(self.driver, 50)
        elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="rating-rank-data-wrap"]')))
        self.assertTrue(1 == len(elements))
        self.assertEquals('1', self.driver.find_element(*StrategiesPage.COUNTER_MY_FAVORITES).text)
        page.out_favorites()
        page.driver.refresh()
        self.assertEquals('0', self.driver.find_element(*StrategiesPage.COUNTER_MY_FAVORITES).text)

    def test_filtration_columns(self):
        page = StrategiesPage(self.driver)
        for column in TestStrategiesPage.columns:
            page.filtration_columns(column)
            wait = WebDriverWait(self.driver, 10)
            elements = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, '//div[@class="rating-rank-data-wrap"]'))
            )
            self.assertTrue(10 > len(elements))
            page.close_input(column)
            page.driver.refresh()
            time.sleep(3)

    def test_sorting_columns(self):
        page = StrategiesPage(self.driver)
        for column in TestStrategiesPage.columns:
            wait = WebDriverWait(self.driver, 10)
            if column == "//*[contains(text(), 'Возраст')]":
                element = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[2]'))).text
                page.sorting_columns(column, "//span[@class=\"rating-age-arrow-prev\"]")
                element_1 = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[2]'))).text
                self.assertNotEqual(element, element_1)
                page.sorting_columns(column, "//span[@class=\"rating-age-arrow-next\"]")
                element_2 = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[2]'))).text
                self.assertNotEqual(element_2, element_1)
            elif column == "//*[contains(text(), 'Прирост')]":
                element = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[3]'))).text
                page.sorting_columns(column, "//span[@class=\"rating-age-arrow-prev\"]")
                element_1 = wait.until(EC.presence_of_element_located((By.XPATH, '//tr[@class="row-top ng-scope"]/td[3]'))).text
                self.assertNotEqual(element, element_1)
                page.sorting_columns(column, "//span[@class=\"rating-age-arrow-next\"]")
                element_2 = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[3]'))).text
                self.assertNotEqual(element_2, element_1)
            elif column == "//*[contains(text(), 'Средний за месяц')]":
                element = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[4]'))).text
                page.sorting_columns(column, "//span[@class=\"rating-age-arrow-prev\"]")
                element_1 = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[4]'))).text
                self.assertNotEqual(element, element_1)
                page.sorting_columns(column, "//span[@class=\"rating-age-arrow-next\"]")
                element_2 = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[4]'))).text
                self.assertNotEqual(element_2, element_1)
            elif column == "//*[contains(text(), 'Всего пунктов')]":
                element = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[5]'))).text
                page.sorting_columns(column, "//span[@class=\"rating-age-arrow-prev\"]")
                element_1 = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[5]'))).text
                self.assertNotEqual(element, element_1)
                page.sorting_columns(column, "//span[@class=\"rating-age-arrow-next\"]")
                element_2 = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[5]'))).text
                self.assertNotEqual(element_2, element_1)
            elif column == "//*[contains(text(), 'Макс. просадка')]":
                element = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[6]'))).text
                page.sorting_columns(column, "//span[@class=\"rating-age-arrow-prev\"]")
                element_1 = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[6]'))).text
                self.assertNotEqual(element, element_1)
                page.sorting_columns(column, "//span[@class=\"rating-age-arrow-next\"]")
                element_2 = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[6]'))).text
                self.assertNotEqual(element_2, element_1)
            elif column == "//*[contains(text(), 'Период просадки')]":
                element = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[7]'))).text
                page.sorting_columns(column, "//span[@class=\"rating-age-arrow-prev\"]")
                element_1 = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[7]'))).text
                self.assertNotEqual(element, element_1)
                page.sorting_columns(column, "//span[@class=\"rating-age-arrow-next\"]")
                element_2 = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[7]'))).text
                self.assertNotEqual(element_2, element_1)
            elif column == "//*[contains(text(), 'Реком. минимум')]":
                element = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[8]'))).text
                page.sorting_columns(column, "//span[@class=\"rating-age-arrow-prev\"]")
                element_1 = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[8]'))).text
                self.assertNotEqual(element, element_1)
                page.sorting_columns(column, "//span[@class=\"rating-age-arrow-next\"]")
                element_2 = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[8]'))).text
                self.assertNotEqual(element_2, element_1)
            elif column == "//*[contains(text(), 'Сделки в прибыли')]":
                element = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[9]'))).text
                page.sorting_columns(column, "//span[@class=\"rating-age-arrow-prev\"]")
                element_1 = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[9]'))).text
                self.assertNotEqual(element, element_1)
                page.sorting_columns(column, "//span[@class=\"rating-age-arrow-next\"]")
                element_2 = wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//tr[@class="row-top ng-scope"]/td[9]'))).text
                self.assertNotEqual(element_2, element_1)

    def test_open_strategy_page(self):
        page = StrategiesPage(self.driver)
        page.open_strategy_page()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'add to portfolio')]")))
        self.assertTrue(element)


if __name__ == "__main__":
    unittest.main()
