from selenium.webdriver.chrome import webdriver


class ChromeDriver:

    chrome_options = webdriver.Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--incognito')
    # chrome_options.add_argument('--lang=en-GB')

    URL = "https://mgr-dev-py.jivestor.com/login"
    # URL = "https://mgr-stage.jivestor.com/login"

    