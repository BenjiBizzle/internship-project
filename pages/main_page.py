from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    CLICK_SECONDARY_OPTION = (By.CSS_SELECTOR, "#w-node-b528dfcf-d2ee-f936-302e-86e97f0796ec-7f66df20")
    CLICK_FILTERS = (By.CSS_SELECTOR, ".filter-button")
    CLICK_FROM_PRICE = (By.CSS_SELECTOR, "[wized='unitPriceFromFilter']")
    CLICK_TO_PRICE = (By.CSS_SELECTOR, "[wized='unitPriceToFilter']")
    CLICK_APPLY = (By.CSS_SELECTOR, "[wized='applyFilterButtonMLS']")
    CLICK_SETTINGS = (By.CSS_SELECTOR, "[href='/settings']")

    def click_secondary(self):
        self.click(*self.CLICK_SECONDARY_OPTION)

    def click_filters(self):
        self.click(*self.CLICK_FILTERS)

    def verify_current_url(self):
        self.verify_url('https://soft.reelly.io/secondary-listings')

    def click_from_price(self):
        self.click(*self.CLICK_FROM_PRICE)
        self.find_element(*self.CLICK_FROM_PRICE).send_keys('1200000')

    def click_to_price(self):
        self.click(*self.CLICK_TO_PRICE)
        self.find_element(*self.CLICK_TO_PRICE).send_keys('2000000')

    def click_apply(self):
        self.click(*self.CLICK_APPLY)

    def click_settings(self):
        self.click(*self.CLICK_SETTINGS)

