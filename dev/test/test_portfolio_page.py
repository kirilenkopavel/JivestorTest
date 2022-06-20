import time
import unittest
import xmlrunner
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from dev.pages.login_page import LoginPage
from dev.pages.portfolio_page import PortfolioPage
from dev.pages.strategy_page import StrategyPage
from dev.pages.user_page import UserPage
from dev.test.chromedriver import ChromeDriver
from dev.test.test_strategy_page import TestStrategyPage


class TestPortfolio(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_add_strategies_button(self):
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.PORTFOLIO_TAB)
        page = PortfolioPage(self.driver)
        page.portfolio_review()
        page.add_strategies()
        self.assertEqual('https://dev-py.jivestor.com/traders', self.driver.current_url)

    def test_pause_and_play_strategy(self):
        wait = WebDriverWait(self.driver, 5)
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.PORTFOLIO_TAB)
        try:
            wait.until(EC.visibility_of_element_located(PortfolioPage.STRATEGY))
        except TimeoutException:
            StrategyPage(self.driver).add_in_portfolio()
        finally:
            page = PortfolioPage(self.driver)
            page.review_status_strategy()
            page.pause_strategy()
            self.assertTrue(wait.until(EC.visibility_of_element_located(PortfolioPage.PLAY)))
            self.assertTrue(wait.until(EC.visibility_of_element_located(PortfolioPage.STATUS_PAUSE)))
            page.play_strategy()
            self.assertTrue(wait.until(EC.visibility_of_element_located(PortfolioPage.PAUSE)))
            self.assertTrue(wait.until(EC.visibility_of_element_located(PortfolioPage.STATUS_PLAY)))

    def test_stop_and_play_strategy(self):
        wait = WebDriverWait(self.driver, 5)
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.PORTFOLIO_TAB)
        try:
            wait.until(EC.visibility_of_element_located(PortfolioPage.STRATEGY))
        except TimeoutException:
            StrategyPage(self.driver).add_in_portfolio()
        finally:
            page = PortfolioPage(self.driver)
            page.review_status_strategy()
            page.stop_strategy()
            self.assertTrue(wait.until(EC.visibility_of_element_located(PortfolioPage.PLAY)))
            self.assertTrue(wait.until(EC.visibility_of_element_located(PortfolioPage.STATUS_STOP)))
            page.play_strategy()
            self.assertTrue(wait.until(EC.visibility_of_element_located(PortfolioPage.STOP)))
            self.assertTrue(wait.until(EC.visibility_of_element_located(PortfolioPage.STATUS_PLAY)))

    def test_delete_strategy(self):
        wait = WebDriverWait(self.driver, 5)
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.PORTFOLIO_TAB)
        try:
            wait.until(EC.visibility_of_element_located(PortfolioPage.STRATEGY))
        except TimeoutException:
            StrategyPage(self.driver).add_in_portfolio()
        finally:
            self.assertTrue(wait.until(EC.visibility_of_element_located(PortfolioPage.STRATEGY)))
            page = PortfolioPage(self.driver)
            page.delete_strategy()
            self.assertTrue(wait.until(EC.visibility_of_element_located(PortfolioPage.ADD_STRATEGIES)))

    def test_settings_strategy_toggle_settings(self):
        wait = WebDriverWait(self.driver, 5)
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.PORTFOLIO_TAB)
        try:
            wait.until(EC.visibility_of_element_located(PortfolioPage.STRATEGY))
        except TimeoutException:
            StrategyPage(self.driver).add_in_portfolio()
        finally:
            self.assertTrue(wait.until(EC.visibility_of_element_located(PortfolioPage.STRATEGY)))
            PortfolioPage(self.driver).open_settings()
            for setting in TestStrategyPage.type_settings:
                StrategyPage(self.driver).toggle_settings(setting)
                if setting == StrategyPage.AUTO_TYPE:
                    self.assertEquals(self.driver.find_element(*StrategyPage.TEXT_DESCRIPTION).text.partition('для')[0],
                                      "Данная опция будет автоматически подбирать наиболее благоприятные настройки ")
                if setting == StrategyPage.PERCENT_OF_BALANCE_TYPE:
                    self.assertEquals(self.driver.find_element(*StrategyPage.TEXT_DESCRIPTION).text.partition('под')[0],
                                      "Введите процент от общего баланса который вы хотите выделить ")
                if setting == StrategyPage.FIX_SIZE_TYPE:
                    self.assertEquals(self.driver.find_element(*StrategyPage.TEXT_DESCRIPTION).text.partition(',')[0],
                                      "Введите фиксированный размер сделки")
                if setting == StrategyPage.PROPORTIONAL_LOT_TYPE:
                    self.assertEquals(self.driver.find_element(*StrategyPage.TEXT_DESCRIPTION).text.partition(',')[0],
                                      "Эта функция позволяет настроить динамический")

    def test_settings_edit_auto(self):
        wait = WebDriverWait(self.driver, 5)
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.PORTFOLIO_TAB)
        try:
            wait.until(EC.visibility_of_element_located(PortfolioPage.STRATEGY))
        except TimeoutException:
            StrategyPage(self.driver).add_in_portfolio()
        finally:
            self.assertTrue(wait.until(EC.visibility_of_element_located(PortfolioPage.STRATEGY)))
            PortfolioPage(self.driver).open_settings()
            page = StrategyPage(self.driver)
            page.toggle_settings(StrategyPage.AUTO_TYPE)
            page.save()
            time.sleep(3)
            PortfolioPage(self.driver).open_settings()
            self.assertEquals(self.driver.find_element(*StrategyPage.TEXT_DESCRIPTION).text.partition('для')[0],
                              "Данная опция будет автоматически подбирать наиболее благоприятные настройки ")

    def test_settings_edit_proportional(self):
        wait = WebDriverWait(self.driver, 5)
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.PORTFOLIO_TAB)
        try:
            wait.until(EC.visibility_of_element_located(PortfolioPage.STRATEGY))
        except TimeoutException:
            StrategyPage(self.driver).add_in_portfolio()
        finally:
            self.assertTrue(wait.until(EC.visibility_of_element_located(PortfolioPage.STRATEGY)))
            PortfolioPage(self.driver).open_settings()
            page = StrategyPage(self.driver)
            page.toggle_settings(StrategyPage.PROPORTIONAL_LOT_TYPE)
            page.save()
            time.sleep(3)
            PortfolioPage(self.driver).open_settings()
            self.assertEquals(self.driver.find_element(*StrategyPage.TEXT_DESCRIPTION).text.partition(',')[0],
                              "Эта функция позволяет настроить динамический")

    def test_settings_edit_fixed(self):
        wait = WebDriverWait(self.driver, 5)
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.PORTFOLIO_TAB)
        try:
            wait.until(EC.visibility_of_element_located(PortfolioPage.STRATEGY))
        except TimeoutException:
            StrategyPage(self.driver).add_in_portfolio()
        finally:
            self.assertTrue(wait.until(EC.visibility_of_element_located(PortfolioPage.STRATEGY)))
            PortfolioPage(self.driver).open_settings()
            page = StrategyPage(self.driver)
            page.toggle_settings(StrategyPage.FIX_SIZE_TYPE)
            page.save()
            time.sleep(3)
            PortfolioPage(self.driver).open_settings()
            self.assertEquals(self.driver.find_element(*StrategyPage.TEXT_DESCRIPTION).text.partition(',')[0],
                              "Введите фиксированный размер сделки")

    def test_settings_edit_percent(self):
        wait = WebDriverWait(self.driver, 5)
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.PORTFOLIO_TAB)
        try:
            wait.until(EC.visibility_of_element_located(PortfolioPage.STRATEGY))
        except TimeoutException:
            StrategyPage(self.driver).add_in_portfolio()
        finally:
            self.assertTrue(wait.until(EC.visibility_of_element_located(PortfolioPage.STRATEGY)))
            PortfolioPage(self.driver).open_settings()
            page = StrategyPage(self.driver)
            page.toggle_settings(StrategyPage.PERCENT_OF_BALANCE_TYPE)
            page.save()
            time.sleep(3)
            PortfolioPage(self.driver).open_settings()
            self.assertEquals(self.driver.find_element(*StrategyPage.TEXT_DESCRIPTION).text.partition('под')[0],
                              "Введите процент от общего баланса который вы хотите выделить ")


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='./test_reports'))
