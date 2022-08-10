import random
import time
from datetime import date

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mgr.pages.page import BasePage


class WhiteLabels(BasePage):

    SORTING_ID = (By.XPATH, '//th[@aria-colindex="2"]')
    ID = (By.XPATH, '//td[@aria-colindex="2"]')
    DEACTIVATED = (By.ID, 'id="checkbox-1"')
    BROKERS = (By.XPATH, '//td[@aria-colindex="7"]/a')
    NAME_WL = (By.XPATH, '//td[@aria-colindex="3"]')

    NAME_BROKER = (By.XPATH, '//td[@aria-colindex="2"]')
    SORTING_NAME = (By.XPATH, '//th[@aria-colindex="2"]')
    INVISIBLE_ICON = (By.XPATH, '//td[@aria-colindex="4"]/a')
    UPDATE = (By.XPATH, '//div[@id="broker-visible-modal-window___BV_modal_body_"]/button')
    DELETE_ICON = (By.XPATH, '//td[@aria-colindex="6"]//a[@title="Remove"]')
    DELETE_SUBMIT = (By.XPATH, '//div[@id="delete-broker-modal-window___BV_modal_body_"]/button[1]')
    SETTINGS_BROKER_BUTTON = (By.XPATH, '//td[@aria-colindex="6"]//button')
    GENERAL_SETTINGS_BROKER = (By.XPATH, '//td[@aria-colindex="6"]//li[1]')
    TRADING_SERVERS = (By.XPATH, '//td[@aria-colindex="6"]//li[2]')
    DESCRIPTION = (By.XPATH, '//td[@aria-colindex="6"]//li[3]')
    COUNT_TRADING_SERVERS = (By.XPATH, '//td[@aria-colindex="5"]')

    HEADER = (By.XPATH, '//h4//span[@aria-current="location"]')

    BROKER_NAME_INPUT = (By.ID, 'id="broker_name"')
    WEIGHT_INPUT = (By.ID, 'id="weight"')
    ACCOUNT_LINK_INPUT = (By.ID, 'id="open_account_link"')
    EMAIL_INPUT = (By.ID, 'id="email"')
    CHECK_LOGO = (By.ID, 'id="broker-hide-logo-in-invoice"')
    UPDATE_GENERAL_SETTINGS = (By.XPATH, '//div[@class="content-block mt-4"]/button')
    CLOSE_MODAL_GENERAL_SETTINGS = (By.XPATH, '//div[@id="modal-update-broker-wl-success___BV_modal_body_"]/button')

    TRADING_SERVER_NAME = (By.XPATH, '//div[@class="trading-servers-flex-wrapper__item"]/div')
    EDIT_SERVER_BUTTON = (By.XPATH, '//div[@class="trading-servers-flex-wrapper"]/div[2]/button')
    DELETE_SERVER_BUTTON = (By.XPATH, '//div[@class="trading-servers-flex-wrapper"]/div[3]/button')
    SUBMIT_DELETE_SERVER = (By.XPATH, '//div[@id="delete-modal-window___BV_modal_body_"]//button[1]')
    ADD_SERVER_BUTTON = (By.XPATH, "//*[contains(text(), 'Add Server')]")
    UPDATE_SERVER_NAME_INPUT = (By.ID, 'id="update-server-name"')
    UPDATE_SERVER_MASK = (By.ID, 'id="update-server-mask"')
    UPDATE_SERVER_BUTTON = (By.XPATH, '//button[@class="btn btn-sm btn-success pl-3 pr-3 btn-secondary"]')
    CLOSE_MODAL_EDIT_SERVERS = (By.XPATH, '//div[@id="modal-update-broker-wl-trading-servers-success___BV_modal_body_"]'
                                          '/button')
    CLOSE_MODAL_DELETE_SERVERS = (By.XPATH, '//div[@id="modal-update-broker-wl-trading-servers-delete-success___'
                                            'BV_modal_body_"]/button')
    NAME_SERVER_ADD_INPUT = (By.XPATH, '//input[@placeholder="Enter server name"]')
    MASK_ADD_INPUT = (By.XPATH, '//input[@placeholder="Enter server mask"]')
    CREATE_ADD_SERVER = (By.XPATH, '//button[@class="btn btn-sm btn-success pl-3 pr-3 btn-secondary"]')
    CLOSE_MODAL_ADD_SERVERS = (By.XPATH, 'btn btn btn-secondary pl-3 pr-3 ml-2 btn-secondary btn-sm')

    LANGUAGES_BUTTON = (By.ID, 'id="languages"')
    LANGUAGES = (By.XPATH, '//div[@class="dropdown b-dropdown dropdown-wlList show btn-group"]/ul[1]/li')
    TYPES_DESCRIPTIONS = (By.XPATH, '//div[@class="dropdown b-dropdown mr-2 btn-group"]')
    RISK_WARNING_TYPE = (By.XPATH, "//a[contains(text(), 'risk warning')]")
    CONDITIONS_TYPE =(By.XPATH, "//a[contains(text(), 'terms and conditions')]")
    PRIVACY_TYPE = (By.XPATH, "//a[contains(text(), 'privacy')]")
    AFFILIATE_TYPE = (By.XPATH, "//a[contains(text(), 'terms affiliate')]")
    TEXT_INPUT =(By.XPATH, '//div[@id="broker-description"]/div[2]')
    UPDATE_DESCRIPTIONS_BUTTON = (By.XPATH, '//button[@class="btn btn-sm btn-success pl-3 pr-3 btn-secondary"]')
    CLOSE_MODAL_EDIT_DESCRIPTIONS = (By.XPATH, '//button[@class="btn btn btn-secondary pl-3 pr-3 ml-2 btn-secondary '
                                               'btn-sm"]')

    SETTINGS_BUTTON = (By.XPATH, '//td[@aria-colindex="8"]//button')
    GENERAL_SETTINGS = (By.XPATH, "//a[contains(text(), 'General Settings')]")
    API_SETTINGS = (By.XPATH, "//a[contains(text(), 'API Settings')]")
    LINKS_SETTINGS = (By.XPATH, "//a[contains(text(), 'Links Settings')]")
    SMPT_SETTINGS = (By.XPATH, "//a[contains(text(), 'SMPT Settings')]")
    FEES_SETTINGS = (By.XPATH, "//a[contains(text(), 'Fees Settings')]")
    CUSTOM_JAVA_SCRIPT = (By.XPATH, "//a[contains(text(), 'Custom Java Script')]")
    LEGAL_SETTINGS = (By.XPATH, "//a[contains(text(), 'Legal Settings')]")
    EMAIL = (By.XPATH, "//a[contains(text(), 'Emails')]")
    ADD_BROKER = (By.XPATH, "//a[contains(text(), 'Add Broker')]")
    DEACTIVATED_WL = (By.XPATH, "//a[contains(text(), 'Deactivate')]")

    WL_NAME_INPUT = (By.ID, 'id="name"')
    WL_DOMAIN_INPUT = (By.ID, 'id="domain"')
    WL_URL = (By.ID, 'id="link"')
    WL_EMAIL = (By.ID, 'id="email"')
    SERVICE_EMAIL = (By.ID, 'id="cs_email"')
    INITIALS = (By.ID, 'id="initials"')
    SEND_EMAILS = (By.ID, 'id="from_name_email"')
    COPYRIGHT = (By.ID, 'id="copyright"')
    LANGUAGES_ADD_WL = (By.ID, 'id="languages"')
    RUS_LANGUAGE = (By.XPATH, "//span[contains(text(), 'Русский')]")
    CONNECT_MESSAGE = (By.ID, 'id="live_account_message"')
    FOOTER_DESCRIPTION = (By.ID, 'id="footer_description"')
    INVOICE_SETTINGS = (By.ID, 'id="invoice_company_data"')
    CHECK_LOGO_EDIT_WL = (By.ID, 'id="invoice_hide_logo"')
    WL_TYPES = (By.XPATH, '///div[@class="multiselect"]//span[@class="multiselect__single"]')
    PRIVATE_WHITE_LABELS = (By.XPATH, "//span[contains(text(), 'private white label')]")
    GENERAL_WHITE_LABELS = (By.XPATH, "//span[contains(text(), 'general white label')]")
    HYBRID_WHITE_LABELS = (By.XPATH, "//span[contains(text(), 'hybrid white label')]")
    BUSINESS_MODELS = (By.XPATH, '//div[@class="multiselect multiselect--above"]//span[@class="multiselect__single"]')
    VOLUME_BASED_COMPENSATION = (By.XPATH, "//span[contains(text(), 'volume based compensation')]")
    PERFORMANCE_BASED_COMPENSATION = (By.XPATH, "//span[contains(text(), 'performance based compensation')]")
    CUSTOM_TRADING_SERVER = (By.XPATH, '//div[@class="trading-servers-wrapper"]//a')
    DELETE_TRADING_SERVER_BUTTON = (By.XPATH, '//div[@class="trading-servers-wrapper"]//button')
    SUBMIT_DELETE_TRADING_SERVER = (By.XPATH, '//button[@class="btn btn btn-success pl-3 pr-3 btn-secondary btn-sm"]')
    EDIT_TRADING_SERVER_NAME = (By.ID, 'id="edit_trading_server_name"')
    EDIT_TRADING_SERVER_MASK = (By.ID, 'id="edit_trading_server_mask"')
    UPDATE_EDIT_TRADING_SERVER = (By.XPATH, '//div[@id="modal-window-edit-trading-server___BV_modal_body_"]//button')
    ADD_TRADING_SERVER = (By.XPATH, '//div[@class="white-labels-flex-wrapper"]//button[@type="submit"]')
    ADD_TRADING_SERVER_NAME = (By.ID, 'id="add_trading_server_name"')
    ADD_TRADING_SERVER_MASK = (By.ID, 'id="add_trading_server_mask"')
    CREATE_ADD_TRADING_SERVER = (By.XPATH, '//div[@id="modal-window-add-trading-server___BV_modal_body_"]//button')
    UPDATE_WL_BUTTON = (By.XPATH, '//div[@class="row"]//button[@class="btn btn btn-success btn-secondary btn-sm"]')

    SECRET_KEY_INPUT = (By.ID, 'id="wl_secret"')
    GENERATE_NEW_KEY = (By.XPATH, "//button[contains(text(), 'Generate a new key')]")
    API_URL_INPUT = (By.ID, 'id="wl_webhook_url"')
    SAVE_URL = (By.XPATH, "//button[contains(text(), 'Save URL')]")

    def edit_business_model(self, model):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(WhiteLabels.BUSINESS_MODELS)).click()
        wait.until(EC.presence_of_element_located(model)).click()
        name_button = wait.until(EC.presence_of_element_located(WhiteLabels.BUSINESS_MODELS)).text
        wait.until(EC.presence_of_element_located(WhiteLabels.UPDATE_WL_BUTTON)).click()
        time.sleep(5)
        return name_button

    def edit_wl_type(self, type_):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(WhiteLabels.WL_TYPES)).click()
        wait.until(EC.presence_of_element_located(type_)).click()
        name_button = wait.until(EC.presence_of_element_located(WhiteLabels.WL_TYPES)).text
        wait.until(EC.presence_of_element_located(WhiteLabels.UPDATE_WL_BUTTON)).click()
        time.sleep(5)
        return name_button

    def edit_general_settings_wl(self):
        wait = WebDriverWait(self.driver, 10)
        page = WhiteLabels(self.driver)

        name = page.edit_input(WhiteLabels.WL_NAME_INPUT)
        page.edit_input(WhiteLabels.WL_DOMAIN_INPUT)
        page.edit_input(WhiteLabels.WL_URL)
        page.edit_input(WhiteLabels.WL_EMAIL)
        page.edit_input(WhiteLabels.SERVICE_EMAIL)
        page.edit_input(WhiteLabels.INITIALS)
        page.edit_input(WhiteLabels.SEND_EMAILS)
        page.edit_input(WhiteLabels.COPYRIGHT)

        wait.until(EC.presence_of_element_located(WhiteLabels.LANGUAGES_ADD_WL)).click()
        wait.until(EC.presence_of_element_located(WhiteLabels.RUS_LANGUAGE)).click()

        page.edit_input(WhiteLabels.CONNECT_MESSAGE)
        page.edit_input(WhiteLabels.FOOTER_DESCRIPTION)
        page.edit_input(WhiteLabels.INVOICE_SETTINGS)

        wait.until(EC.presence_of_element_located(WhiteLabels.UPDATE_WL_BUTTON)).click()
        return name

    def review_trading_server(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            notes = len(wait.until(EC.presence_of_all_elements_located(WhiteLabels.CUSTOM_TRADING_SERVER)))
        except TimeoutException:
            notes = 0
        return notes

    def delete_trading_server(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(WhiteLabels.DELETE_TRADING_SERVER_BUTTON)).click()
        wait.until(EC.presence_of_element_located(WhiteLabels.SUBMIT_DELETE_TRADING_SERVER)).click()
        time.sleep(5)

    def edit_trading_server(self):
        wait = WebDriverWait(self.driver, 10)
        page = WhiteLabels(self.driver)
        name = page.edit_input(WhiteLabels.EDIT_TRADING_SERVER_NAME)
        wait.until(EC.presence_of_element_located(WhiteLabels.UPDATE_EDIT_TRADING_SERVER)).click()
        time.sleep(5)
        return name

    def add_trading_server(self):
        wait = WebDriverWait(self.driver, 10)
        page = WhiteLabels(self.driver)
        wait.until(EC.presence_of_element_located(WhiteLabels.ADD_TRADING_SERVER)).click()
        name = page.edit_input(WhiteLabels.ADD_TRADING_SERVER_NAME)
        page.edit_input(WhiteLabels.ADD_TRADING_SERVER_MASK)
        wait.until(EC.presence_of_element_located(WhiteLabels.CREATE_ADD_TRADING_SERVER)).click()
        time.sleep(5)
        return name

    def show_deactivated(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(WhiteLabels.SORTING_ID)).click()
        time.sleep(5)

    def review_brokers(self, size):
        wait = WebDriverWait(self.driver, 10)
        brokers = wait.until(EC.presence_of_all_elements_located(WhiteLabels.BROKERS))
        for broker in brokers:
            value = broker.text
            if int(value) > size:
                wait.until(EC.presence_of_element_located(WhiteLabels.BROKERS)).click()
                time.sleep(5)
                return value
                pass

    def invisible(self):
        wait = WebDriverWait(self.driver, 10)
        broker_invisible = wait.until(EC.presence_of_element_located(WhiteLabels.INVISIBLE_ICON))
        status = broker_invisible.text
        broker_invisible.click()
        wait.until(EC.presence_of_element_located(WhiteLabels.UPDATE)).click()
        return status

    def delete_broker(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(WhiteLabels.DELETE_ICON)).click()
        wait.until(EC.presence_of_element_located(WhiteLabels.DELETE_SUBMIT)).click()
        time.sleep(5)

    def open_settings(self, type_settings):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(WhiteLabels.SETTINGS_BROKER_BUTTON)).click()
        wait.until(EC.presence_of_element_located(type_settings)).click()
        time.sleep(5)
        header = wait.until(EC.presence_of_element_located(type_settings)).text
        return header

    def edit_input(self, type_input):
        wait = WebDriverWait(self.driver, 10)
        value = 'Autotest' + str(date.today())
        element = wait.until(EC.presence_of_element_located(type_input))
        element.clear()
        element.send_keys(value)
        return value

    def edit_general_settings_broker(self):
        inputs = {WhiteLabels.BROKER_NAME_INPUT,
                  WhiteLabels.WEIGHT_INPUT,
                  WhiteLabels.ACCOUNT_LINK_INPUT,
                  WhiteLabels.EMAIL_INPUT
                  }
        wait = WebDriverWait(self.driver, 10)
        page = WhiteLabels(self.driver)
        for input_ in inputs:
            page.edit_input(input_)
        wait.until(EC.presence_of_element_located(WhiteLabels.CHECK_LOGO)).click()
        wait.until(EC.presence_of_element_located(WhiteLabels.UPDATE_GENERAL_SETTINGS)).click()
        wait.until(EC.presence_of_element_located(WhiteLabels.CLOSE_MODAL_GENERAL_SETTINGS)).click()

    def edit_server(self):
        wait = WebDriverWait(self.driver, 10)
        page = WhiteLabels(self.driver)
        wait.until(EC.presence_of_element_located(WhiteLabels.EDIT_SERVER_BUTTON)).click()
        page.edit_input(WhiteLabels.UPDATE_SERVER_NAME_INPUT)
        page.edit_input(WhiteLabels.UPDATE_SERVER_MASK)
        wait.until(EC.presence_of_element_located(WhiteLabels.UPDATE_SERVER_BUTTON)).click()
        wait.until(EC.presence_of_element_located(WhiteLabels.CLOSE_MODAL_EDIT_SERVERS)).click()
        time.sleep(5)

    def delete_server(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(WhiteLabels.DELETE_SERVER_BUTTON)).click()
        wait.until(EC.presence_of_element_located(WhiteLabels.SUBMIT_DELETE_SERVER)).click()
        time.sleep(5)

    def add_server(self):
        wait = WebDriverWait(self.driver, 10)
        page = WhiteLabels(self.driver)
        wait.until(EC.presence_of_element_located(WhiteLabels.ADD_SERVER_BUTTON)).click()
        name = page.edit_input(WhiteLabels.NAME_SERVER_ADD_INPUT)
        page.edit_input(WhiteLabels.MASK_ADD_INPUT)
        wait.until(EC.presence_of_element_located(WhiteLabels.CREATE_ADD_SERVER)).click()
        wait.until(EC.presence_of_element_located(WhiteLabels.CLOSE_MODAL_ADD_SERVERS)).click()
        time.sleep(5)
        return name

    def edit_descriptions(self):
        global descriptions
        types = {WhiteLabels.RISK_WARNING_TYPE,
                 WhiteLabels.CONDITIONS_TYPE,
                 WhiteLabels.PRIVACY_TYPE,
                 WhiteLabels.AFFILIATE_TYPE
                 }
        wait = WebDriverWait(self.driver, 10)
        page = WhiteLabels(self.driver)
        wait.until(EC.presence_of_element_located(WhiteLabels.LANGUAGES_BUTTON)).click()
        languages = wait.until(EC.presence_of_all_elements_located(WhiteLabels.LANGUAGES))
        language = random.choice(languages)
        language.click()

        for type_descriptions in types:
            wait.until(EC.presence_of_element_located(WhiteLabels.TYPES_DESCRIPTIONS)).click()
            wait.until(EC.presence_of_element_located(type_descriptions)).click()
            descriptions = page.edit_input(WhiteLabels.TEXT_INPUT)
            wait.until(EC.presence_of_element_located(WhiteLabels.UPDATE_DESCRIPTIONS_BUTTON)).click()
        self.driver.back()
        return descriptions

    def check_deactivated(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(WhiteLabels.DEACTIVATED)).click()
        time.sleep(10)






