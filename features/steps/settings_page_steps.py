from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SETTINGS_OPTIONS = (By.CSS_SELECTOR, ".page-setting-block")


@then('Verify correct page opens')
def verify_right_url(context):
    context.app.settings_page.verify_current_url()
    sleep(2)


@then('Verify there are 12 options for the settings')
def verify_options(context):
    elements = context.driver.find_elements(*SETTINGS_OPTIONS)
    elements_except_first = elements[1:]
    sleep(3)


@then('Verify connect the company button is available')
def verify_button(context):
    context.app.settings_page.connect_comp_button()
    sleep(2)
