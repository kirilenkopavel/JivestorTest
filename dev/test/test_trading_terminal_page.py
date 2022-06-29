import time
import unittest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from dev.pages.login_page import LoginPage
from dev.pages.trading_terminal_page import TradingTerminalPage
from dev.pages.user_page import UserPage
from dev.test.chromedriver import ChromeDriver


class TestTradingTerminal(unittest.TestCase):

    time_frames = {TradingTerminalPage.M1,
                   TradingTerminalPage.M5,
                   TradingTerminalPage.M15,
                   TradingTerminalPage.H1,
                   TradingTerminalPage.H4,
                   TradingTerminalPage.D1,
                   TradingTerminalPage.W1,
                   TradingTerminalPage.WN
                   }

    trading_tools = {TradingTerminalPage.EUR_USD,
                     TradingTerminalPage.GBP_USD,
                     TradingTerminalPage.USD_JPY
                     }

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_switch_timeframe(self):
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.TRADING_TERMINAL_TAB)
        self.driver.refresh()
        wait = WebDriverWait(self.driver, 10)
        for time_frame in TestTradingTerminal.time_frames:
            selected_time_frame = TradingTerminalPage(self.driver).selection_time_frame(time_frame)
            open_time_frame = wait.until(EC.visibility_of_element_located(TradingTerminalPage.ACTIV_TIME_FRAME)).text
            self.assertEqual(selected_time_frame, open_time_frame)

    def test_switch_trading_tool(self):
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.TRADING_TERMINAL_TAB)
        self.driver.refresh()
        wait = WebDriverWait(self.driver, 10)
        for trading_tool in TestTradingTerminal.trading_tools:
            selected_trading_tool = TradingTerminalPage(self.driver).selection_trading_tool(trading_tool)
            open_trading_tool = wait.until(EC.visibility_of_element_located(TradingTerminalPage.ACTIV_TRADING_TOOL))\
                .text
            self.assertEqual(selected_trading_tool, open_trading_tool)

    def test_add_trading_tool(self):
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.TRADING_TERMINAL_TAB)
        self.driver.refresh()
        wait = WebDriverWait(self.driver, 10)
        number_tools = len(wait.until(EC.visibility_of_all_elements_located(TradingTerminalPage.TRADING_TOOL)))
        list_tools = TradingTerminalPage(self.driver).add_trading_tool('usdrub')
        new_number_tools = len(wait.until(EC.visibility_of_all_elements_located(TradingTerminalPage.TRADING_TOOL)))
        self.assertTrue(list_tools == 91)
        self.assertTrue(wait.until(EC.presence_of_element_located(TradingTerminalPage.USD_RUB)))
        self.assertTrue(number_tools < new_number_tools)
        self.driver.refresh()
        TradingTerminalPage(self.driver).delete_trading_tool('usdrub')
        self.driver.refresh()
        number_tools = len(wait.until(EC.visibility_of_all_elements_located(TradingTerminalPage.TRADING_TOOL)))
        self.assertTrue(number_tools < new_number_tools)

    def test_order_sell_market(self):
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.TRADING_TERMINAL_TAB)
        self.driver.refresh()
        wait = WebDriverWait(self.driver, 10)
        time.sleep(9)
        TradingTerminalPage(self.driver).open_order(TradingTerminalPage.SELL_ORDER, '.Market', ',1', '', '')
        time.sleep(10)

    def test_open_trade_sell(self):
        LoginPage(self.driver).authorization()
        UserPage(self.driver).open_page(UserPage.TRADING_TERMINAL_TAB)
        self.driver.refresh()
        time.sleep(9)
        wait = WebDriverWait(self.driver, 10)
        TradingTerminalPage(self.driver).open_trade(TradingTerminalPage.SELL_BUTTON, ',1')


if __name__ == '__main__':
    unittest.main()
