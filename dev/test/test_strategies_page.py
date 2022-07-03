import time
import unittest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from dev.pages.strategies_page import StrategiesPage
from dev.pages.strategy_page import StrategyPage
from dev.test.chromedriver import ChromeDriver


class TestStrategiesPage(unittest.TestCase):

    columns = {StrategiesPage.COLUMN_AGE,
               StrategiesPage.COLUMN_GROWTH,
               StrategiesPage.COLUMN_AVG,
               StrategiesPage.COLUMN_TOTAL,
               StrategiesPage.COLUMN_MAX,
               StrategiesPage.COLUMN_DD,
               StrategiesPage.COLUMN_RECOMMEN,
               StrategiesPage.COLUMN_PROFITABILITY
               }

    tabs = {StrategiesPage.TOP_GROWTH,
            StrategiesPage.MY_FAVORITES,
            StrategiesPage.RISING_STARS,
            StrategiesPage.TOP_POPULAR,
            StrategiesPage.TOP_RANK
            }

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_show_more(self):
        StrategiesPage(self.driver).show_more()
        element = self.driver.find_elements(*StrategiesPage.STRATEGY)
        self.assertEquals(20, len(element))

    def test_search_strategy(self):
        StrategiesPage(self.driver).search_strategy('Rodax')
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.presence_of_all_elements_located(StrategiesPage.STRATEGY))
        self.assertTrue(1 == len(elements))
        counter = self.driver.find_element(*StrategiesPage.COUNTER_TOP_RANK).text
        self.assertEquals('1', counter)

    def test_switching_tab(self):
        for tab in TestStrategiesPage.tabs:
            StrategiesPage(self.driver).switching_tab(self, tab)
            if tab == StrategiesPage.TOP_GROWTH:
                self.assertEquals('https://dev-py.jivestor.com/traders/growth', self.driver.current_url)
            elif tab == StrategiesPage.MY_FAVORITES:
                self.assertEquals('https://dev-py.jivestor.com/traders/favorites', self.driver.current_url)
            elif tab == StrategiesPage.RISING_STARS:
                self.assertEquals('https://dev-py.jivestor.com/traders/rising-stars', self.driver.current_url)
            elif tab == StrategiesPage.TOP_POPULAR:
                self.assertEquals('https://dev-py.jivestor.com/traders/top-popular', self.driver.current_url)
            else:
                self.assertEquals('https://dev-py.jivestor.com/traders', self.driver.current_url)

    def test_in_favorites(self):
        page = StrategiesPage(self.driver)
        page.in_favorites()
        page.driver.refresh()
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.presence_of_all_elements_located(StrategiesPage.STRATEGY))
        self.assertTrue(1 == len(elements))
        self.assertEquals('1', self.driver.find_element(*StrategiesPage.COUNTER_MY_FAVORITES).text)
        page.out_favorites()
        page.driver.refresh()
        self.assertEquals('0', self.driver.find_element(*StrategiesPage.COUNTER_MY_FAVORITES).text)

    def test_filtration_columns(self):
        page = StrategiesPage(self.driver)
        for column in TestStrategiesPage.columns:
            page.filtration_columns(column)
            time.sleep(3)
            wait = WebDriverWait(self.driver, 10)
            elements = wait.until(EC.presence_of_all_elements_located(StrategiesPage.STRATEGY))
            self.assertTrue(10 > len(elements))
            page.close_input(column)
            page.driver.refresh()
            time.sleep(3)

    def test_sorting_columns(self):
        page = StrategiesPage(self.driver)
        for column in TestStrategiesPage.columns:
            wait = WebDriverWait(self.driver, 10)
            if column == StrategiesPage.COLUMN_AGE:
                element = wait.until(EC.presence_of_element_located(StrategiesPage.AGE)).text
                page.sorting_columns(column, StrategiesPage.DOWN_ICON)
                element_1 = wait.until(EC.presence_of_element_located(StrategiesPage.AGE)).text
                self.assertNotEqual(element, element_1)
                page.sorting_columns(column, StrategiesPage.UP_ICON)
                element_2 = wait.until(EC.presence_of_element_located(StrategiesPage.AGE)).text
                self.assertNotEqual(element_2, element_1)
            elif column == StrategiesPage.COLUMN_GROWTH:
                element = wait.until(EC.presence_of_element_located(StrategiesPage.GROWTH)).text
                page.sorting_columns(column, StrategiesPage.DOWN_ICON)
                element_1 = wait.until(EC.presence_of_element_located(StrategiesPage.GROWTH)).text
                self.assertNotEqual(element, element_1)
                page.sorting_columns(column, StrategiesPage.UP_ICON)
                element_2 = wait.until(EC.presence_of_element_located(StrategiesPage.GROWTH)).text
                self.assertNotEqual(element_2, element_1)
            elif column == StrategiesPage.COLUMN_AVG:
                element = wait.until(EC.presence_of_element_located(StrategiesPage.AVG)).text
                page.sorting_columns(column, StrategiesPage.DOWN_ICON)
                element_1 = wait.until(EC.presence_of_element_located(StrategiesPage.AVG)).text
                self.assertNotEqual(element, element_1)
                page.sorting_columns(column, StrategiesPage.UP_ICON)
                element_2 = wait.until(EC.presence_of_element_located(StrategiesPage.AVG)).text
                self.assertNotEqual(element_2, element_1)
            elif column == StrategiesPage.COLUMN_TOTAL:
                element = wait.until(EC.presence_of_element_located(StrategiesPage.TOTAL)).text
                page.sorting_columns(column, StrategiesPage.DOWN_ICON)
                element_1 = wait.until(EC.presence_of_element_located(StrategiesPage.TOTAL)).text
                self.assertNotEqual(element, element_1)
                page.sorting_columns(column, StrategiesPage.UP_ICON)
                element_2 = wait.until(EC.presence_of_element_located(StrategiesPage.TOTAL)).text
                self.assertNotEqual(element_2, element_1)
            elif column == StrategiesPage.COLUMN_MAX:
                element = wait.until(EC.presence_of_element_located(StrategiesPage.MAX)).text
                page.sorting_columns(column, StrategiesPage.DOWN_ICON)
                element_1 = wait.until(EC.presence_of_element_located(StrategiesPage.MAX)).text
                self.assertNotEqual(element, element_1)
                page.sorting_columns(column, StrategiesPage.UP_ICON)
                element_2 = wait.until(EC.presence_of_element_located(StrategiesPage.MAX)).text
                self.assertNotEqual(element_2, element_1)
            elif column == StrategiesPage.COLUMN_DD:
                element = wait.until(EC.presence_of_element_located(StrategiesPage.DD)).text
                page.sorting_columns(column, StrategiesPage.DOWN_ICON)
                element_1 = wait.until(EC.presence_of_element_located(StrategiesPage.DD)).text
                self.assertNotEqual(element, element_1)
                page.sorting_columns(column, StrategiesPage.UP_ICON)
                element_2 = wait.until(EC.presence_of_element_located(StrategiesPage.DD)).text
                self.assertNotEqual(element_2, element_1)
            elif column == StrategiesPage.COLUMN_RECOMMEN:
                element = wait.until(EC.presence_of_element_located(StrategiesPage.RECOMMEN)).text
                page.sorting_columns(column, StrategiesPage.DOWN_ICON)
                element_1 = wait.until(EC.presence_of_element_located(StrategiesPage.RECOMMEN)).text
                self.assertNotEqual(element, element_1)
                page.sorting_columns(column, StrategiesPage.UP_ICON)
                element_2 = wait.until(EC.presence_of_element_located(StrategiesPage.RECOMMEN)).text
                self.assertNotEqual(element_2, element_1)
            elif column == StrategiesPage.COLUMN_PROFITABILITY:
                element = wait.until(EC.presence_of_element_located(StrategiesPage.PROFITABILITY)).text
                page.sorting_columns(column, StrategiesPage.DOWN_ICON)
                element_1 = wait.until(EC.presence_of_element_located(StrategiesPage.PROFITABILITY)).text
                self.assertNotEqual(element, element_1)
                page.sorting_columns(column, StrategiesPage.UP_ICON)
                element_2 = wait.until(EC.presence_of_element_located(StrategiesPage.PROFITABILITY)).text
                self.assertNotEqual(element_2, element_1)

    def test_open_strategy_page(self):
        StrategiesPage(self.driver).open_strategy_page()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located(StrategyPage.ADD_TO_NOT))
        self.assertTrue(element)


if __name__ == "__main__":
    unittest.main()
