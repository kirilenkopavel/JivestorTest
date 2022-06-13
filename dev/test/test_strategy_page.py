import time
import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from dev.pages.data_test import DataTest
from dev.pages.login_page import LoginPage
from dev.pages.portfolio_page import PortfolioPage
from dev.pages.provider_page import ProviderPage
from dev.pages.strategies_page import StrategiesPage
from dev.pages.strategy_page import StrategyPage
from dev.test.chromedriver import ChromeDriver


class TestStrategyPage(unittest.TestCase):

    type_settings = {StrategyPage.AUTO_TYPE,
                     StrategyPage.PERCENT_OF_BALANCE_TYPE,
                     StrategyPage.FIX_SIZE_TYPE,
                     StrategyPage.PROPORTIONAL_LOT_TYPE
                     }

    periods = {StrategyPage.ALL_PERIOD,
               StrategyPage.WEEK_PERIOD,
               StrategyPage.ONE_MONTH_PERIOD,
               StrategyPage.THREE_MONTH_PERIOD,
               StrategyPage.SIX_MONTH_PERIOD,
               StrategyPage.ONE_YEAR_PERIOD
               }

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL_STRATEGY)

    def tearDown(self):
        self.driver.close()

    def test_view_followers(self):
        StrategyPage(self.driver).view_followers()
        wait = WebDriverWait(self.driver, 10)
        self.assertTrue(wait.until(EC.visibility_of_all_elements_located(StrategyPage.FOLLOWERS)))

    def test_periods_table(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        from_date = self.driver.find_element(*StrategyPage.FROM_DATE) \
            .get_attribute('value')
        monthly_values = wait.until(EC.presence_of_all_elements_located(StrategyPage.MONTHLY_VALUES))
        for period in TestStrategyPage.periods:
            StrategyPage(self.driver).selection_period(period)
            if period != StrategyPage.ALL_PERIOD:
                new_from_date = self.driver.find_element(*StrategyPage.FROM_DATE) \
                    .get_attribute('value')
                new_monthly_values = wait.until(EC.presence_of_all_elements_located(StrategyPage.MONTHLY_VALUES))
                self.assertNotEquals(from_date, new_from_date)
                self.assertNotEquals(len(monthly_values), len(new_monthly_values))
            else:
                new_from_date = self.driver.find_element(*StrategyPage.FROM_DATE) \
                    .get_attribute('value')
                new_monthly_values = wait.until(EC.presence_of_all_elements_located(StrategyPage.MONTHLY_VALUES))
                self.assertEquals(from_date, new_from_date)
                self.assertEquals(len(monthly_values), len(new_monthly_values))

    def test_open_provider(self):
        StrategyPage(self.driver).open_provider_page()
        self.assertTrue(self.driver.find_element(By.XPATH, ProviderPage.COMMENT_TAB))

    def test_share_strategy(self):
        StrategyPage(self.driver).share_strategy()
        element = self.driver.find_element(*StrategyPage.WEB_ADDRESS_INPUT) \
            .get_attribute('value')
        self.assertEquals(self.driver.current_url, element)

    def test_in_my_favorites(self):
        StrategyPage(self.driver).in_favorites()
        LoginPage(self.driver).open_strategies_page()
        StrategiesPage(self.driver).switching_tab(StrategiesPage.MY_FAVORITES)
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.presence_of_all_elements_located(StrategiesPage.STRATEGY))
        self.assertTrue(1 == len(elements))
        self.assertEquals('1', self.driver.find_element(*StrategiesPage.COUNTER_MY_FAVORITES).text)
        page = StrategyPage(self.driver)
        page.open_strategy()
        page.in_favorites()
        LoginPage(self.driver).open_strategies_page()
        StrategiesPage(self.driver).switching_tab(StrategiesPage.MY_FAVORITES)
        self.assertEquals('0', self.driver.find_element(*StrategiesPage.COUNTER_MY_FAVORITES).text)

    def test_add_strategy_in_login(self):
        page = StrategyPage(self.driver)
        page.add_strategy()
        self.assertTrue(self.driver.find_element(*StrategyPage.LOGIN_BUTTON))
        page.in_login()
        self.assertEquals('https://dev-py.jivestor.com/login', self.driver.current_url)

    def test_add_strategy_in_register(self):
        page = StrategyPage(self.driver)
        page.add_strategy()
        page.in_register()
        self.assertEquals('https://dev-py.jivestor.com/registration', self.driver.current_url)

    def test_add_strategy_user_choose_account(self):
        LoginPage(self.driver).authorization()
        self.assertTrue(self.driver.find_element(*LoginPage.BURGER_MENU))
        StrategiesPage(self.driver).open_strategy_page()
        time.sleep(9)
        page = StrategyPage(self.driver)
        page.add_strategy_user()
        time.sleep(5)
        page.select_account(DataTest.DEMO_ACCOUNT_SELECT)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(DataTest.DEMO_ACCOUNT))
        self.assertTrue(element)

    def test_toggle_settings(self):
        LoginPage(self.driver).authorization()
        self.assertTrue(self.driver.find_element(*LoginPage.BURGER_MENU))
        time.sleep(5)
        PortfolioPage(self.driver).portfolio_review()
        StrategiesPage(self.driver).open_strategy_page()
        time.sleep(5)
        page = StrategyPage(self.driver)
        page.add_strategy_user()
        for setting in TestStrategyPage.type_settings:
            page.toggle_settings(setting)
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

    def test_add_portfolio_auto(self):
        LoginPage(self.driver).authorization()
        self.assertTrue(self.driver.find_element(*LoginPage.BURGER_MENU))
        PortfolioPage(self.driver).portfolio_review()
        StrategiesPage(self.driver).open_strategy_page()
        time.sleep(5)
        page = StrategyPage(self.driver)
        page.add_strategy_user()
        page.toggle_settings(StrategyPage.AUTO_TYPE)
        # page.check_copy(StrategyPage.COPY_AS_IS)
        page.save()
        page.in_portfolio()
        wait = WebDriverWait(self.driver, 10)
        strategies = wait.until(EC.visibility_of_all_elements_located(PortfolioPage.STRATEGY))
        self.assertTrue(len(strategies) == 1)

    def test_add_portfolio_percent(self):
        LoginPage(self.driver).authorization()
        self.assertTrue(self.driver.find_element(*LoginPage.BURGER_MENU))
        PortfolioPage(self.driver).portfolio_review()
        StrategiesPage(self.driver).open_strategy_page()
        time.sleep(5)
        page = StrategyPage(self.driver)
        page.add_strategy_user()
        page.toggle_settings(StrategyPage.PERCENT_OF_BALANCE_TYPE)
        page.input_lot("5")
        page.input_lot_min("5")
        page.input_lot_max("10")
        page.input_fixed_take("10")
        page.input_fixed_stop("10")
        page.input_stop_out("10")
        page.input_worst_dev("10")
        page.save()
        page.in_portfolio()
        wait = WebDriverWait(self.driver, 10)
        strategies = wait.until(EC.visibility_of_all_elements_located(PortfolioPage.STRATEGY))
        self.assertTrue(len(strategies) == 1)

    def test_add_portfolio_fixed(self):
        LoginPage(self.driver).authorization()
        self.assertTrue(self.driver.find_element(*LoginPage.BURGER_MENU))
        PortfolioPage(self.driver).portfolio_review()
        StrategiesPage(self.driver).open_strategy_page()
        time.sleep(5)
        page = StrategyPage(self.driver)
        page.add_strategy_user()
        page.toggle_settings(StrategyPage.FIX_SIZE_TYPE)
        page.input_lot("0.05")
        page.input_fixed_stop("10")
        page.input_fixed_take("10")
        page.input_stop_out("10")
        page.input_worst_dev("10")
        page.check_limit_trade("10", "10")
        page.save()
        page.in_portfolio()
        wait = WebDriverWait(self.driver, 10)
        strategies = wait.until(EC.visibility_of_all_elements_located(PortfolioPage.STRATEGY))
        self.assertTrue(len(strategies) == 1)

    def test_add_portfolio_proportional(self):
        LoginPage(self.driver).authorization()
        self.assertTrue(self.driver.find_element(*LoginPage.BURGER_MENU))
        PortfolioPage(self.driver).portfolio_review()
        StrategiesPage(self.driver).open_strategy_page()
        time.sleep(5)
        page = StrategyPage(self.driver)
        page.add_strategy_user()
        page.toggle_settings(StrategyPage.PROPORTIONAL_LOT_TYPE)
        page.input_lot("5")
        page.input_lot_min("5")
        page.input_lot_max("10")
        page.input_fixed_stop("10")
        page.input_fixed_take("10")
        page.input_stop_out("10")
        page.input_worst_dev("10")
        page.check_flipped_trading()
        page.save()
        page.in_portfolio()
        wait = WebDriverWait(self.driver, 10)
        strategies = wait.until(EC.visibility_of_all_elements_located(PortfolioPage.STRATEGY))
        self.assertTrue(len(strategies) == 1)


if __name__ == '__main__':
    unittest.main()
