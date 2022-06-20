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
        wait = WebDriverWait(self.driver, 10)
        for time_frame in TestTradingTerminal.time_frames:
            selected_time_frame = TradingTerminalPage(self.driver).selection_time_frame(time_frame)
            open_time_frame = wait.until(EC.visibility_of_element_located(TradingTerminalPage.ACTIV_TIME_FRAME)).text
            self.assertEqual(selected_time_frame, open_time_frame)


if __name__ == '__main__':
    unittest.main()
