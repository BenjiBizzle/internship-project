from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_main(context):
    context.app.login_page.open()
    sleep(4)


@when('Log in to the page')
def click_login_fields(context):
    context.app.login_page.click_email()
    context.app.login_page.click_password()
    sleep(2)
    context.app.login_page.click_continue()




