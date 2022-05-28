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
        time.sleep(4)
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
            page = StrategiesPage.switching_tab(self, tab)
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
        columns = {"//*[contains(text(), 'Возраст')]",
                   "//*[contains(text(), 'Прирост')]",
                   "//*[contains(text(), 'Средний за месяц')]",
                   "//*[contains(text(), 'Всего пунктов')]",
                   "//*[contains(text(), 'Макс. просадка')]",
                   "//*[contains(text(), 'Период просадки')]",
                   "//*[contains(text(), 'Реком. минимум')]",
                   "//*[contains(text(), 'Сделки в прибыли')]"
                   }
        for column in columns:
            page.filtration_columns(column)
            wait = WebDriverWait(self.driver, 10)
            elements = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, '//div[@class="rating-rank-data-wrap"]'))
            )
            self.assertTrue(10 > len(elements))
            page.close_input(column)
            page.driver.refresh()
            time.sleep(3)


if __name__ == "__main__":
    unittest.main()
