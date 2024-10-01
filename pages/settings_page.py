from selenium.webdriver.common.by import By

from pages.base_page import Page


class SettingsPage(Page):
    CONNECT_COMPANY_BTN = (By.CSS_SELECTOR, "[class='get-free-period menu']")

    def verify_current_url(self):
        self.verify_url('https://soft.reelly.io/settings')

    def connect_comp_button(self):
        self.find_elements(*self.CONNECT_COMPANY_BTN)
