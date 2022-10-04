from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

from dev_new.pages.data_test import DataTest
from dev_new.pages.page import BasePage


class NavigatePage(BasePage):

    STRATEGIES_TAB = (By.XPATH, '//a[@href="/traders"]') # Вкладка Стратегии в верхнем меню навишации
    TRADING_TERMINAL_TAB = (By.XPATH, '//a[@href="/sf/terminal"]') # Вкладка Торговый терминал в верхнем меню навишации

    BURGER_MENU = (By.XPATH, '//span[@class="fas fa-bars p-button-icon"]') # Иконка "бургер" меню в верхнем меню навишации

    STRATEGIES_MENU_BUTTON = (By.XPATH, '//span[@class="p-menuitem-icon fas fa-arrow-trend-up"]') # Вкладка Стратегии в меню пользователя
    TRADING_TERMINAL_MENU_BUTTON = (By.XPATH, '//span[@class="p-menuitem-icon fas fa-chart-line"]') # Вкладка Торговый терминал в меню пользователя
    PROFILE_MENU_BUTTON = (By.XPATH, '//span[@class="p-menuitem-icon fas fa-user"]') # Кнопка Профиль в меню пользователя
    SETTING_MENU_BUTTON = (By.XPATH, '//span[@class="p-menuitem-icon fas fa-cog"]') # Кнопка Настройки в меню пользователя
    LOGOUT_MENU_BUTTON = (By.XPATH, '//span[@class="p-menuitem-icon fas fa-sign-out-alt"]') # Кнопка Выйти в меню пользователя
    CLOSE_MENU_ICON = (By.XPATH, '//span[@class="p-sidebar-close-icon pi pi-times"]') # Кнопка Х закрыть меню пользователя
    
    SELECT_ROLE_BUTTON = (By.XPATH, '//span[@class="p-dropdown-trigger-icon pi pi-chevron-down"]') # Выбор пользователя в меню навигации
    FOLLOWER_ROLE = (By.XPATH, '//li[@aria-label="Follower"]') # Роль фолловера
    PROVIDER_ROLE = (By.XPATH, '//li[@aria-label="Provider"]') # Роль провайдера

    SELECT_ACCOUNT_TYPE = (By.XPATH, '//div[@class="jv__sidebar-menu"]//div[@class="p-dropdown p-component p-inputwrapper'
                                     ' p-inputwrapper-filled jv__basic-select__input"][1]')
    PERSONAL_ACCOUNT_TYPE = (By.XPATH, '//li[@aria-label="Personal account"]')
    CORPORATE_ACCOUNT_TYPE = (By.XPATH, '//li[@aria-label="Corporate account"]')
    COMPANY_NAME_INPUT = (By.NAME, 'companyName') # Поле Название компании

    global wait 
    wait = WebDriverWait(10)

    """
    @param role Роль пользователя
    """
    @allure.step('Переключение роли - {role}')
    def selection_role(self, role):
        wait.until(EC.visibility_of_element_located(NavigatePage.SELECT_ROLE_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(role)).click()

    """
    @param tab Вкладка
    """
    @allure.step('Открытие вкладки - {tab}')
    def open_page(self, tab):
        wait.until(EC.visibility_of_element_located(tab)).click()

    @allure.step('Открыть настройки профиля')
    def open_profile_settings(self):
        wait.until(EC.visibility_of_element_located(NavigatePage.PROFILE_SETTINGS_BUTTON)).click()

    """
    @param company_name  Название компании
    """
    @allure.step('Заполнение инпута Название компании - {company_name}')
    def set_company_name(self, company_name):
        wait.until(EC.visibility_of_element_located(NavigatePage.COMPANY_NAME_INPUT)).send_keys(company_name)

    """
    @param type_account  Тип аккаунта
    """
    @allure.step('Выбор типа аккаунта - {type_account}')
    def set_type_account(self, type_account):
        wait.until(EC.visibility_of_element_located(NavigatePage.SELECT_ACCOUNT_TYPE)).click()
        wait.until(EC.visibility_of_element_located(type_account)).click()
        if type_account == NavigatePage.CORPORATE_ACCOUNT_TYPE:
            NavigatePage.set_company_name('Автотест')



