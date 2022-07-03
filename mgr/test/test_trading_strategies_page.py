import unittest

from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from mgr.test.chromedriver import ChromeDriver


class TestTradingStrategies(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
