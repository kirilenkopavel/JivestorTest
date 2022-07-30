import time
import unittest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.login_page import LoginPage
from mgr.pages.navigation_user import NavigationUser
from mgr.pages.white_labels_page import WhiteLabels
from mgr.test.chromedriver import ChromeDriver


class TestWhiteLabels(unittest.TestCase):

    types_settings_broker = {WhiteLabels.GENERAL_SETTINGS_BROKER,
                             WhiteLabels.TRADING_SERVERS,
                             WhiteLabels.DESCRIPTION
                             }

    types_descriptions = {WhiteLabels.RISK_WARNING_TYPE,
                          WhiteLabels.CONDITIONS_TYPE,
                          WhiteLabels.PRIVACY_TYPE,
                          WhiteLabels.AFFILIATE_TYPE
                          }

    type_settings = {WhiteLabels.GENERAL_SETTINGS,
                     WhiteLabels.API_SETTINGS,
                     WhiteLabels.LINKS_SETTINGS,
                     WhiteLabels.SMPT_SETTINGS,
                     WhiteLabels.FEES_SETTINGS,
                     WhiteLabels.CUSTOM_JAVA_SCRIPT,
                     WhiteLabels.LEGAL_SETTINGS,
                     WhiteLabels.EMAIL,
                     WhiteLabels.ADD_BROKER
                     }

    def setUp(self):
        self.driver = webdriver.WebDriver(ChromeDriverManager().install(),
                                          chrome_options=ChromeDriver.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get(ChromeDriver.URL)

    def tearDown(self):
        self.driver.close()

    def test_sorting_id(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LABELS_TAB)
        page = WhiteLabels(self.driver)
        table = page.collect_table(WhiteLabels.ID)
        page.sort_by(WhiteLabels.SORTING_ID)
        new_table = page.collect_table(WhiteLabels.ID)
        self.assertNotEqual(table, new_table)
        page.show_deactivated()
        table = page.collect_table(WhiteLabels.ID)
        self.assertNotEqual(table, new_table)
        page.sort_by(WhiteLabels.SORTING_ID)
        new_table = page.collect_table(WhiteLabels.ID)
        self.assertNotEqual(table, new_table)

    def test_review_brokers(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LABELS_TAB)
        page = WhiteLabels(self.driver)
        size = page.review_brokers(0)
        brokers = str(len(wait.until(EC.presence_of_all_elements_located(WhiteLabels.BROKERS))))
        self.assertTrue(size, brokers)

    def test_sorting_name(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LABELS_TAB)
        page = WhiteLabels(self.driver)
        page.review_brokers(0)
        table = page.collect_table(WhiteLabels.NAME_BROKER)
        page.sort_by(WhiteLabels.SORTING_NAME)
        new_table = page.collect_table(WhiteLabels.NAME_BROKER)
        self.assertNotEqual(table, new_table)

    def test_invisible_broker(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LABELS_TAB)
        page = WhiteLabels(self.driver)
        page.review_brokers(0)
        status = page.invisible()
        new_status = wait.until(EC.presence_of_element_located(WhiteLabels.INVISIBLE_ICON)).text
        self.assertNotEqual(status, new_status)

    def test_delete_broker(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LABELS_TAB)
        page = WhiteLabels(self.driver)
        page.review_brokers(1)
        size_brokers = len(wait.until(EC.presence_of_all_elements_located(WhiteLabels.NAME_BROKER)))
        page.delete_broker()
        new_sice_brokers = len(wait.until(EC.presence_of_all_elements_located(WhiteLabels.NAME_BROKER)))
        self.assertTrue(size_brokers > new_sice_brokers)

    def test_open_settings_broker(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LABELS_TAB)
        page = WhiteLabels(self.driver)
        page.review_brokers(0)
        for type_settings in TestWhiteLabels.types_settings_broker:
            header = page.open_settings(type_settings)
            if type_settings == WhiteLabels.GENERAL_SETTINGS_BROKER:
                self.assertEqual(header, 'General Settings')
            elif type_settings == WhiteLabels.TRADING_SERVERS:
                self.assertEqual(header, 'Trading Servers')
            else:
                self.assertEqual(header, 'Equit - Description')
            self.driver.back()
            time.sleep(5)

    def test_edit_general_settings_brokers(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LABELS_TAB)
        page = WhiteLabels(self.driver)
        page.review_brokers(0)
        name_broker = wait.until(EC.presence_of_element_located(WhiteLabels.NAME_BROKER)).text
        page.open_settings(WhiteLabels.GENERAL_SETTINGS_BROKER)
        page.edit_general_settings_broker()
        self.driver.back()
        new_name_broker = wait.until(EC.presence_of_element_located(WhiteLabels.NAME_BROKER)).text
        self.assertNotEqual(name_broker, new_name_broker)

    def test_edit_server(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LABELS_TAB)
        page = WhiteLabels(self.driver)
        page.review_brokers(0)
        size_server = wait.until(EC.presence_of_element_located(WhiteLabels.COUNT_TRADING_SERVERS)).text
        page.open_settings(WhiteLabels.TRADING_SERVERS)
        trading_servers = str(len(wait.until(EC.presence_of_all_elements_located(WhiteLabels.TRADING_SERVER_NAME))))
        self.assertEqual(size_server, trading_servers)
        name_server = wait.until(EC.presence_of_element_located(WhiteLabels.TRADING_SERVER_NAME)).text
        page.edit_server()
        new_name_server = wait.until(EC.presence_of_element_located(WhiteLabels.TRADING_SERVER_NAME)).text
        self.assertNotEqual(name_server, new_name_server)

    def test_delete_servers(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LABELS_TAB)
        page = WhiteLabels(self.driver)
        page.review_brokers(0)
        page.open_settings(WhiteLabels.TRADING_SERVERS)
        name_server = wait.until(EC.presence_of_element_located(WhiteLabels.TRADING_SERVER_NAME)).text
        page.delete_server()
        new_name_server = wait.until(EC.presence_of_element_located(WhiteLabels.TRADING_SERVER_NAME)).text
        self.assertNotEqual(name_server, new_name_server)

    def test_add_servers(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LABELS_TAB)
        page = WhiteLabels(self.driver)
        page.review_brokers(0)
        page.open_settings(WhiteLabels.TRADING_SERVERS)
        create_name = page.add_server()
        name_server = wait.until(EC.presence_of_element_located(WhiteLabels.TRADING_SERVER_NAME)).text
        self.assertEqual(create_name, name_server)

    def test_edit_description(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LABELS_TAB)
        page = WhiteLabels(self.driver)
        page.review_brokers(0)
        page.open_settings(WhiteLabels.DESCRIPTION)
        text = page.edit_descriptions()
        page.open_settings(WhiteLabels.DESCRIPTION)
        for type_descriptions in TestWhiteLabels.types_descriptions:
            wait.until(EC.presence_of_element_located(WhiteLabels.TYPES_DESCRIPTIONS)).click()
            wait.until(EC.presence_of_element_located(type_descriptions)).click()
            description = wait.until(EC.presence_of_element_located(WhiteLabels.TEXT_INPUT)).text
            self.assertEqual(text, description)

    def test_open_settings(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LABELS_TAB)
        page = WhiteLabels(self.driver)
        page.review_brokers(0)
        for type_settings in TestWhiteLabels.type_settings:
            header = page.open_settings(type_settings)
            if type_settings == WhiteLabels.GENERAL_SETTINGS:
                self.assertEqual(header, 'General Settings')
            elif type_settings == WhiteLabels.API_SETTINGS:
                self.assertEqual(header, 'Links Settings')
            elif type_settings == WhiteLabels.LINKS_SETTINGS:
                self.assertEqual(header, 'SMTP Settings')
            elif type_settings == WhiteLabels.FEES_SETTINGS:
                self.assertEqual(header, 'Fees Settings')
            elif type_settings == WhiteLabels.CUSTOM_JAVA_SCRIPT:
                self.assertEqual(header, 'Custom Java Script')
            elif type_settings == WhiteLabels.LEGAL_SETTINGS:
                self.assertEqual(header, 'Legal Settings')
            elif type_settings == WhiteLabels.EMAIL:
                self.assertEqual(header, 'Emails')
            else:
                self.assertEqual(header, 'Add Broker')
            self.driver.back()
            time.sleep(5)

    def test_check_deactivated_wl(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LABELS_TAB)
        page = WhiteLabels(self.driver)
        table = page.collect_table(WhiteLabels.ID)
        page.check_deactivated()
        new_table = page.collect_table(WhiteLabels.ID)
        self.assertNotEqual(table, new_table)

    def test_add_trading_server(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LABELS_TAB)
        page = WhiteLabels(self.driver)
        page.open_settings(WhiteLabels.GENERAL_SETTINGS)
        server_name = page.add_trading_server()
        wait = WebDriverWait(self.driver, 10)
        note = wait.until(EC.presence_of_element_located(WhiteLabels.CUSTOM_TRADING_SERVER)).text
        self.assertEqual(server_name, note)

    def test_edit_trading_server(self):
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LABELS_TAB)
        page = WhiteLabels(self.driver)
        page.open_settings(WhiteLabels.GENERAL_SETTINGS)
        server_name = page.edit_server()
        wait = WebDriverWait(self.driver, 10)
        note = wait.until(EC.presence_of_element_located(WhiteLabels.CUSTOM_TRADING_SERVER)).text
        self.assertEqual(server_name, note)

    def test_delete_trading_server(self):
        wait = WebDriverWait(self.driver, 10)
        LoginPage(self.driver).authorization()
        NavigationUser(self.driver).open_page(NavigationUser.WHITE_LABELS_TAB)
        page = WhiteLabels(self.driver)
        try:
            note = wait.until(EC.presence_of_element_located(WhiteLabels.CUSTOM_TRADING_SERVER)).text
        except TimeoutException:
            page.add_trading_server()
            note = wait.until(EC.presence_of_element_located(WhiteLabels.CUSTOM_TRADING_SERVER)).text
        finally:
            page.delete_server()
            self.assertTrue()

if __name__ == '__main__':
    unittest.main()
