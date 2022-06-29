import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from dev.pages.page import BasePage


class TradingTerminalPage(BasePage):

    TIME_FRAME = (By.XPATH, '//a[@ng-click="changeTimeFrame(timeFrame)"]')
    M1 = (By.XPATH, "//a[contains(text(), 'M1')]")
    M5 = (By.XPATH, "//a[contains(text(), 'M5')]")
    M15 = (By.XPATH, "//a[contains(text(), 'M15')]")
    H1 = (By.XPATH, "//a[contains(text(), 'H1')]")
    H4 = (By.XPATH, "//a[contains(text(), 'H4')]")
    D1 = (By.XPATH, "//a[contains(text(), 'D1')]")
    W1 = (By.XPATH, "//a[contains(text(), 'W1')]")
    WN = (By.XPATH, "//a[contains(text(), 'MN')]")
    ACTIV_TIME_FRAME = (By.XPATH, '//div[@class="chart-tabs"]//li[@class="ng-scope active"]/a')
    ORDER = (By.XPATH, '//a[@ng-click="openNewOrderPopup()"]')
    ORDER_SUBMIT = (By.XPATH, '//form[@class="popup-form ng-valid ng-dirty ng-valid-parse ng-submitted"]'
                              '//div[@class="form-buttons"]//span')
    TRADING_TOOL = (By.XPATH, '//a[@ng-click="setCurrentInstrument(instrument)"]')
    ACTIV_TRADING_TOOL = (By.XPATH, '//li[@class="ng-scope active"]/a[@ng-click="setCurrentInstrument(instrument)"]')
    EUR_USD = (By.XPATH, "//a[contains(text(), 'EURUSD')]")
    GBP_USD = (By.XPATH, "//a[contains(text(), 'GBPUSD')]")
    USD_JPY = (By.XPATH, "//a[contains(text(), 'USDJPY')]")
    USD_RUB = (By.XPATH, "//a[contains(text(), 'USDRUB')]")
    ADD_ICON = (By.XPATH, '//a[@ng-click="toggleInstrumentPopup()"]')
    LIST_TOOLS = (By.XPATH, '//li[@ng-repeat="instrument in instrumentList | filter:instrumentSearch"]//label')
    SEARCH_INPUT = (By.ID, 'autocomplete')
    INPUT_ORDER_SIZE = (By.ID, 'order_volume')
    SELL_ORDER = (By.XPATH, '//label[@for="order_sell"]')
    TYPE_ORDER = (By.ID, 'order_type')
    INPUT_STOP_LOSS = (By.ID, 'pop_order_loss')
    INPUT_TAKE_PROFIT = (By.ID, 'order_profit')
    SELL_BUTTON = (By.XPATH, '//div[@ng-click="orderBuy(marketData.best_bid, orderType.sell)"]')
    INPUT_TRADE_SIZE = (By.XPATH, '//span[@class="ui-spinner ui-widget ui-widget-content ui-corner-all"]')
    TRADE_SUBMIT = (By.XPATH, '//a[@ng-click="orderConfirm(); orderBuy(marketData.best_bid, orderType.sell); '
                              'closeThisDialog()"]')

    def selection_time_frame(self, element):
        time_frame = self.driver.find_element(*element)
        time_frame.click()
        time.sleep(2)
        value = time_frame.text
        return value

    def selection_trading_tool(self, tool):
        trading_tool = self.driver.find_element(*tool)
        trading_tool.click()
        time.sleep(2)
        value = trading_tool.text
        return value

    def add_trading_tool(self, tool):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(TradingTerminalPage.ADD_ICON)).click()
        value = wait.until(EC.presence_of_all_elements_located(TradingTerminalPage.LIST_TOOLS))
        wait.until(EC.presence_of_element_located(TradingTerminalPage.SEARCH_INPUT)).send_keys(tool)
        wait.until(EC.presence_of_element_located(TradingTerminalPage.LIST_TOOLS)).click()
        time.sleep(2)
        return len(value)

    def delete_trading_tool(self, tool):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(TradingTerminalPage.ADD_ICON)).click()
        wait.until(EC.presence_of_element_located(TradingTerminalPage.SEARCH_INPUT)).send_keys(tool)
        wait.until(EC.presence_of_element_located(TradingTerminalPage.LIST_TOOLS)).click()

    def open_order(self, type_trade, type_order, size, stop_loss, take_profit):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(TradingTerminalPage.ORDER)).click()
        time.sleep(2)
        wait.until(EC.presence_of_element_located(type_trade)).click()
        time.sleep(2)
        Select(self.driver.find_element(*TradingTerminalPage.TYPE_ORDER)).select_by_visible_text(type_order)
        time.sleep(2)
        wait.until(EC.presence_of_element_located(TradingTerminalPage.INPUT_ORDER_SIZE)).send_keys(size)
        time.sleep(2)
        wait.until(EC.presence_of_element_located(TradingTerminalPage.INPUT_STOP_LOSS)).send_keys(stop_loss)
        time.sleep(2)
        wait.until(EC.presence_of_element_located(TradingTerminalPage.INPUT_TAKE_PROFIT)).send_keys(take_profit)
        time.sleep(2)
        wait.until(EC.presence_of_element_located(TradingTerminalPage.ORDER_SUBMIT)).click()

    def open_trade(self, type_trade, size):
        wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.presence_of_element_located(TradingTerminalPage.INPUT_TRADE_SIZE)).send_keys(size)
        wait.until(EC.presence_of_element_located(type_trade)).click()
        try:
            wait.until(EC.presence_of_element_located(TradingTerminalPage.TRADE_SUBMIT)).click()
        except TimeoutException:
            return




