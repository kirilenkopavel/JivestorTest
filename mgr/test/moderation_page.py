from selenium.webdriver.common.by import By

from mgr.pages.page import BasePage


class Moderation(BasePage):

    STATUS_NEW = (By.XPATH, '//div[@style="display: flex;"]/div[1]/button')
    STATUS_APPROVED = (By.XPATH, '//div[@style="display: flex;"]/div[2]/button')
    DISCRIPTION_TAB = (By.XPATH, "//span[contains(text(), 'Description')]")
    REVIEWS_TAB = (By.XPATH, "//span[contains(text(), 'Reviews')]")
    DELETE_ICON_DISCRIPTION = (By.XPATH, '//td[@aria-colindex="4"]//a')
    DELETE_ICON_REVIEW = (By.XPATH, '//td[@aria-colindex="5"]//a')
    SORTING_DATE = (By.XPATH, '//th[@aria-colindex="2"]')
    DATE = (By.XPATH, '//td[@aria-colindex="2"]')
    EDIT_ICON = (By.XPATH, '//td[@aria-colindex="3"]//*[@class="bi-pencil-square b-icon bi"]')
    SUBMIT_DELETE = (By.XPATH, "//button[contains(text(), 'Delete')]")
    TEXT = (By.XPATH, '//td[@aria-colindex="3"]/div[4]')
    INPUT_TEXT = (By.XPATH, '//div[@class="inline-buttons__textarea-description"]/textarea ')
    APPROVED_REVIEW_ICON = (By.XPATH, '//td[@aria-colindex="5"]//div[@class="customIcons"]/div[1]/a')
    DELETE_NEW_REVIEW_ICON = (By.XPATH, '//td[@aria-colindex="5"]//div[@class="customIcons"]/div[2]/a')




