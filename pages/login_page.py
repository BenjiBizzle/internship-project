from selenium.webdriver.common.by import By
from pages.base_page import Page


class LoginPage(Page):
    CLICK_EMAIL_BOX = (By.CSS_SELECTOR, "#email-2")
    CLICK_PASSWORD_BOX = (By.CSS_SELECTOR, '#field')
    CLICK_CONTINUE = (By.CSS_SELECTOR, "a[wized='loginButton']")

    def open(self):
        self.open_url('https://soft.reelly.io/sign-in')

    def click_email(self):
        self.click(*self.CLICK_EMAIL_BOX)
        self.find_element(*self.CLICK_EMAIL_BOX).send_keys('bballardo209@gmail.com')

    def click_password(self):
        self.click(*self.CLICK_PASSWORD_BOX)
        self.find_element(*self.CLICK_PASSWORD_BOX).send_keys('Fuckyou209')

    def click_continue(self):
        self.click(*self.CLICK_CONTINUE)
