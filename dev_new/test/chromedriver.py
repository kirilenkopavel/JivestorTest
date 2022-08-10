import unittest

from selenium.webdriver.chrome import webdriver


class ChromeDriver(unittest.TestCase):

    chrome_options = webdriver.Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--incognito')

    URL = "https://dev-new.jivestor.com/"
    URL_STRATEGY = "https://dev-py.jivestor.com/performance/19613"
    URL_PROVIDER = "https://dev-py.jivestor.com/profile/f5ea45bed2c5526c5dfafa0a5bd8d039/reviews"


